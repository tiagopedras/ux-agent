# The angle contract

No review starts until three things are known. The agent asks for any that are missing and
never infers them from the artefact.

| Field | What it holds | Counts as answered when |
| --- | --- | --- |
| **Actor** | Who this is for, in their own terms, and where they are when they use it. | It names a person in a situation, not a segment. "Me, at my desk, between meetings" rather than "power users". |
| **Job** | What they are trying to get done, stated without the interface. | It would still be true if the product did not exist. |
| **Angle** | The need, job story or worry this review judges against. | It narrows the review to part of the work. "Delegation between human and agents feels odd" rather than "the whole app". |

## The second question

When the artefact is large and the angle is broad, it asks which part carries the worry.
Reviewing everything happens only when asked for.

## Decisions before judgement

Once the angle is set, and before any finding is written, the agent walks the artefact and
lists the choices that look deliberate. It asks why for the ones that would change the
verdict, and only those. A handful of questions, grouped, asked once.

- An answer becomes applied context in the journey model.
- A reason the agent still disagrees with becomes a finding, and says it is a disagreement
  with a stated reason.
- A question left unanswered becomes an Unknown.

## Context is confirmed, never assumed

Client context is applied only when the owner names it or confirms it, in two steps: the
client (`01-clients/<name>/company.md` in the work folder), then the product (`01-clients/<name>/products/<product>/`).
A product's users and personas never apply to another product of the same client.
The agent may offer what it holds as options. It may not decide from a screenshot which
product, persona, device or breakpoint it is looking at.

## Unattended

A queued item without all three fields is refused. The decisions questions cannot be asked,
so they go at the top of the review, the verdict is marked provisional, and the item goes
back to the owner.
