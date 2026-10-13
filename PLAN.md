# Foundations

## The shape

Four stages, always in this order, and each one is allowed to fail loudly rather
than guess.

1. **Capture** pulls the artefact off its surface onto disk. Figma frames and
   prototype links, a live page's screens and DOM, a diagram's nodes and arrows, a
   pasted plan. Output is evidence: images, structure, and a note of what could
   not be read.
2. **Model** turns that evidence into the journey model below. This is the only
   place the artefact type matters. After it, nothing downstream knows whether the
   input was a prototype or a paragraph.
3. **Assess** runs the passes against the model.
4. **Report** writes the review in a fixed format.

## No review starts without an angle

A review needs three things before it begins, and it asks for any that are
missing rather than inventing them.

- **The actor.** Who this is for.
- **The job.** What they are trying to get done, stated without reference to the
  interface.
- **The angle.** The user need, job to be done or user story the review is being
  asked to judge against.

The angle is the one that matters most and the one most likely to be missing. A
forty-screen Figma file with no angle produces forty screens of undifferentiated
notes. With an angle it produces a walk of the four screens that carry the job
and a verdict on whether they carry it.

Where the file is large and the angle is broad, it asks a second question: which
part are you worried about? Asking is the default. Reviewing everything is what
it does only when told to.

## It never assumes which context applies

The knowledge base grows over time: the company, the users, the personas, the
products, the devices, the breakpoints. None of it is applied to a review until
you have said so or confirmed it.

So it asks rather than infers. "Is this the Parents app, and is the persona the
one we called the returning parent?" It may offer what it holds as options,
because picking from a list is quicker than typing. It may not read a screenshot,
decide this looks like the teacher journey on mobile, and review against that.

What it has been told goes into the journey model as applied context, so any
review can be checked against what it was working from. A review that silently
applied the wrong persona is worse than one that asked an obvious question.

The same holds for devices and breakpoints. Knowing your breakpoints does not
tell it which one a given frame is.

## Evidence, and what it falls back to

It asks for evidence at the start of every review. Research notes, analytics,
support themes, past usability sessions, anything already known about how people
behave here. Often there will be none, and the review proceeds anyway.

With evidence, a finding is backed by the evidence.

Without it, a finding is backed by a named principle and a source that can be
checked: an established heuristic, a documented psychological effect, a
well-evidenced pattern. Named, not gestured at. This is the difference between a
reasoned finding and taste.

The starter set in `knowledge/effects/` covers the strategic half of that, the
psychological effects and laws worth reasoning with (cognitive load, Hick's law,
the peak-end rule, the Zeigarnik effect and the rest), from free, open sources. Each
is summarised into a local file rather than fetched live at review time, so a review
is never blocked on a website.

The knowledge base is where it starts, not where it stops. The agent reasons as a
designer first and looks for backing second. When a finding rests on something
neither knowledge layer holds, it says so, searches, and cites what it finds. The
source then goes into the work folder's `05-knowledge/` through `ux-add-reference`,
so the next review has it locally. If nothing credible turns up, the finding stays and is marked as
judgement.

## It asks why before it judges

Once the angle is set, it lists the choices in the work that look deliberate and
asks the reasoning behind the ones that would change the verdict. A design choice
usually has a reason the artefact does not show. An answer becomes context. A
reason it still disagrees with becomes a finding that says so.

## The journey model

The thing that has to be invented first, because everything else depends on it.
One file per review, holding:

- **Actor.** Who this is for, in their own terms. Teacher on a phone, mid-lesson.
- **Job.** The one thing they are trying to get done.
- **Angle.** The need, JTBD or story this review is judging against.
- **Entry.** Where they arrive from, and what they already know and hold when they
  arrive.
- **Steps.** One per meaningful moment. Each records four things: what they see,
  what they must decide, what they must supply, and what can go wrong here.
- **States.** Empty, loading, error, partial, first-time, returning. Which ones the
  artefact covers and which it is silent on.
- **Exits.** Success, failure, and abandon. Abandon is the one artefacts never
  show and the one worth asking about.
- **Applied context.** Which stored knowledge this review was told to use, named
  explicitly. Product, persona, device, breakpoint. Empty until confirmed.
- **Unknowns.** What the artefact does not say and the review had to assume.

Unknowns are part of the model rather than a caveat at the end. A journey with
eleven unknowns is a finding on its own.

## How it judges

**Pass one, the problem.** Given the actor, the job and the angle, is the thing
being built a solution to that job? Is the job real, or inherited from how the
current product happens to work? Would the actor recognise this as their problem?
This pass can end the review, and often should. A well-made solution to the wrong
problem gets one finding, not fifteen.

