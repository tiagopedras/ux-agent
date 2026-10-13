# The review queue

What the UX agent reviews when nobody is in the room. One Markdown file per
artefact, in the folder of the client it belongs to: `02-queue/<client>/plans-mobile.md` in the work folder.
The shared runner (`PACKAGES/agents-engine/RUNNER.md`) picks up anything in
`To review` at the client's scheduled hours, writes a review into `03-reviews/`, and
moves the item to `Waiting for you`.

## An item

```markdown
---
state: ready
owner: ux-agent
actor: Me, at my desk between meetings, checking what the agents did overnight
job: Decide which overnight plans to accept before the day starts
angle: Does the Plans view make it obvious which plans need a decision today?
product: bench
artefact: http://localhost:8765/#plans
---
# Plans view, first thing in the morning

Anything the agent should know that the page cannot show: what changed
recently, which state you are worried about, what to leave alone.
```

`actor`, `job` and `angle` are required, as `contracts/angle.md` defines them.
An item missing any of them is left alone and named in the day's log under
**Not run**, with what to add.

`artefact` is a URL or a file path (relative to the work folder, or
absolute). It can be left out when the brief itself is what is being reviewed,
such as a plan. A Figma link is refused until Figma capture is built; use
screenshots instead.

`product` and `persona` are optional. The client is the folder the item sits in.

## What the runner writes back

`state`, `owner`, `id`, `seen`, and `review` (the path of the review it wrote).
After three failed attempts it moves the item to `Blocked` with `needs_you: yes`
and the reason in `feedback`.

To ask for another pass, move the item back to `ready` with a line in
`feedback`. An item moved back with no change is skipped as unchanged.

## Where to see what happened

`state/<client>/runs/<date>.md`, one per day: what ran, what did not and why,
and what failed with what fixes it.
