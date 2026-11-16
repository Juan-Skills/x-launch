# /x-launch · a Claude Code skill for launching on X

A 40-step launch method for X, with 10 agents, 10 prompts and 30 templates, turned into a Claude Code skill. It starts from the method unfair.so published after 99 launches in 11 weeks (unfair.so/strategy), rewritten and adapted so Claude can run it.

The idea: one strong post published at an exact minute, and 30 to 60 creators quoting it with their own angle within the first hour. Everything else prepares that moment or collects what it brings.

## What the command does

| Command | What happens |
|---|---|
| `/x-launch new <what you're launching>` | Reads what it already knows (memory, notes, your site), asks 2-3 questions, writes the one-page brief, builds the tracking folder and the 40 steps with durations and due times counted from T0, and a tracker page that shows one step at a time. |
| `/x-launch status <what moved>` | Ticks steps, logs blockers, opens the next step with its template and prompt, hands the work to the right agent, runs the GO / NO-GO at T−12h. |
| `/x-launch retro` | Checks the creators' posts, builds the lead list, one-page retro (expected vs actual), books the next slot. |

## The 10 agents

Angle Scout, Launch Manager, Post Critic, Creator Scout, Quote Drafter, Network Scorer, Reply Scout, Wave Watcher, Lead Lister, Retro Analyst. They read, count and draft. None of them posts, DMs or pays: you press the button.

## Install

```bash
cp -R x-launch ~/.claude/skills/
```

Python 3 is all you need. In the Claude app the tracker becomes an artifact; elsewhere it's a `tracker.html` file you open in your browser. For agents to read X: a browser logged into X, the X API, or posts pasted by hand.

## What it creates

```
x-launches/
├── Backlog.md                launch ideas in reserve
├── Creators.md               your creator log, updated after each launch
├── launch-log.csv            one row per launch
└── 2026-12-02-my-launch/
    ├── 00 My launch.md       home: status and links
    ├── Brief.md              the 11-line brief
    ├── To-do.md              the 40 steps, generated
    ├── Decisions.md · Log.md · Retro.md
    ├── work/                 what the agents hand back
    ├── plan.json             the source of truth
    └── tracker.html          the tracker page
```

The files read fine as plain text and open in Obsidian (`[[...]]` links).

MIT license for the skill. The original method belongs to its authors; this repo rewrites it and credits them.