**Pass two, the solution.** Given that the problem stands, walk the steps and
count the cost. Where does the user have to remember something the system already
knows? Where do they have to decide without the information to decide? Where does
a wrong guess cost them work? Where does the journey ask for effort before it has
given any value? Where is a state missing that the user will certainly hit?

**Pass three, alternatives, only when earned.** When pass one fails, or when pass
two finds a cost that is structural rather than fixable, it proposes different
shapes for the journey. Two or three, each with what it would cost to build and
what it gives up. This pass is where the brief to look outside the norm lives, and
it is gated so the agent does not redesign things that only needed three fixes.

Alternatives are judged against what already exists, both what the client ships today
and how the problem is solved elsewhere. A proposal that ignores either will not
survive contact with stakeholders, which is what `knowledge/` is for.

## Every finding carries a consequence

A finding is not valid unless it names what happens to the actor. "The filter is
unclear" is not a finding. "A teacher who picks Year 3 here gets results for the
whole key stage and will not notice until she opens one" is.

The consequence is the finding. The backing sits underneath it, as evidence where
there is any and as a named principle with a source where there is not. A
heuristic name is never the finding itself.

## Every report carries both a verdict and the findings

The verdict sits at the top, marked as a suggestion rather than a decision, and
it names the findings it rests on by number. Ship, fix these, or rethink, with
the reasoning in a line or two.

Every finding then appears in full underneath, including the ones the verdict
judged cheap. Nothing is dropped because it did not change the call.

That way the call is there to disagree with and the rationale is there to check
it against. It also means the verdict can be wrong without the report being
useless.

## Accessibility, proportioned to the conversation

In scope, and weighted by where the discussion has got to.

- **Discussing a broad solution**: none. It waits until you and it have agreed a
  way forward. Raising focus order against a shape that may be discarded is noise.
- **Roughly settled, or assessing specific screens**: about a fifth of the output.
  Keyboard order, focus, what a screen reader announces, contrast where it stops
  being decorative and starts being information.
- **Asked for an accessibility review**: that becomes the whole review.

## Out of scope

- **Aesthetics, trend and visual craft.** Colour, type, spacing, whether it looks
  current.
- **Design system conformance.** This is a UX agent, not a UI agent, and parity
  already has its own tooling.
- **Editing anything.** Capture is read-only, always.
- **A screen judged in isolation** without asking what came before it.

## When it disagrees with you

It holds the line where it has strong backing and can name a source that stands
up. Being contradicted is not a reason to fold.

It folds when you make the stronger case, or when you show it is wrong. No
performance of being persuaded, and no repeating the point in a later message.

Where you tell it to stop arguing, it stops and does what you asked. It records
the disagreement in the work folder's `05-knowledge/disputes/`: what it claimed, what you decided, and
what would settle it. That file is the thing to read back when the answer shows
up in real use, and it is how both of you find out which view was actually
stronger.

## Yours now, the designers later

Two cheap things now are what make that handover free.

**Candid context goes in its own file from day one.** `private.md` in the client
folder rather than mixed into `products.md`, so opening this up is a matter of not copying one
file rather than a read-through of everything it has learnt.

**A finding is about the work, never the person who made it.** No "the designer
has not considered", no inference about why a choice was made. This is the only
rule in the format that would need a rewrite later if it were skipped now.

Tone stays blunt either way. Findings that name a consequence for the actor are
already safe to hand to whoever made the thing.

## How it learns

Knowledge that is true everywhere sits in two layers, split by who it belongs to.
What is true of one client sits in a third place.

`knowledge/` in the agent folder is the starter set it ships with: free, open
sources, each summarised with short quotes and a link. `05-knowledge/` in the work
folder is yours: the sources you added, paid or free, and every lesson from your
reviews. Each layer has an `INDEX.md` listing every file in it with one line each,
so a review reads both indexes and picks the few files that apply.

| File | Holds | Comes from | Layer |
| --- | --- | --- | --- |
| `effects/` | The psychological effects and heuristics it reasons with, each with its source. | Seeded from NN/g, W3C, Laws of UX and GOV.UK, then extended by you and by searches during reviews | Both |
| `patterns/` | How a problem is solved today in the market, one file per pattern. This is what stops proposals arriving with no idea what already exists. | It, as it reviews | Both |
| `principles.md` | The judgements you have taught it, each with the case that produced it. | Your corrections | Yours |
| `disputes/` | Open disagreements, and closed ones with what settled them. | Both of you | Yours |
| `sources.md` | Every web source copied in, with the date. | `ux-add-reference` | Both |

