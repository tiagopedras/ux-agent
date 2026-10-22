---
name: ux-review
description: Review the user experience of a journey, from whatever represents it — a live page or local app, screenshots, a Figma frame, a flow, a plan, or a paragraph describing what someone will do. Establishes who it is for, what they are trying to get done and what the review should judge against, asks about the decisions behind the work, then writes a verdict and findings that each name what happens to the person. Use whenever he asks for a UX review, a UX critique, "is this the right problem", "does this flow work", "review this journey", "what's wrong with this experience", "look at this as a UX designer", or shares a design, prototype, page or plan and asks what a user would struggle with. Do not use it for visual polish, colour, type or spacing, for design system conformance, or to add a web source to the knowledge base, which is ux-add-reference.
---

# UX review

A review as a UX designer would give it: judgement first, backing second, and questions
before verdicts.

Two folders matter. The **agent folder** holds the agent: `AGENT=$(dirname "$(dirname "$(realpath ~/.claude/skills/ux-review)")")`. The **work folder** holds the owner's clients, queue, reviews, evals and private knowledge: `python3 "$AGENT/setup.py" --status` prints it as `work_dir`.

Paths below that start with `contracts/`, `knowledge/` or `PLAN.md` are in the agent folder.
`clients/`, `reviews/` and `evals/` are the work folder's `01-clients/`, `03-reviews/` and
`04-evals/`.

Knowledge comes in two layers, and a review reads both. `knowledge/` in the agent folder is
the starter set the agent ships with: free, open sources. `05-knowledge/` in the work folder
is the owner's own: the sources they added, their principles and their disputes.

The three files in `contracts/` are the authority on format. Read all three before starting,
and follow them rather than anything remembered from a past review:

- `contracts/angle.md` — what must be known before reviewing, and the decisions questions.
- `contracts/journey-model.md` — the template for `journey.md`.
- `contracts/review-format.md` — the template for `review.md`, and what is checked before it
  is shown.

`PLAN.md` holds the reasoning behind them. Read it once if anything below is unclear.

## 0. First run

**Work folder.** If `python3 "$AGENT/setup.py" --status` says `configured: false`, set it up
before anything else:

1. Ask which folder to use as the work folder. Suggest the `default_work_dir` from the status
   output, which sits outside the agent folder.
2. Run `python3 "$AGENT/setup.py" --work-dir <folder>`. It writes `config.json`, creates
   `01-clients`, `02-queue`, `03-reviews`, `04-evals` and `05-knowledge`, and fills
   `05-knowledge` with an empty `principles.md`, `disputes/`, `effects/`, `patterns/`, and a
   `sources.md` and `INDEX.md` with only their headers. Anything already there is kept.
3. Say in one line where the folder is.

<!-- STARTER-KNOWLEDGE -->
**Starter knowledge.** Straight after setup, read `knowledge/sources.md` and list the starter
sources it holds, one line each: the name and what it gives. Then ask whether they want to
add sources of their own, such as a newsletter, a glossary or their company's guidelines.
For each URL they give, run the `ux-add-reference` steps, which write into `05-knowledge/`.
If they have none, carry on.

**Welcome.** If `$AGENT/.welcomed` does not exist, open with the block
below, as written, before asking anything. Then create the file (empty) and carry on with
step 1 in the same message. Show the block again whenever he asks how the review works.

> **UX review**
>
> I review the experience of a journey, from a live page, screenshots, a Figma frame or a
> plan, and tell you what happens to the person using it. Pick a way to use me, or just share
> the work and I'll do the full review:
>
> - **Quick check.** One screen, a short list of what a person would trip on.
> - **Plan review.** A plan or brief, before anything is drawn.
> - **Accessibility only.** Just that angle, nothing else judged.
> - **Alternatives without a verdict.** Two or three other shapes for the same job, with
>   what each costs.
> - **Second pass with client context.** I reuse the saved company and product context, and
>   ask before I apply it.
> - **Log agreed findings.** Once we've talked it through, I add the ones you agree with to
>   the repo's backlog.
>
> What to expect:
>
> - I ask who it's for, what they're trying to get done and what to judge against, then ask
>   why about the decisions that look deliberate, before I judge any of them.
> - Each finding names what happens to the person, backed by your evidence, a named source,
>   or marked as my judgement. The verdict is a suggestion, and every finding is listed so
>   you can disagree.
> - I keep client and product context, sources and lessons between reviews. Corrections
>   become rules I follow next time. Where we disagree, I record both views.
> - I never edit the work, and nothing goes to Figma or anywhere else without your yes.

## 1. The angle

Get the actor, the job and the angle, as `contracts/angle.md` defines them. Ask for whichever
are missing in one message, as questions. Never infer them from the artefact.

If the artefact is large and the angle broad, ask which part carries the worry.

**Client context.** List the folders in `01-clients/`. If any exist, ask which client applies,
then which product in its `products/` folder, offering both as options. Apply only what he
names or confirms. Read the client's `company.md` and `private.md`, then the product's
`product.md`, `users.md`, `personas.md` and `platforms.md` where they exist. Name the persona
the review judges against, or check the work for all of them. Never quote `private.md`. If
no client applies, go on without one. Record the files applied under `applied_context` in
the journey model.

