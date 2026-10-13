# UX agent

A reviewer for user experience, not for interfaces. It takes whatever represents a
journey (Figma screens, a clickable prototype, a live HTML page, a flow diagram, a
plan, a paragraph describing what someone will do) and answers two questions in
order: is this the right problem to be solving, and does this solution actually
work for the person doing it.

It is built around one idea. Every one of those artefacts is a different surface
over the same thing, a person trying to get something done, so the agent converts
all of them into one shared model of that journey and does its thinking against
the model. A Figma prototype and three sentences of intent get the same treatment,
which is what stops the review quality following the fidelity of the artefact.
Half of the value here is being able to review a plan before anyone has drawn
anything.

It does not review aesthetics. Colour, type, spacing and whether something looks
current are someone else's job, and mostly they are the design system's job. This
one cares about effort, memory, confidence and wrong guesses.

`PLAN.md` is the foundations: the model, how it judges, how it learns, the skills
it needs and the order to build them in. `contracts/` holds the three formats every
review follows. Built so far: `ux-review`, `ux-learn`, `ux-add-reference`, the starter `knowledge/` with its
`INDEX.md`, the eval cases in `04-evals/`, and unattended runs.

## Where the owner's work lives

This folder holds the agent and nothing about the person using it. Clients, the
review queue, reviews, evals and private knowledge sit in a work folder the owner
picks on first run, named by `work_dir` in `config.json` (gitignored;
`config.example.json` shows the shape). Inside it, numbered:

```
01-clients/    one folder per client: company.md, private.md, products/
02-queue/      one folder per client of queued items, and stream.json
03-reviews/    one folder per review: journey.md, review.md, evidence/
04-evals/      cases a good review is checked against
05-knowledge/  the owner's own sources, principles and disputes
```

`python3 setup.py` asks nothing: `--status` shows both folders, `--default` suggests
a work folder, `--work-dir <folder>` writes the config and creates the five
folders, with an empty `05-knowledge/` ready for the owner's own knowledge. The `ux-review` skill runs it on first use. Skills find this folder by
resolving their own link in `~/.claude/skills/`; the agent definition does the
same from `~/.claude/agents/ux-agent.md`.

## Two layers of knowledge

The agent ships with a small starter set in `knowledge/`: free, open sources such as Nielsen's
heuristics, WCAG 2.2, Laws of UX and the GOV.UK Service Standard, each summarised with short
quotes and a link. `knowledge/sources.md` lists them. Anything personal or paywalled, and every
lesson from the owner's own reviews, lives in the work folder's `05-knowledge/` instead, with
its own `sources.md` and `INDEX.md`. A review reads both. On first run the agent lists the
starter set and asks whether the owner wants to add sources of their own.

## Running unattended

Reviews can be queued and run overnight on the shared runner in
`PACKAGES/agents-engine` (`RUNNER.md` there). Put an item in `02-queue/<client>/` of
the work folder (`contracts/queue.md` has the format), switch the client on and pick its hours in
the agents dashboard, and the review is waiting in `03-reviews/` in the morning with
its open questions at the top.

What happened each day is in `state/<client>/runs/<date>.md`: what ran, what did
not and why, and what failed with what fixes it.

This folder holds only its own part: `hooks.py` (which items can run, what Claude
is asked and may touch, where the review lands), `run.py`, `agent.json`,
`workdir.py`, `templates/stream.json` (the queue's manifest, filled in for this
machine and written into `02-queue/`), and `bin/capture.sh`, the one shell
command an unattended review may run. It can write only under `03-reviews/` and
this folder's `knowledge/`.

```
python3 run.py --dry-run                        what would run now, no spend
python3 run.py --now --target <client>          a pass by hand, now
python3 run.py --now --item plans-mobile.md     one item by hand
```
