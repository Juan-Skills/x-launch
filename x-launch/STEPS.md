# The 40 steps of a launch on X

Based on the method unfair.so published after 99 launches in 11 weeks, rewritten and adapted for Claude Code. For each step you get when it happens, why it matters, what to do, and the pitfalls.

# Once, before your first launch

Five choices you make one time. They are what turn a one-off launch into a habit you can repeat every week.

<a id="step-01"></a>
## 01 · Put a revenue number on the launch before you prepare it

**When**: once · **Prompt**: [Size a launch from revenue](PROMPTS.md#size-from-revenue)

Views are easy to get, and they are not what you want. First decide what the launch should bring in, in signups and in money. Then work back to the reach and the budget you need to get there.

1. Pick one metric you can count the next morning: signups, booked demos, paying customers or new monthly revenue.
2. Write the target next to the spend. A rule of thumb used at unfair.so, borrowed from a founder: new monthly revenue in the first month should roughly match what the launch cost.
3. Redo the math with your own funnel. The prompt runs the numbers for three scenarios.
4. Put that number in the brief (step 07) and check it again three days later (step 40).

**Starting conversion rates (unfair.so benchmark, 2026)**

| Stage | What they see |
|---|---|
| Views → site visits | about 1,000 visits per 100,000 views, ranging from 300 to 6,000 |
| Visits → signups | depends on your landing page: measure it first |
| Signups → paying customers | depends on your product; one B2B tool they launch converts 8 to 9% of its trials |

Only the views → visits rate and its range come from their experience. The rest is your product, and it moves the result more than reach does.

**A worked example (unfair.so, their own launch)**: $2,905 and one day of prep. Two days later, 50 demos on the calendar and $12,000 in new monthly revenue, which is $36,000 back over a three-month customer lifetime.

**Pitfalls**
- Aiming for a view count: you hit it and learn nothing.
- Trusting one viral post. A founder told them about days at +$10,000 in monthly revenue, and about multi-million-view posts that brought in nothing. The difference was who saw them.
- Judging the method on a single launch. Give it six tries.

<a id="step-02"></a>
## 02 · Give every launch its own trail

**When**: once · **Template**: [The launch log](TEMPLATES.md#launch-log)

With two launches a week landing in the same signup curve, you can't tell which angle paid off. So each launch gets its own link, its own code and a question at signup.

1. One UTM campaign per launch: `utm_source=x&utm_campaign=launch-date-angle`. Creators reuse the same campaign with `utm_content={{their_handle}}`.
2. One promo code per launch, in the post and in the quotes.
3. One question at signup: "Where did you hear about us?", free text.
4. One row per launch in a spreadsheet: views, visits, signups, paying customers, revenue, spend.

**Why a code beats a link.** A UTM link only counts the person who clicks inside the post. Someone who watches the video, opens your profile the next day and types your URL by hand stays invisible. The code catches them. It also gives the creator something concrete to say: a number of spots, a deadline.

Seen at unfair.so: one launch capped its code at 200 uses for the first hours, then announced the cap was going up to 500. That gave them a second post on the same launch, and a reason to act for everyone who had seen the first one.

**Pitfalls**
- One UTM for the whole month.
- Looking only at last click. Launch traffic keeps coming in for days through direct visits and search.
- No signup question, when it's the cheapest measurement you will ever build.

<a id="step-03"></a>
## 03 · Fill the backlog: everything is a launch

**When**: once · **Agent**: [Angle Scout](AGENTS.md#angle-scout) · **Prompt**: [One product, twelve launches](PROMPTS.md#twelve-launches)

Two launches a week sounds like a lot until you list what you already have. A launch needs a clear idea and a reason to post it today. Not necessarily a new product.

At unfair.so, every piece of content is treated as a launch. A normal post gets a few thousand views from whoever happens to scroll by. The same idea in launch format, with creators behind it, aims for 200,000 to 300,000 views.

1. Write down eight launches for the next four weeks. Pull from the twelve types below until you have more ideas than slots.
2. One angle per launch. Two ideas in one post compete with each other.
3. Put the strongest one in week one: its result is what you will show the next creators.

**Twelve things that make a launch**
1. A feature, even a small one, if it changes what people can do today
2. An integration or plugin for a tool your customers already use
3. A benchmark with numbers for your whole category, you included
4. Your take on the week's big release, with your product doing something on top of it
5. A customer story with a number in the first line
6. An open release: a repo, a dataset, a prompt pack
7. A free tool that does one small thing
8. A side-by-side: the old way and your way, on the same task
9. A walkthrough of one use case for a specific audience
10. A milestone, with proof
11. A contest with a prize
12. A manifesto: what you think about your category

**Twelve launches, one product.** An unfair.so client shipped twelve launches in five weeks (close to 2 million views in total). Same product every time, different angle: a new search feature, a tie-in to that week's model release, a plugin for an AI tool, a public benchmark, a how-to for one type of user.

**Pitfalls**
- Saving the launch for the big release. It gets one shot; eight small launches teach you what it should say.
- Replaying last week's hit word for word. At unfair.so, a side-by-side that got 456,000 views, redone identically, got 104,000.

<a id="step-04"></a>
## 04 · Book two slots a week and stick to them

**When**: once

A channel has a schedule. Same days, same time: your team, your creators and your followers learn when you ship something.

1. Pick two days with a day between them. Tuesday and Thursday is the classic.
2. Pick an hour when your audience is awake. To reach the US and Europe at once: 9 to 11 am Pacific, or late morning London time if your audience sits further east.
3. Put the next four weeks on the calendar now. The rule at unfair.so: the next two or three launches are always already booked.
4. Keep the slot quiet: no other post from the account in the six hours before and after.

**Twelve launches in five weeks, one team (unfair.so)**: from 24,000 to 478,000 views depending on the launch (views checked on November 12: 115,000, 205,000, 47,000, 61,000, 24,000, 32,000, 393,000, 150,000, 315,000, 133,000, 42,000, 478,000). Eight of the twelve went out in the same twenty-minute slot. That spread is the whole point: same team, same product, a 20x gap between the weakest and the strongest. You find the best one by also running the other eleven.

**What a steady rhythm looks like (unfair.so, late August to mid-November 2026)**: 99 launches for 36 teams; 16 teams came back for a second one; 7 went past four launches; the longest streak was 21 launches in 10 weeks; the fastest, 12 launches in 25 days.

**Why not one big launch.** A big launch is a single draw from a very wide range of outcomes. Small accounts feel this the most: a post shown to a few hundred followers in its first minutes lives or dies on who was online at that moment. Several launches warm up the account, reach different corners of your market and tell you which angle sells before you put real money behind it.

**Pitfalls**
- Launching when the post is ready instead of when the slot comes. The slot is what builds the habit.
- A date that keeps moving. One launch slipped five times because of content, then nearly went out at the wrong hour because of a mix-up between two time zones. Write the time zone every time.

<a id="step-05"></a>
## 05 · Set the budget per launch

**When**: once

Decide what a launch costs before the first one. After that, the weekly question becomes "which angle?" and never again "do we go?".

1. The creator budget is the money paid to the accounts that quote you. At unfair.so, no launch goes out under $4,000.
2. Aim for at least 30 creators. Below that, a post rarely gets out of its own followers' circle.
3. Keep the same budget for six launches, then shift money toward the angles that brought in signups.

**What a creator costs (unfair.so benchmark, 2026)**

| Profile | Price per quote |
|---|---|
| A quote on X, in general | from $20, $100 median |
| Creators with 2,000 to 5,000 followers | about $50 |
| Big accounts | $250 to $400, two or three per launch |
| People who already like your product | free: ask them first |

About a third of the creators they work with had never been paid to post before.

**Pitfalls**
- A $500 launch. They tried it: 13,000 people reached, one signup.
- The whole budget on two big names. Thirty small, well-targeted accounts in the same window do more than two big ones an hour apart.
- A different budget every launch: you can't compare angles if the spend moves with them.
- Don't have thirty creators on hand? Start building your network now (steps 13 to 15), beginning with your happy customers.

# Kickoff (T−48h to T−30h)

A launch is prepared in its last two days. These three steps lock what you are preparing.

<a id="step-06"></a>
## 06 · Set the date, the minute and the time zone

**When**: T−48h · **Agent**: [Launch Manager](AGENTS.md#launch-manager) · **Template**: [The 48-hour countdown](TEMPLATES.md#countdown-48h)

Everything else on the list hangs on one moment: the minute the post goes out (T0). Until it's written down with its time zone, nothing can be scheduled around it.

1. Write T0 with a date, a time and a time zone. "Tuesday morning" is not a time.
2. Name one launch owner. One person, even if five are helping.
3. Open one discussion thread for this launch and put everything in it.
4. Count down from T0 with the template.
5. No confirmed time at T−30h: that's your first blocker. Say it out loud.

**Which hour.** Launch when your audience on both sides of the Atlantic is awake. 9 am Pacific catches the US morning and the European evening. Late morning in London catches Europe at work and Asia in the evening, and America wakes up to a post that already has momentum.

**The post keeps moving for two days.** One launch tracked by unfair.so had 34,000 views and 56 quotes after 76 minutes, 1.3 million after 17 hours and 2.75 million after two days. Don't draw conclusions in the first hour.

**Pitfalls**
- A period instead of a date. You can't book "mid-October".
- Two owners.
- Confirming the time from memory after a call. The time is confirmed when the person who presses "Post" writes it back to you, to the minute.

<a id="step-07"></a>
## 07 · Write the one-page brief

**When**: T−30h · **Agent**: [Launch Manager](AGENTS.md#launch-manager) · **Template**: [The brief](TEMPLATES.md#the-brief) · **Prompt**: [From call notes to brief](PROMPTS.md#notes-to-brief)

One page that your team and your agents work from, and that the creator briefs get cut from later. If the goal, the number and the link aren't on it, everyone makes up their own.

1. Fill in the eleven lines of the template. None left empty: write "unknown", and it becomes a task with a name on it.
2. Reread your recent calls and threads before writing. A brief is mostly things already said.
3. Pin it at the top of the launch thread.

**What a good WIN PLAN line looks like**: "Outcome: 40 demos with data teams. Lever: a benchmark of the ten tools they already use, with their logos in the carousel. Target: 500,000 views, 5,000 visits, 40 demos." One sentence for what you want, one for why this launch can get it, one for how you'll know.

**Pitfalls**
- A brief that copies the product page.
- No NOT THIS TIME line: the second idea sneaks into the post.
- A metric nobody can count the next morning.

<a id="step-08"></a>
## 08 · Find the angle: the idea people will repeat

**When**: T−30h · **Prompt**: [Test an angle](PROMPTS.md#test-an-angle)

This is where most of the thinking goes. The angle is the sentence a stranger would use to tell a friend about your post. If you can't say it in one line, the post isn't ready.

1. Write the angle in one sentence, without the product name.
2. Try it on someone outside your company. If they say "so what?", keep looking.
3. Tie it to something happening this week when that's honest. Posts that ride a real event travel furthest.
4. Give the reader something to keep: a list, a number, a method. Useful posts get saved and shared more than announcements.

**Five angles that work again and again**
1. The news: the week's big release, and your product doing something with it the same day
2. The awkward number: a benchmark or a stat your category would rather not see
3. The demo that looks impossible: one take, no cuts, a real task
4. The useful object: a tool list, a template, a dataset people will save
5. The stance: something you believe that most of your category doesn't

**Two examples (anonymized)**
- Seven words, no product name: an AI company launched with a claim along the lines of "AI agents are the biggest users of the web". You want to argue with it before you even know who wrote it. 340,000 views, and the launch made it into X's trends.
- A simple claim with a number behind it: "here's the best tool for X", and the next line proves it: up to 2.8x more throughput. 2.3 million views, and a spot in X's trends.

**What a good 500,000-view launch looks like (unfair.so benchmark)**

| Signal | How to read it |
|---|---|
| Likes | 1,000 or more is excellent; under 500, the content didn't land |
| Bookmarks per like | above 0.7: people want to come back to it |

A poor likes-to-views ratio almost always points to the angle or the creators.

**Pitfalls**
- The feature list as an angle.
- Going viral with the wrong people. A founder turned down a celebrity stunt that was sure to work, because it would have pulled in curious people looking for freebies and no buyers. It was the right call.

# The post (T−30h to T−24h)

Nothing can be fixed once it's out. Everything is frozen a day before.

<a id="step-09"></a>
## 09 · Launch from the founder's account

**When**: T−30h

People reshare people. A founder saying "we built this" goes further than a logo, and the replies turn into conversations a company account can't have.

1. The main post goes out from the founder's account. The company account quotes it with its own take and handles replies.
2. Launching twice a week? Give a launch to the product account now and then. unfair.so's hunch: an account that carries every launch ends up eating its own reach.
3. Check before launch day that the account can carry the post: long text, long video, pinned slot free.
4. If someone else will reply on the founder's behalf, set up X's delegated access now, not at T0.

**Ten out of twelve.** An unfair.so client launched twelve times in five weeks: ten from the founder's account, two from the product's.

**A small, quiet or brand-new account.** None of that stops a launch. On its own, a quiet account reaches about a thousand people per post, a new one even fewer, and the post's fate depends on who sees it first. Creators fix exactly that: the first signals come from thirty relevant accounts instead of from chance. Warm up the account anyway: a week of daily replies in your niche and a few ordinary posts before the first launch.

**Pitfalls**
- The founder posts and walks into a meeting (see step 37).

<a id="step-10"></a>
## 10 · Make the first line and the first five seconds carry it

**When**: T−24h · **Template**: [The post skeleton](TEMPLATES.md#post-skeleton) · **Prompt**: [Ten first lines, three full posts](PROMPTS.md#ten-first-lines)

People decide in about a second. The first line of text and the start of the video have to earn the rest.

1. First line: the angle, alone. No hello, no "excited to announce".
2. A video uploaded natively to X, with the hook in the first five seconds. Cut everything before the first interesting frame.
3. Burn in the captions: on X, everything is watched with the sound off.
4. Second paragraph: what it is, and who it's for. Then the link (step 11).
5. Frozen means frozen. Once people quote a post, you can't rewrite it.

**Three video formats that work**
1. The founder demo: you, the screen, a real task
2. The animation: the idea in motion, nobody on camera
3. The scenario: the product reacting to the week's news

Whatever the format, the very first frame is already the interesting part.

**A second line that does a paragraph's job.** Anonymized example: "They run on our tool, so we see what they'll go looking for: licensed data, not published data." In one sentence: who they are, why they know, and what the news is.

**Pitfalls**
- "We're excited to announce".
- A logo animation before anything happens.
- A thread where one post would do. The first post has to stand alone: it's the one people quote.

<a id="step-11"></a>
## 11 · Put the link in the post, above "Show more"

**When**: T−24h

If readers have to expand the post or open the replies to find your link, most won't. What unfair.so tells every founder: a link in the first reply converts about ten times worse than a link in the post.

1. Keep the text short enough that the link shows without tapping "Show more".
2. Open the link on a phone, on mobile data. Does it open? Does the page load? The post itself gets checked logged out at T0 (step 31).
3. Add the UTM and the code from step 02.
4. Then drop the link again as the first reply, for those who scroll that far.

**"But links cut reach, right?"** That fear is what pushes people to hide the link in the replies. unfair.so's position: better a launch that reaches fewer people who can act than one that reaches more who can't do anything. They've seen a great wave of quotes wasted on a post whose link was hidden under "Show more".

**Pitfalls**
- The link only in the bio.
- The link on the video's end screen.
- A link to the homepage when the post is about one feature. Send people to what you showed.

<a id="step-12"></a>
## 12 · Get an honest read before you freeze

**When**: T−24h · **Agent**: [Post Critic](AGENTS.md#post-critic) · **Prompt**: [A harsh read of the draft](PROMPTS.md#harsh-read)

You can't fix a post once it's out. Take the hard feedback while it's still a draft, from someone with no reason to be nice.

1. Send the draft to one person who will tell you the truth. Ask what they would cut.
2. Run it past the critic (agent or prompt).
3. Fix the first line and the first five seconds first: that's where most of the notes land.
4. Freeze it at T−24h. Later tweaks are for the next launch.

**What X's ranking code rewards.** Weights read by unfair.so in the published code of X's algorithm (repo `xai-org/x-algorithm`), in September 2026:

| Signal | Weight |
|---|---|
| Someone copies the post's link | 20 |
| A reply, a quote, a share by DM | 5 each |
| A follow from the post | 4 |
| A like | 0.5 |
| One second of attention | 0.004 |

The code changes: check the repo before you lean on a number. What matters is the shape: a like is worth almost nothing, and anything that starts a conversation or carries the post somewhere else counts ten times more. Quotes reach people who don't follow the person quoting, while plain reposts mostly stay with their followers. Bookmarks help the reader, but didn't show up as a signal when unfair.so looked.

**Pitfalls**
- Asking the team: they've seen it ten times and can't read it fresh anymore.
- Polishing after T−24h. The angle and every creator draft are written against the frozen version.

# The creators (T−24h to T−12h)

Creators decide who sees the post first. Pick them by their audience, check them by hand, confirm in writing.

<a id="step-13"></a>
## 13 · Shortlist 30 to 60 creators by who follows them

**When**: T−24h · **Agent**: [Creator Scout](AGENTS.md#creator-scout) · **Prompt**: [A long list from a competitor's launch](PROMPTS.md#list-from-competitor)

A creator is worth what their followers are worth to you. Fifty thousand followers who will never buy do less for a launch than three thousand who might.

1. Start from people, not lists. Who do your best customers follow? Who quoted the last launch in your category?
2. Build the long list from three sources: quotes under your competitors' launches, replies under accounts your audience reads, and your own active followers.
3. Score each one: audience fit first, recent activity second, size last.
4. Keep at least 30 accounts, 40 to 60 if the budget allows. Line up a few backups: someone always drops out.
5. Mix sizes: two or three big accounts for reach, the rest small and focused.

**How to score a creator**

| Criterion | What you look at |
|---|---|
| Who follows them | jobs, companies and countries that look like your customer |
| Their last ten posts | steady replies and bookmarks for their size |
| What they talk about | your category, in their own words |
| Their last paid post | not this week: audiences tire fast |
| Their size | to break ties, never as a reason to pick |

**Small and fresh beats big and tired.** One of unfair.so's best launches used 70 creators for $8,000: almost all cheap, the most expensive at $800. Accounts at $500 and up rarely pay for themselves. Better to spot a small account making good content early and grow with it.

**One pool, a different mix each time.** For a developer platform, unfair.so screened about 500 creators against the target customer (founders, operators, people building in public, in the US) and kept about 300. Each launch used 40 to 60 of them, in a slightly different mix, to reach new people every time.

Done by hand, this step took them about seven hours per launch.

**Pitfalls**
- Sorting by follower count.
- Trusting a tool's pick without opening the profile. Every creator goes past a human's eyes.
- An audience in the wrong country or the wrong job. Check before you pay.

<a id="step-14"></a>
## 14 · Read each one's last ten posts

**When**: T−24h · **Agent**: [Creator Scout](AGENTS.md#creator-scout) · **Template**: [The two-minute check](TEMPLATES.md#two-minute-check)

A profile tells you who someone was. Their last ten posts tell you what will happen if they post tomorrow.

1. Open the profile and read ten posts, not counting the pinned one.
2. Look at replies before likes. Real replies from real accounts are the hardest thing to fake.
3. Compare views to follower count. A 50,000-follower account getting 400 views a post has an audience that left.
4. Find their last paid post and see how it did compared to usual.
5. Two minutes per account. Thirty creators is an hour, and that hour saves the launch.

**Size is not reach (unfair.so example).** A 158,000-follower account paid $300: 8,300 views on its quote. A founder with 26,000 followers paid $150: 61,700 views. Same product, three weeks apart. The second one's followers were the customers.

**Pitfalls**
- Reading the follower count and stopping there.
- Rebooking a creator who didn't deliver because they were nice about it. Write down why, and don't book them again.

<a id="step-15"></a>
## 15 · Rotate your creator team

**When**: T−24h · **Template**: [The creator log](TEMPLATES.md#creator-log)

The same thirty faces quoting you twice a week stops looking like news, both to their followers and to the feed. Rotate.

1. Keep the few who did best and swap the rest. A slightly different mix each launch reaches people the last one missed.
2. Track each creator: number of launches with you, last paid post anywhere, results of their quotes.
3. Before booking, check how many paid posts they've already put out this week. An account that only posts sponsored content has stopped working.
4. Bring in two or three new accounts every launch. Some will become your best.

**The hidden gems.** unfair.so's favorite accounts are small ones that make good content and have never been paid to post. They cost less, their followers trust them, and they grow. Find them early and they stay on your team for a year.

**Pitfalls**
- The same team every time because it's easier.
- No notes. In a month you won't remember who delivered.

<a id="step-16"></a>
## 16 · Set the price and the posting window

**When**: T−18h · **Template**: [The invite DM](TEMPLATES.md#invite-dm)

A creator who knows the price, the minute and what counts as done shows up. If they only know two of the three, maybe.

1. Ask for their price. Don't name yours first.
2. Agree in writing on three things: the amount; the window (first wave within five minutes of your ping, everyone within the hour); what counts as delivered (a quote in their own words, still up the next day).
3. Offer product access or credits on top. It brings prices down and makes the posts better.
4. Paid is paid: ask creators to disclose it the way X and their country's rules require.
5. Pay what was agreed, on time. Creators talk to each other.

**What moves the price**

| Factor | Effect |
|---|---|
| Account size | the least important |
| A video clip or original content in the quote | up |
| A regular spot on your team | down, per post |
| Product credits on top | down, and the posts are better |

**Pitfalls**
- Negotiating on launch day.
- No window in the deal. "Sometime today" is how a wave turns into a trickle.
- Paying before the post is live (step 25).

<a id="step-17"></a>
## 17 · Give each creator their own angle

**When**: T−18h · **Agent**: [Quote Drafter](AGENTS.md#quote-drafter) · **Template**: [The angle sheet](TEMPLATES.md#angle-sheet) · **Prompt**: [A quote in a creator's voice](PROMPTS.md#quote-in-their-voice)

Thirty people posting the same sentence reads like a script, and the feed treats copies as spam. Thirty people each saying what struck them reads like news.

1. Write two or three angles derived from the main one, each for a different audience.
2. Assign angles to creators based on what they usually talk about.
3. Draft a quote for each creator, in their own voice. It's a starting point: they can rewrite it or bring their own.
4. Aim for quotes that could travel without your post. A quote with its own clip or its own claim reaches people the original never would.

**Three angles on the same benchmark (made-up example, but that's the range to aim for)**
- The user: "ran our tool through this benchmark. 7th out of 10. the top three all do one thing we don't"
- The skeptic: "vendor benchmarks usually flatter the vendor. this one puts itself 4th, so i read it"
- The tinkerer: "the test harness is open. reran two rows in an hour"

**Pitfalls**
- One draft for everyone.
- Copy to post word for word. The posts come out stiff and creators don't want to come back.
- Same-day drafts. Creators need them before T−12h.

<a id="step-18"></a>
## 18 · Make the creators' visuals for them

**When**: T−18h · **Template**: [The creator folder](TEMPLATES.md#creator-folder)

A quote with its own clip or screenshot works far better than text alone, and most creators won't make one unless you hand it to them.

1. Cut your main video into three to five short clips, one moment each.
2. Give real product access to about ten creators so they can make their own. A code for one paid month is enough.
3. Put everything in a single folder: clips, screenshots, logo, angle sheet.
4. Text only is fine for creators who never post video. A well-turned sentence in their voice beats a clip that doesn't look like them.

**The mix on a 30-creator launch (unfair.so)**: 15 with clips cut from the founder's video, 10 with access to make their own, 5 with a strong text quote. The access was a $30 subscription given by code. Bonus: it turns a paid quote into someone who uses the product.

**Pitfalls**
- Access that doesn't work. On one launch, several creators couldn't log into the product on the day.
- A brief that points to last month's video.

<a id="step-19"></a>
## 19 · Send brief, draft and instructions, and get a yes from each

**When**: T−12h · **Template**: [The kit sent to each creator](TEMPLATES.md#creator-kit)

A creator who hasn't replied hasn't said yes. Count the yeses, not the messages sent.

1. Send each creator four things in one message: the angle, their draft, the visuals, the launch-day instructions.
2. The instructions are the five steps at the bottom of the kit. The "it's live" ping repeats them (step 32).
3. Wait for a yes. Nudge at T−6h, and bring in a backup for anyone still silent at T−3h.
4. Handle special requests now. A creator with an open question at T0 posts late.

**Why you never send a direct link.** At unfair.so, creators are asked to open the profile and find the pinned post themselves. Their reasoning: a visit that comes through the profile looks like what it is, someone who went looking. Thirty clicks on the same pasted link look like a group chat.

**What you ask for and what you need to get**

| Ask | Target |
|---|---|
| Share the post by DM | asked of everyone, you need 40 to 50% |
| A yes to the kit | from every creator before T−3h, or they get replaced |

**Pitfalls**
- Counting sent messages as confirmations.
- A kit so long nobody reaches the instructions.
- No draft. Without one, creators post late or post thin.

<a id="step-20"></a>
## 20 · Ask them to follow you before the launch

**When**: T−12h

A quote from someone who follows you reads like a fan talking. And your post lands in their feed the second it goes out.

1. Ask every creator to follow the launching account.
2. Follow them back.
3. Do it the day before, when nobody's in a rush. Launch morning is for the post.

unfair.so's take: replies between accounts that follow each other weigh more than replies from strangers. It costs nothing, and it's the first thing they do with every team that comes back for a second launch.

# Your own network (T−24h to T−6h)

Before the platform shows a post to strangers, it checks how the people who already follow you react. Most founders skip this part, and it is the only part that costs nothing.

<a id="step-21"></a>
## 21 · Score your followers and keep the 200 that matter

**When**: T−24h · **Agent**: [Network Scorer](AGENTS.md#network-scorer) · **Prompt**: [Score a follower list](PROMPTS.md#score-followers)

In unfair.so's reading of the current algorithm, how your own followers react comes before everything else. A few hundred well-chosen people who heard from you in advance count for more than a few thousand who stumble on the post by chance.

1. Pull the follower lists: yours, your co-founders', your team's and your investors'.
2. Score each person against your ideal buyer: their job, their company, the topics they post about.
3. Keep the best 200 and sort them into three groups:
   - people who know you: you ask them straight out;
   - people this launch would interest: you tell them why;
   - people with an audience: you give them early access.

**Example** (unfair.so benchmark, 2026): a founder with 33,000 followers picked the 200 closest to his topic and wrote to them. Result: more than five strong quotes, without spending a cent.

**Pitfalls**
- Writing to everyone. You burn your list and your account.
- Forgetting your investors' and team's followers. That is where the warmest people are.

<a id="step-22"></a>
## 22 · Give them a heads-up by hand

**When**: T−24h · **Templates**: [The day-before DM](TEMPLATES.md#day-before-dm), [The "it's live" DM](TEMPLATES.md#its-live-dm)

A short personal note the day before earns a reply and a quote. A mass send gets muted, and at this volume automation gets accounts restricted.

1. Start the day before, earlier if you can. Six hours ahead is the minimum.
2. Send by hand, in batches over an hour or two. No automated bulk sending.
3. Three lines: what is coming out, when, one single ask.
4. The minute the post is live, send the second note: it's live, it's the pinned post.

**One of the best network campaigns at unfair.so** (2026 benchmark)

| Send | Volume |
|---|---|
| DMs to accounts with an audience | 20 to 30 |
| Messages to on-topic followers, eight hours before | 300 |

**Tone**: write as you would to a friend who works in your field. Lowercase reads fine. One ask only. A bit of honesty about nerves helps: "launching today, a bit nervous, would love your take" gets more replies than a polished pitch.

**Pitfalls**
- Pasting a big paragraph with a link.
- Asking for a repost. Ask for their opinion: replies and quotes do more, and people would rather be asked what they think.
- Automating. A restricted account costs you more than all the messages you thought you were saving.

<a id="step-23"></a>
## 23 · Brief the team: one quote ready, one hour blocked

**When**: T−18h · **Template**: [The team note](TEMPLATES.md#team-note)

Your own people are the fastest quotes you will get, and the most believable replies. They need what the creators get: a time, an angle, a draft.

1. Every team member with an X account writes their quote today, in their own words, about their part of the work.
2. Everyone blocks the first hour after T0.
3. Split the replies: who takes technical questions, who takes pricing, who says thanks.
4. Ask investors and advisors for a quote too, and send them a draft: they don't have time.
5. Line up one named quote: someone your field already listens to. It has to be their real opinion, never a courtesy.

**Pitfalls**
- Team members who only repost. A repost reaches their followers; a quote with an opinion reaches strangers.
- Five identical "so proud of the team" posts.

<a id="step-24"></a>
## 24 · Prepare the newsletter and your other channels

**When**: T−18h · **Template**: [The launch email](TEMPLATES.md#launch-email)

Your email list is the only audience you can reach whenever you want. Sent at T0, it brings your warmest people to the post in its first minutes.

1. Write the email now and leave the link blank. Send it by hand as soon as the post is live: before that, the post has no address.
2. One link only: the post. The product link is already in it.
3. Same for LinkedIn, Discord, Telegram and the Slack groups you belong to: a short note, at the same minute.
4. Four lists if you have them: waitlist, people who booked a demo, customers, sign-ups.

**The second email**: a week later, send the result as a short case study: what you launched, what happened, one number. People who ignored the launch read the result.

**Pitfalls**
- Linking the product page instead of the post. You want the first-minutes engagement on X, and the post already carries the product link.
- Sending an hour late.

# Lock-in (T−12h)

Twelve hours out, everything that can be decided is decided. After that, you say go, or you say no.

<a id="step-25"></a>
## 25 · Set the creator money aside, pay only for published posts

**When**: T−12h · **Template**: [The payout sheet](TEMPLATES.md#payout-sheet)

Creators post on time when the money is already set aside. And you stay protected by only releasing it once the post is live.

1. Add up the agreed prices and compare with the budget you set in [step 5](STEPS.md#step-05).
2. Set the total aside before T−12h: an escrow, a separate balance, or at the very least a sheet everyone can see.
3. Release each payment when the creator's quote is published in the agreed window and still up one day later ([step 38](STEPS.md#step-38)).
4. No post, no payment. The money goes back into your budget.

Without a dedicated tool, a shared sheet with four columns is enough: agreed, posted, checked, paid.

**Pitfalls**
- Paying upfront.
- Paying late. A creator who waited three weeks won't answer next time.
- Money that lands after T−12h. At unfair.so, that is one of the usual reasons for a NO-GO.

<a id="step-26"></a>
## 26 · Plan where you will reply

**When**: T−12h · **Agent**: [Reply Scout](AGENTS.md#reply-scout) · **Template**: [A reply that works](TEMPLATES.md#good-reply)

Your post is just one place. The conversation about your topic is happening today in fifty others. A good reply under a post that is taking off puts you in front of all its readers for free.

1. List the keywords your audience argues about.
2. Find 30 to 50 active posts on those topics, no more than two days old: big accounts in your niche, threads about the problem you solve, posts about the news your launch ties into.
3. For each one, write a reply that adds something on its own. The link to your launch comes second, or not at all.
4. Decide who replies from which account: the founder, the team, the product account.
5. The floor at unfair.so: 40 replies per launch.

**Visuals made for each thread**: for one launch, unfair.so prepared 20 to 30 small images, each one designed for the conversation it was going to be posted in. A reply with an image made for the thread gets read; a reply with a logo gets scrolled past.

Stay out of threads where it would be out of place: funding announcements, someone's bad news, anywhere you would be the stranger selling at a funeral.

**Pitfalls**
- "Great post! We just launched X." That is spam, and it shows.
- Replying from throwaway accounts made for the occasion.
- Sending every reply at once. Spread them over the day.

<a id="step-27"></a>
## 27 · Rehearse the first ten minutes

**When**: T−12h · **Template**: [The first-ten-minutes run sheet](TEMPLATES.md#run-sheet)

Ten minutes is too short to improvise. Walk through them once on paper, with names, and prepare every message before launch day.

1. Write the run sheet: one line per minute, one name per line.
2. Draft every message you will send at T0 and keep it where you can paste it: the creator ping, the "it's live" to the team, the network message, the email.
3. Open the landing page on a phone, on mobile data. Test the link, the sign-up and the code.
4. Name who watches the counter and who chases missing creators. Neither of them should be the person replying.

**Pitfalls**
- One person doing everything. Posting, counting and replying are three jobs.
- Writing the creator ping at T0. It takes a minute you don't have.

<a id="step-28"></a>
## 28 · Write down the numbers you expect

**When**: T−12h · **Template**: [The goals note](TEMPLATES.md#goals-note)

Without a forecast written beforehand, any result looks fine afterwards. The gap between what you expected and what happened is what makes the next launch better.

1. Two numbers written before the launch, where the team can see them: expected views and the metric from [step 1](STEPS.md#step-01).
2. Add the checkpoints: quotes at T+10m and T+1h, views at T+24h.
3. Afterwards, put the real numbers next to them ([step 40](STEPS.md#step-40)).

**Checkpoints at unfair.so** (2026 benchmark)

| Moment | Target |
|---|---|
| First wave | about 20 quotes in 5 to 10 minutes |
| T+15m | most creators have quoted |
| T+1h | everyone has quoted, and every quote is checked |

**Pitfalls**
- Goals written after the result.
- A goal in views only (see [step 1](STEPS.md#step-01)).

<a id="step-29"></a>
## 29 · Call GO or NO-GO

**When**: T−12h · **Agent**: [Launch Manager](AGENTS.md#launch-manager) · **Template**: [The eight GO / NO-GO gates](TEMPLATES.md#eight-gates)

A launch that isn't ready costs as much as one that is, and returns a fraction. At twelve hours, someone must have the right to say no.

1. Go through the eight gates one by one. Each gate is yes or no.
2. All yes: GO. Announce it where the whole team sees it.
3. A single no: name the blocker, its owner and the time it has to be cleared by. If it doesn't clear, move to the next slot.

That is what two slots a week buy you: a NO-GO costs three days, while launching unready burns the angle.

**What a skipped gate looks like** (unfair.so example): one launch had slipped because of content and went out anyway. Three hours before, creators weren't confirmed, the brief pointed to an old video and some creators couldn't log in to the product. It still got 690,000 views, and the team rated it one star out of five.

**Pitfalls**
- Nobody with the authority to say no.
- A "GO with five risks". That is a NO-GO with better manners.

# Launch day (T−3h to T+2h)

Two hours decide almost everything. Everyone knows their minute.

<a id="step-30"></a>
## 30 · Count confirmations and go quiet

**When**: T−3h · **Templates**: [The T−3h reminder](TEMPLATES.md#reminder-t-3h), [The T−15m line](TEMPLATES.md#line-t-15m)

At three hours, you can still replace a creator. At T0, you can't.

1. Show the count where the team can see it: confirmed, pending, dropped out.
2. Replace everyone who hasn't answered. Your shortlist had backups for exactly this.
3. Send the reminder to everyone with a role today: the time, the brief one more time, and that you will ping them the moment it's live.
4. No other post from the launching account until six hours after. Replies are fine.
5. T−1h: the founder is online, the creators are in the group chat, the team is at their posts.
6. T−15m: one last note to everyone.

**Pitfalls**
- Finding out at T+10m that six creators are asleep.
- A post scheduled the week before that goes out an hour before the launch.

<a id="step-31"></a>
## 31 · Post by hand, pin it, check the post is alive

**When**: T0 · **Template**: [The T0 check](TEMPLATES.md#t0-check)

The first minute is the only one fully in your hands. Post it yourself, look at it with your own eyes, and only then bring everyone in.

1. Post by hand. No scheduling tool: you want to see it go out.
2. Pin it.
3. Add the first reply with the link ([step 11](STEPS.md#step-11)).
4. Open the post in a logged-out window. Text, video, link: is it all there? Does the video play?
5. If something is off, delete and repost before the first quote. After the first quote, you are committed.
6. Paste the post's URL in the team chat and announce it's out.

**When X breaks the post**: it happens. On one unfair.so launch, about 15 quotes in 15 minutes, 30 to 40 in total, and the post stalled at 11,000 views: it had broken on X's side. Since then they check the post is alive before pinging a single creator, and a dead post gets reposted.

**Pitfalls**
- Scheduling the post and hoping for the best.
- Pinging creators before you've looked at the post.
- Editing the post once it already has quotes.

<a id="step-32"></a>
## 32 · Tell creators it's live, without a link

**When**: T0 · **Template**: [The "it's live" ping to creators](TEMPLATES.md#live-ping)

One message, at the same second for everyone, telling them where to go.

1. Post it in the creator group chat, and by DM to anyone not in it.
2. Use the template. No direct link (see [step 19](STEPS.md#step-19)).
3. Watch who reacts. Anyone silent after three minutes gets a personal message.

**Pitfalls**
- Putting a link in the ping.
- Pinging in waves without meaning to, because you message people one by one. Use a single group chat.

<a id="step-33"></a>
## 33 · Land the first wave in five minutes

**When**: T+5m · **Agent**: [Wave Watcher](AGENTS.md#wave-watcher)

The feed makes up its mind early. Twenty posts in the same window look like news. Twenty posts spread over a week look like nothing.

1. At T+5m: your own quotes are up (the team, the named quote planned in [step 23](STEPS.md#step-23)) along with the first five creators.
2. At T+10m: about twenty quotes.
3. Count them. Open the post's quotes and check them against your creator list.
4. A little spread is good. Arrivals over fifteen to twenty minutes look healthier than thirty posts in the same second.

**The wave, minute by minute** (unfair.so benchmark)

| Moment | What should be live |
|---|---|
| T+5m | your team and the first 5 creators |
| T+10m | about 20 quotes |
| T+15m | most creators |
| T+30m | second nudge to the missing ones |
| T+60m | everyone, every quote checked |

**Why five minutes**: the window is an unfair.so rule, not a platform one, but it is the whole trick. A post that gathers its first real engagement over an afternoon is judged as a normal post. A post that twenty relevant accounts talk about within minutes is judged as an event. That is how launches from the big AI labs travel: their whole circle quotes at once.

**Pitfalls**
- Relying on creators to remember. Someone has to watch the counter.
- Thirty identical posts in sixty seconds (see [step 17](STEPS.md#step-17)).

<a id="step-34"></a>
## 34 · Half the creators by 15 minutes, everyone within the hour

**When**: T+15m · **Agent**: [Wave Watcher](AGENTS.md#wave-watcher) · **Template**: [The nudge to a late creator](TEMPLATES.md#nudge)

The wave has a tail. Creators who post in the first hour keep pushing the post while the feed is still deciding how far to take it.

1. T+15m: half or more have quoted. Message the rest, by name.
2. T+30m: anyone still missing gets a second nudge and a question: is something blocking you?
3. T+1h: everyone has posted. Open every quote: right angle, right link or code, your name spelled correctly.
4. Log each quote's URL and time next to the creator ([step 25](STEPS.md#step-25)).
5. Ask the creators who have posted to boost each other's quotes.

**How long paid quotes take** (unfair.so measurements, three launches in September 2026)

| | Launch 1 | Launch 2 | Launch 3 |
|---|---|---|---|
| Median delay after T0 | 6.5 min | 7.4 min | 7.7 min |
| Quotes delivered | 12 of 12 | 12 of 12 | 10 of 10 |

**Quotes of quotes**: when a creator's quote does well, another creator can quote that quote, with the original still visible inside. Over two or three levels, each level reaches a new audience and sends attention back to your post.

**Pitfalls**
- Not opening the quotes. A wrong link in a quote that takes off means a launch for someone else's URL.
- Letting a delay slide without logging it. Delays happen. Log it anyway ([step 15](STEPS.md#step-15)).

<a id="step-35"></a>
## 35 · Work the replies, yours and theirs

**When**: T+30m · **Template**: [Three kinds of replies](TEMPLATES.md#three-replies)

Replies are where a launch turns into conversations, and conversations are what the feed carries furthest.

1. Answer every reply under your post. A real answer, not a thank-you emoji.
2. Reply under the creators' quotes too: that is where their followers discover you.
3. Start the reply plan from [step 26](STEPS.md#step-26): the first ten replies in other threads go out now, the rest through the day.
4. Ask a question back whenever you can. A reply that gets a reply counts double.

**A Q&A at T+35m**: a habit unfair.so picked up from another team. Between 35 and 45 minutes after launch, the founder posts a short reply under the post inviting questions, and answers them over the next hour. It sparks a second wave of replies just as the first one fades.

**Pitfalls**
- Liking replies without answering them.
- Six replies to a troll. Reply once, then let it go.
- Pasting the same reply to twenty people.

<a id="step-36"></a>
## 36 · Give the launch a second beat

**When**: T+1h · **Template**: [Three second beats](TEMPLATES.md#second-beat)

After an hour, the first wave has been seen. A second post about the same launch reaches those who missed it and gives everyone else a reason to come back.

1. Quote your own launch post with something new: a first number, a behind-the-scenes clip, the best reply you got.
2. Ask two or three creators whose quote did well to add a follow-up under theirs.
3. The next morning, post the same video on LinkedIn. unfair.so's working assumption: a video that won on X does about as well there.
4. Only one more post that day. The quiet rule from [step 4](STEPS.md#step-04) still holds for everything else.

**Raising a cap**: if you launched with a limited code ([step 2](STEPS.md#step-02)), raising the cap is a second beat on its own: "the 200 went in two hours, we're opening 500".

**Pitfalls**
- Reposting the launch post itself. A quote with something new travels; a repost of your own post doesn't.
- Three follow-ups in the same afternoon.

<a id="step-37"></a>
## 37 · Stay online for two hours

**When**: T+2h · **Template**: [The DM to someone who engaged](TEMPLATES.md#engager-dm)

The founder being there is the difference between a post and a launch. The people replying are the warmest contacts of your week, and they are here right now.

1. Block two hours. No calls.
2. Answer everything, under your post and under the quotes.
3. Follow back everyone who engages and looks like your ideal buyer.
4. Move the warmest ones to DMs while they are still watching: a thank-you, a question, the link.
5. Keep the post pinned for at least 24 hours.

**What a launch should leave behind** (unfair.so benchmarks for a 500,000-view launch)

| | |
|---|---|
| New followers | 300 to 800 |
| Of whom exactly your ideal buyer | 10 to 20 |
| People who replied, quoted or reposted | a few hundred, each with a name |

**If you can't be there**: give someone you trust delegated access to the account for the day, with how you would answer the ten most likely questions, and the list of replies that should wait for you. It is a second-best option, but it beats silence.

**Pitfalls**
- Posting, then leaving for a call.
- Only answering the nice replies.
- Unpinning that same evening.

# Wrap up and go again (T+1d to T+3d)

A launch is only over once the next one is booked.

<a id="step-38"></a>
## 38 · Check every creator post is still up

**When**: T+1d · **Template**: [The thank-you to creators](TEMPLATES.md#thank-you)

You are paying for posts that stay. A day later, some have been deleted, and a few went out with the wrong link.

1. Open every quote URL logged in the sheet.
2. Still up? Right angle? Right link or code?
3. Pay the ones that pass. For the others, ask before you decide.
4. One line per creator in the [creator log](TEMPLATES.md#creator-log): how the quote did, rebook or not.
5. Thank them and share the result. People post better for a launch they feel part of.

**Pitfalls**
- Paying everyone the same evening without looking.
- Never telling creators how it went.

<a id="step-39"></a>
## 39 · Turn the people who engaged into a lead list

**When**: T+2d · **Agent**: [Lead Lister](AGENTS.md#lead-lister) · **Template**: [The note to a lead](TEMPLATES.md#lead-note) · **Prompt**: [Score the people who engaged](PROMPTS.md#score-engagers)

Everyone who liked, replied or quoted raised their hand. On most launches that is a few hundred names, and nobody writes them down.

1. Pull everyone who replied, quoted or reposted. Then everyone who liked.
2. For each one: name, job, company, X handle. Then LinkedIn and email when you can find them.
3. Score them against your ideal buyer and sort.
4. The top of the list gets a personal note this week. The rest goes into your CRM as "people who saw you".
5. New followers who look like your buyer get the same treatment.

**What one launch produced** (unfair.so example, early November 2026)

| | People | Found on LinkedIn | With an email |
|---|---|---|---|
| Replied, quoted or reposted | 438 | 176 | 127 |
| Liked | 1,600 | 349 | 167 |

At unfair.so, about 40% of active people (replies, quotes, reposts) are found on LinkedIn.

**Pitfalls**
- Looking at the view count and closing the tab.
- Sending an automated sequence to the whole list. These people just discovered you: write to the first twenty yourself.

<a id="step-40"></a>
## 40 · Run the numbers and book the next slot

**When**: T+3d · **Agent**: [Retro Analyst](AGENTS.md#retro-analyst) · **Template**: [The one-page retro](TEMPLATES.md#one-page-retro)

Every launch should teach you something that makes the next one better. That only happens if you write it down while it's fresh, and if there is a next one on the calendar.

1. Fill in the row of the [launch log](TEMPLATES.md#launch-log) you opened in [step 2](STEPS.md#step-02): views, visits, sign-ups, paying customers, revenue, spend.
2. Put them next to the goals note from [step 28](STEPS.md#step-28). Where were you wrong?
3. Three lines: what worked, what didn't, what you change.
4. Pick the next angle from the backlog with what you just learned.
5. Confirm the next slot. It should already be on the calendar.

**Do the math once**: what this launch cost you in money and in hours. That is the number to keep in mind when deciding how you run the next one.

**Pitfalls**
- No retro because the launch went well.
- Treating views as the verdict. At unfair.so, a 690,000-view launch was rated one star out of five, and a 470,000-view one got five stars.
- No next date. That is how a channel turns back into a one-off event.