## 2. Capture

Get the artefact onto disk as evidence in `03-reviews/<today>-<slug>/evidence/` of the work folder. Read-only,
always: nothing here clicks a save button or posts anything.

| Artefact | How |
| --- | --- |
| Pasted text or a plan | Save it as `evidence/brief.md`. |
| Screenshots he shares | Copy them into `evidence/`. |
| A live page or local app | The built-in browser pane if it is available. Otherwise headless Chrome, one view per call, each run killed after 20 seconds because pages that poll never finish: `"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu --user-data-dir=<temp dir> --hide-scrollbars --window-size=1600,1100 --virtual-time-budget=5000 --screenshot=<file> <url>`. A hash-routed app takes a view per `#hash`. Read the code and docs behind a view when the screenshot cannot show a state. |
| A Figma file | The Figma Console MCP, with the desktop app open on the file and the bridge paired. Screenshots of the frames in scope, plus the prototype connections if there are any. |

Write down what could not be read: a state the capture did not reach, a view behind a login,
a frame that would not export. Each one becomes an Unknown.

## 3. The journey model

Fill `journey.md` from the template in `contracts/journey-model.md`. Steps are named from the
actor's side, not the screen's. Run the four walkthrough questions at every step. Leave a field
empty rather than guess, and add the gap to Unknowns.

## 4. Ask why

Walk the model and list the choices that look deliberate. Ask about the ones that would change
the verdict, and only those: a handful, numbered, in one message. Say briefly what you
observed in each, so he can answer without opening the artefact.

Record his answers in the model's "Decisions asked about" table, in his words, shortened.
Do not write findings until he has answered.

## 5. Judge

Work through the three passes in `PLAN.md` ("How it judges"):

1. **The problem.** Is this the right problem for this actor and job? If not, that is the
   review: one finding, and alternatives.
2. **The solution.** Walk the steps and count the cost to the actor: memory, decisions
   made without information, wrong guesses that cost work, effort before value, and states
   they are certain to hit that the work leaves out.
3. **Alternatives**, only when pass one fails or a cost is part of the structure rather than
   fixable. Two or three shapes, each with cost and what it gives up, set against how the
   problem is solved elsewhere.

Reason as the actor first. Look for backing after the finding exists:

1. Evidence he gave.
2. `knowledge/INDEX.md`, then `05-knowledge/INDEX.md` in the work folder, then only the
   files that apply from either.
3. When neither holds anything that fits, search the web. Prefer research, established
   guidelines and how well-known products solve it. Cite what you find, and add each source
   worth keeping through the `ux-add-reference` steps, which write it into `05-knowledge/`
   with its line in that folder's `INDEX.md`. List them under "Sources added".
4. If nothing credible turns up, write "Judgement" as the backing. The finding stays.

Before judging, read `05-knowledge/principles.md` and every open file in
`05-knowledge/disputes/`, both in the work folder. Follow the principles. Where a finding
touches an open dispute, say so in the finding and link the dispute, rather than repeating
the claim as settled.

Before the verdict, read the most recent review in `03-reviews/` of the same product, if there
is one, and say where this one disagrees with it.

## 6. Write and check

Write `review.md` from the template in `contracts/review-format.md`. Links to the owner's
`05-knowledge/` are relative from the review folder (`../../05-knowledge/...`). Links to the
starter `knowledge/` are absolute paths into the agent folder, since it sits outside the work
folder.

Run the checks listed in `contracts/review-format.md`, plus these:

- Every link to `knowledge/` or `05-knowledge/` resolves.
- Every Unknown is dealt with: a finding, an open question, or accepted.

Fix anything that fails before showing the review.

## 7. Report

In chat: a link to `review.md` (absolute path), the verdict, one line per finding, sources
added, and any open questions. Nothing else.

## After the review

- **Findings and suggestions he agreed with:** list them and ask whether to log them in the
  reviewed repo's `IMPROVEMENTS.md`, one entry each. The question names the repo, and says
  plainly when it has no `IMPROVEMENTS.md` yet, so a yes also means creating one. On a yes,
  use `improve-idea`, one entry per item, pointing back at `review.md`, then note in
  `review.md` which findings were logged and where. Write nothing without the yes.
- **He disagrees:** hold the point where the backing stands up, fold when he makes the
  stronger case. If he says to drop it, or stays unconvinced, record it with `ux-learn` as a
  dispute.
- **He corrects how the agent works:** record it with `ux-learn` as a principle, once he
  agrees it should always apply.
- **Figma comments:** propose each one in chat and post only the ones he approves, one by one.

## Unattended

When run off the queue, there is nobody to ask. Refuse an item without actor, job and angle.
Skip step 4's questions and put them under "Open questions" at the top of the review, mark the
verdict provisional, and post nothing to Figma. Log nothing to any backlog: list the findings
that would be candidates under "Open questions" too. Add no sources to either knowledge layer:
list any worth keeping under "Sources added" as links, for the owner to add with
`ux-add-reference`.
