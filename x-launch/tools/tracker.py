#!/usr/bin/env python3
"""Tracks a launch on X from plan.json.

Usage:
  python3 tracker.py FOLDER --init --project "Name" --t0 2026-12-02T18:00 --tz America/New_York [--existing-channel]
                                              # creates the folder: 40-step plan, .md files, tools
  python3 tracker.py FOLDER                   # rebuilds tracker.html and To-do.md, prints where things stand
  python3 tracker.py FOLDER --status 3=done   # changes a step's status (repeatable)
  python3 tracker.py FOLDER --status 5=blocked --note 5="waiting on the video"
  python3 tracker.py FOLDER --gate G3=yes --gate G6=no    # GO / NO-GO gates (yes, no, clear)

Statuses: todo, doing, done, blocked, dropped.
Python standard library only.
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
from datetime import datetime, timedelta
from pathlib import Path

try:
    from zoneinfo import ZoneInfo
except ImportError:  # Python < 3.9
    ZoneInfo = None

STATUSES = ("todo", "doing", "done", "blocked", "dropped")
BOXES = {"todo": "[ ]", "doing": "[~]", "done": "[x]", "blocked": "[!]", "dropped": "[-]"}


def zone(plan: dict):
    if ZoneInfo and plan.get("tz"):
        try:
            return ZoneInfo(plan["tz"])
        except Exception:
            sys.exit(f"Unknown time zone: {plan['tz']} (example: America/New_York)")
    return None


def local(text: str, tz) -> datetime:
    d = datetime.fromisoformat(text)
    return d.replace(tzinfo=tz) if (tz and d.tzinfo is None) else d


def read_plan(folder: Path) -> dict:
    path = folder / "plan.json"
    if not path.exists():
        sys.exit(f"No plan.json in {folder}")
    return json.loads(path.read_text(encoding="utf-8"))


def due(step: dict, t0: datetime | None, tz=None) -> datetime | None:
    if step.get("due"):
        return local(step["due"], tz)
    if t0 is not None and step.get("offset_h") is not None:
        return t0 + timedelta(hours=float(step["offset_h"]))
    return None


def dur(minutes: float) -> str:
    minutes = int(round(minutes))
    if minutes < 60:
        return f"{minutes}m"
    h, m = divmod(minutes, 60)
    return f"{h}h{m:02d}" if m else f"{h}h"


def compute(plan: dict, now: datetime) -> dict:
    tz = zone(plan)
    t0 = local(plan["t0"], tz) if plan.get("t0") else None
    plan["_t0_ms"] = t0.timestamp() * 1000 if t0 else None
    live = [s for s in plan["steps"] if s.get("status", "todo") != "dropped"]
    done = [s for s in live if s.get("status") == "done"]
    for s in plan["steps"]:
        d = due(s, t0, tz)
        s["_due"] = d.replace(tzinfo=None).isoformat(timespec="minutes") if d else None
        s["_due_ms"] = d.timestamp() * 1000 if d else None
        s["_late"] = bool(d and d < now and s.get("status") not in ("done", "dropped"))
    left = sorted((s for s in live if s.get("status") != "done"), key=lambda s: (s["_due"] or "9999", s["id"]))
    return {
        "done": len(done), "total": len(live),
        "percent": round(100 * len(done) / len(live)) if live else 0,
        "total_min": sum(s.get("minutes", 0) for s in live),
        "left_min": sum(s.get("minutes", 0) for s in live if s.get("status") != "done"),
        "late": [s for s in live if s["_late"]],
        "blocked": [s for s in live if s.get("status") == "blocked"],
        "next": left[0] if left else None,
    }


def verdict(plan: dict) -> str:
    states = [g.get("state") or "" for g in plan.get("gates", [])]
    if not states or ("" in states and "no" not in states):
        return "pending"
    return "NO-GO" if "no" in states else "GO"


def write_todo(folder: Path, plan: dict, st: dict, now: datetime) -> None:
    lines = [
        "---", f"updated: {now.date().isoformat()}", "generated_by: tracker.py (do not edit by hand)", "---",
        f"# To-do · {plan['project']}", "",
        f"Progress: **{st['done']}/{st['total']} steps ({st['percent']}%)**, "
        f"about {dur(st['left_min'])} of work left out of {dur(st['total_min'])}.",
    ]
    if plan.get("t0"):
        lines.append(f"Launch (T0): {plan['t0'].replace('T', ' at ')} ({plan.get('tz', 'local time')}).")
    if st["late"]:
        lines.append("Late: " + ", ".join(f"#{s['id']} {s['title']}" for s in st["late"]) + ".")
    if plan.get("gates"):
        lines += ["", "GO / NO-GO: " + " · ".join(f"{g['id']} {g.get('state') or '?'}" for g in plan["gates"]) + f" → **{verdict(plan)}**"]
    lines += ["", "Key: [ ] todo · [~] doing · [x] done · [!] blocked · [-] dropped", ""]
    phase = None
    for s in plan["steps"]:
        if s.get("phase") != phase:
            phase = s.get("phase")
            lines += ["", f"## {phase}", ""]
        when = s["_due"].replace("T", " ") if s["_due"] else "no date"
        bits = [dur(s.get("minutes", 0)), f"by {when}", s.get("owner", "")]
        if s.get("agent"):
            bits.append(f"agent: {s['agent']}")
        line = f"- {BOXES.get(s.get('status', 'todo'), '[ ]')} **#{s['id']} {s['title']}** · " + " · ".join(b for b in bits if b)
        if s["_late"]:
            line += " · **LATE**"
        lines.append(line)
        if s.get("note"):
            lines.append(f"  - {s['note']}")
    (folder / "To-do.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


FILES = {
    "Brief.md": """---
