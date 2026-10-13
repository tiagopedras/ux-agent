# The review format

One file per review, `03-reviews/<date>-<slug>/review.md` in the work folder, next to its `journey.md`.

```markdown
# <Journey name>: UX review

Reviewed <date> · Actor: <actor> · Angle: <angle>

## Verdict (a suggestion)
**Ship / Fix these / Rethink.** One or two lines of reasoning, citing findings by number.

## Open questions
Only when unattended, or when a question stayed unanswered. What would change the verdict.

## Findings

### 1. <The consequence, as a sentence about the actor>
**Where:** step or screen
**Why it happens:** what in the work causes it
**Backing:** evidence given, or a named principle with a link to its file in `knowledge/`,
or a web source found during the review. "Judgement" when nothing credible was found.
**Fix:** what to change, when there is an obvious one

## Alternatives
Only when the verdict is Rethink, or a finding is structural. Two or three shapes, each with
what it costs to build and what it gives up, set against how the problem is solved today.

## Accessibility
Proportioned to the conversation, as PLAN.md sets out.

## Sources added
Anything pulled into `knowledge/` during this review.
```

## What a finding must do

- Its title names what happens to the actor. "A teacher who picks Year 3 gets the whole key
  stage and will not notice until she opens one." Never "the filter is unclear".
- It is about the work, never the person who made it.
- A principle backs a finding. It is never the finding.

## Checked before the review is shown

- No line of a client's `private.md` appears.
- Every finding's title names a consequence for the actor.
- The verdict cites only findings that exist.
- Every Unknown in the journey model is either in a finding, an open question, or accepted.
- No Figma comment is posted without the owner's yes in the conversation.
