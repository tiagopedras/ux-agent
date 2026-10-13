---
name: ux-learn
description: Write a lesson into the UX agent's knowledge so the next review starts with it. Three kinds — a principle he taught it by correcting a review, a pattern for how a problem is solved (seen in a review or in another product), and a dispute where he and the agent disagree. Each keeps the case that produced it. Use whenever he corrects the UX agent and it should stick, says "remember this for reviews", "the agent should know this", "log this disagreement", "we disagree on this", "record this pattern", or when a review ends with him overruling a finding or telling it to stop arguing. Also use to close a dispute once real use settles it. Do not use it to add a web source, which is ux-add-reference, or to review anything, which is ux-review.
---

# Learning from a review

The only writer of lessons in the UX agent. The **agent folder** is
`AGENT=$(dirname "$(dirname "$(realpath ~/.claude/skills/ux-learn)")")`. Lessons belong to
the owner, so they live in the work folder's `05-knowledge/` (`python3 "$AGENT/setup.py"
--status` prints the work folder as `work_dir`), and all paths below are under it. The
agent's own `knowledge/` is the starter set it ships with and never takes a lesson. A lesson
is written the same way every time and always keeps the case that produced it, so it can be
checked later against what really happened.

## 1. Which kind

Decide from what he said, and ask if it is not clear.

| Kind | When | Where it goes |
| --- | --- | --- |
| **Principle** | He corrected how the agent works or judges, and agrees it should always apply. | `principles.md` |
| **Pattern** | How a problem is solved, in a product under review or elsewhere, worth reusing when proposing alternatives. | `patterns/<slug>.md` |
| **Dispute** | He and the agent disagree, or he is not convinced, and nothing has settled it yet. | `disputes/<slug>.md` |

Something the agent proposed that he has not accepted is a dispute, never a principle.
A principle applies to every client. Anything true of one client or product goes in that
client's folder in the work folder's `01-clients/`, not here.

## 2. Check for a duplicate

Read `INDEX.md`, `principles.md` and `disputes/`. If any of them is missing, run
`python3 "$AGENT/setup.py" --work-dir <work_dir>` first, which creates them and changes
nothing that exists. If the lesson is already there, update
that entry and add the new case to it rather than writing a second one.

## 3. Write it

**Principle**, appended to `principles.md` under the next number:

```markdown
### <n>. <The rule, one sentence, as an instruction>
**Case:** <review folder or conversation, date> — what happened.
**Why:** what went wrong for him, or would have.
**Applies when:** the situations it covers.
```

**Pattern**, one file:

```markdown
# <Product or source>: <the problem it solves>

Seen in: <review folder, or URL>. Written <date>.

## The problem
## How it is solved
## What it costs and what it gives up
## When to propose it
```

A pattern copied from a web page goes through `ux-add-reference` instead, with its source.

**Dispute**, one file:

```markdown
# <What is disputed, as a question>

Status: open · Opened <date> · Review: <review folder>

## What the agent claimed
The claim and its backing, as written in the review.

## What he thinks
In his words, shortened.

## What would settle it
The evidence or real use that would show which view is stronger.

## Outcome
Empty until settled: what happened, the date, and which view held.
```

When a dispute is settled, fill in Outcome, set Status to `closed`, and if the outcome is a
rule worth keeping, write it as a principle that points back to the dispute.

## 4. Update the index

Add or update the line in `INDEX.md` under "Lessons": the file, and one line saying what it
holds. `principles.md` gets one line for the file, not one per principle.

## 5. Report

One line per lesson: its kind, the file, and the sentence written. Nothing else.