updated: {date}
---
# Brief · {project}

WIN PLAN        unknown (the outcome, the lever that gets it, the number)
WHAT            unknown (what is launching, in one sentence)
KPI             unknown (one number and its target, counted the next morning)
TIME            {t0} ({tz}), in the words of the person who presses Post
POST FROM       unknown (the account that posts)
LINK            unknown (the one link, visible without "Show more")
BUDGET          unknown (what goes to creators)
PROMISED        unknown (what people were told they would get)
OPEN QUESTIONS  unknown (what is missing, and who can answer)
RISKS           unknown (what could sink it)
NOT THIS TIME   unknown (what waits for the next launch)
""",
    "Decisions.md": "---\nupdated: {date}\n---\n# Decisions · {project}\n\nNewest first. Format: `- **YYYY-MM-DD · the choice** · why: … · who: …`\n",
    "Log.md": "---\nupdated: {date}\n---\n# Log · {project}\n\n- {date}: folder created, launch on {t0} ({tz}).\n",
}

HOME = """---
updated: {date}
status: preparing
---
# {project}

Launch on X. T0: {t0} ({tz}).

- The 40-step to-do: [[To-do]] · the tracker: `tracker.html`
- The brief: [[Brief]]
- Choices made: [[Decisions]]
- Day by day: [[Log]]
- After launch: [[Retro]]
"""

SHARED = {
    "Backlog.md": "---\nupdated: {date}\n---\n# Launch backlog\n\nIdeas for upcoming launches (step 03). One line each: `- angle in one sentence · type · first line of the post · who it is for`.\n",
    "Creators.md": "---\nupdated: {date}\n---\n# Creator log\n\nOne row per creator, updated after every launch (steps 15 and 38).\n\n```csv\nhandle,followers,audience,launches_with_us,last_launch,last_paid_post_elsewhere,avg_quote_views,best_quote_url,price,notes,book_again\n```\n",
    "launch-log.csv": "date,angle,account,post_url,creators,creator_budget,views_48h,likes,bookmarks,replies,quotes,visits,signups,paid,new_mrr,cost_per_signup,notes\n",
}


def init(a) -> None:
    if not (a.project and a.t0):
        sys.exit("--init needs --project and --t0")
    d = a.folder
    if (d / "plan.json").exists():
        sys.exit(f"{d}/plan.json already exists: nothing overwritten")
    datetime.fromisoformat(a.t0)
    here = Path(__file__).resolve().parent
    plan = json.loads((here / "plan-template.json").read_text(encoding="utf-8"))
    plan.update(project=a.project, t0=a.t0, tz=a.tz)
    zone(plan)
    d.mkdir(parents=True, exist_ok=True)
    date = datetime.now().date().isoformat()
    plan["updated"] = date
    if a.existing_channel:
        for s in plan["steps"]:
            if s["phase"].startswith("Once"):
                s["status"] = "done"
                s["note"] = "already in place from an earlier launch"
    (d / "plan.json").write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for name in ("tracker.py", "tracker-template.html"):
        if (here / name).resolve() != (d / name).resolve():
            shutil.copy2(here / name, d / name)
    (d / "work").mkdir(exist_ok=True)
    values = dict(project=a.project, t0=a.t0.replace("T", " at "), tz=a.tz, date=date)
    for name, text in FILES.items():
        if not (d / name).exists():
            (d / name).write_text(text.format(**values), encoding="utf-8")
    shared = d.resolve().parent
    for name, text in SHARED.items():
        if not (shared / name).exists():
            (shared / name).write_text(text.format(date=date), encoding="utf-8")
    home = d / f"00 {a.project}.md"
    if not home.exists():
        home.write_text(HOME.format(**values), encoding="utf-8")
    print(f"Folder created: {d} (40 steps, files, tools)")


def write_html(folder: Path, plan: dict, st: dict, now: datetime) -> None:
    template = Path(__file__).with_name("tracker-template.html")
    if not template.exists():
        sys.exit(f"Template not found: {template}")
    data = dict(plan)
    data["verdict"] = verdict(plan)
    data["generated_ms"] = now.timestamp() * 1000
    text = json.dumps(data, ensure_ascii=False, indent=1).replace("</", "<\\/")
    html = template.read_text(encoding="utf-8").replace("__PLAN_JSON__", text)
    html = html.replace("__TITLE__", plan["project"].replace("<", "&lt;"))
    (folder / "tracker.html").write_text(html, encoding="utf-8")


def main() -> None:
    p = argparse.ArgumentParser(description="Track a launch on X")
    p.add_argument("folder", type=Path)
    p.add_argument("--status", action="append", default=[], help="ID=status")
    p.add_argument("--note", action="append", default=[], help='ID="text"')
    p.add_argument("--gate", action="append", default=[], help="G1=yes|no|clear")
    p.add_argument("--now", help="reference time (tests), YYYY-MM-DDTHH:MM")
    p.add_argument("--init", action="store_true", help="create the folder from the template plan")
    p.add_argument("--project")
    p.add_argument("--t0", help="YYYY-MM-DDTHH:MM, local time in --tz")
    p.add_argument("--tz", default="UTC")
    p.add_argument("--existing-channel", action="store_true", help="the 'once' steps are already done")
    a = p.parse_args()
    if a.init:
        init(a)

    plan = read_plan(a.folder)
    by_id = {s["id"]: s for s in plan["steps"]}
    for field, values in (("status", a.status), ("note", a.note)):
        for v in values:
            ident, eq, val = v.partition("=")
            if not eq:
                sys.exit(f"Missing '=' in --{field} {v} (example: --{field} 3=...)")
            if not ident.isdigit() or int(ident) not in by_id:
                sys.exit(f"Unknown step: {ident}")
            if field == "status" and val not in STATUSES:
                sys.exit(f"Unknown status: {val} (pick one of {', '.join(STATUSES)})")
            by_id[int(ident)][field] = val
    gates = {g["id"]: g for g in plan.get("gates", [])}
    for v in a.gate:
        ident, _, val = v.partition("=")
        if ident not in gates or val not in ("yes", "no", "clear"):
            sys.exit(f"Invalid gate: {v} (example: --gate G3=yes)")
        gates[ident]["state"] = "" if val == "clear" else val

    tz = zone(plan)
    now = local(a.now, tz) if a.now else datetime.now(tz).replace(second=0, microsecond=0)
    if a.status or a.note or a.gate:
        plan["updated"] = now.replace(tzinfo=None).isoformat(timespec="minutes")
        clean = {**{k: v for k, v in plan.items() if not k.startswith("_")},
                 "steps": [{k: v for k, v in s.items() if not k.startswith("_")} for s in plan["steps"]]}
        (a.folder / "plan.json").write_text(json.dumps(clean, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    st = compute(plan, now)
    write_todo(a.folder, plan, st, now)
    write_html(a.folder, plan, st, now)

    print(f"{plan['project']}: {st['done']}/{st['total']} steps ({st['percent']}%), {dur(st['left_min'])} left")
    for s in st["late"]:
        print(f"  LATE     #{s['id']} {s['title']} (due {s['_due'].replace('T', ' ')})")
    for s in st["blocked"]:
        print(f"  BLOCKED  #{s['id']} {s['title']} {('· ' + s['note']) if s.get('note') else ''}")
    if plan.get("gates"):
        print(f"  GO/NO-GO {verdict(plan)}")
    if st["next"]:
        s = st["next"]
        print(f"  NEXT     #{s['id']} {s['title']} ({dur(s.get('minutes', 0))}, {s.get('owner') or 'unassigned'})")


if __name__ == "__main__":
    main()