`01-clients/<name>/` in the work folder holds what is true of one client, in two layers, and is applied
only when you name or confirm it.

- **The client:** `company.md` (who they are, their principles, their quality
  bar, how they make money) and `private.md`, the candid half that is never
  shared and never quoted in a review.
- **Each product:** `products/<product>/` with `product.md` (what it is, what is
  fixed, what was tried and failed, competitors), `users.md`, `personas.md` and
  `platforms.md`. Users and personas belong to a product, not to the client,
  because two products from one client rarely share them.

The first client set up was the owner's own, with two products of his, a to-dos app and an agents
dashboard.

`03-reviews/<date>-<slug>/` holds the output: the evidence, `journey.md` and
`review.md`. It sits outside `knowledge/` because it is output, and the agent
reads the last review of the same product on purpose, to name where it now
disagrees with itself.

Corrections go in through one skill rather than by editing the files, so a lesson
is written the same way every time and always keeps the case that produced it.

## The contracts

`contracts/` is the only authority on format. The skills point at it rather than
restating it.

- `angle.md`: actor, job, angle, the decisions questions, and confirmed context.
- `journey-model.md`: the model as a template.
- `review-format.md`: verdict, findings, and what is checked before a review is
  shown.

## The skills

| Skill | What it does | Why it is separate |
| --- | --- | --- |
| `ux-review` | The entry point. Establishes the angle, asks about the decisions, runs all four stages, writes the review. | The thing you actually call. |
| `ux-capture` | Gets an artefact onto disk as evidence, with a list of what it could not read. Modes: live page, Figma file, Figma prototype, diagram or text. | Ingestion is where the tooling and the failures are. Keeping it out means the judgement can be tested without any of it. |
| `ux-alternatives` | Proposes different shapes for a journey, against what exists today and elsewhere, with costs and trade-offs. | Called on its own when you want options rather than a verdict. |
| `ux-learn` | Writes a correction, a pattern or a dispute into the work folder's `05-knowledge/`. | One writer for the lessons, same reason the `pa` skill is the only thing that writes the to-do list. |
| `ux-add-reference` | Copies a web source into the work folder's `05-knowledge/`, or into the starter `knowledge/` when maintaining it. Built. | Sources and lessons are different kinds of knowledge. |

Plus one agent definition, so a review can be handed off and come back as a
report rather than filling a session.

## Where a review goes

Always a file in `03-reviews/`. Comments on a Figma file as well, but only the ones
you approve in the conversation, one by one. Nothing is posted to Figma unattended.

## Running unattended

It will, once there is a queue of things to review. The queue is a work stream on
`PACKAGES/work-streams`, one item per artefact, and an item without an actor, a job
and an angle is refused. Unattended, it cannot ask about decisions, so its
questions go at the top of the review, the verdict is marked provisional, and the
item comes back to you as `needs_you`. Proposed Figma comments wait in the review
for your yes.

It runs on the shared runner in `PACKAGES/agents-engine` (`RUNNER.md` there),
the first agent to do so. The runner owns the wake, the lock, the queue pass, the
budget, the daily log and the dashboard's commands. This folder provides only its
own part:

- `templates/stream.json`, written into `02-queue/` with this machine's paths: one document per artefact, carrying actor, job, angle,
  client, product and where the artefact is.
- A hooks module: `eligible` refuses an item missing any of the three angle
  fields, `prompt` runs `ux-review` in its unattended mode, `land` writes to
  `03-reviews/` and marks the verdict provisional.
- `agent.json` with the `wake` command, so the dashboard switches it on and sets
  its hours.

One target per client, so each client's reviews have their own switch, hours and
budget.

## Build order

1. **Contracts, tested by hand** against the to-dos board on port 8765, angle:
   delegation and collaboration between a person and agents.
2. **`ux-review` over text, screenshots and a live page**, with `knowledge/INDEX.md`
   and three eval cases, each listing what a good review must raise and must not.
3. **Client context**, set up with you once the first review has run.
4. **`ux-capture` for Figma**, then diagrams.
5. **`ux-learn`, `patterns/` and `disputes/`.**
6. **The agent definition, then `ux-alternatives`.**
7. ~~**The queue, hooks and `agent.json` on the shared runner** (`PACKAGES/agents-engine/RUNNER.md`).~~ Built 21 Sep 2026.

Local only for now: a local git repo and an `IMPROVEMENTS.md`, no remote.
