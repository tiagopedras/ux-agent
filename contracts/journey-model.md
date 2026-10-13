# The journey model

One file per review, `03-reviews/<date>-<slug>/journey.md` in the work folder. Everything downstream of capture
reads this and nothing else, so a prototype and a paragraph get the same treatment.

Copy the template below. Leave a field empty rather than guessing, and add the gap to
Unknowns.

```markdown
---
actor:
job:
angle:
artefact:          # what was reviewed: URL, Figma link, file, or "pasted text"
captured:          # date
applied_context:   # client files the owner confirmed, by path. Empty until confirmed.
---

# <Short name of the journey>

## Entry
Where the actor arrives from, what they already know, what they already hold.

## Steps

### 1. <Moment, named from the actor's side>
- **Sees:**
- **Decides:**
- **Supplies:**
- **Can go wrong:**
- **Walkthrough:** will they try it · will they see how · will they link it to their goal · will they know it worked

## States
| State | Covered | Where |
| --- | --- | --- |
| Empty | | |
| Loading | | |
| Error | | |
| Partial | | |
| First time | | |
| Returning | | |

## Exits
- **Success:**
- **Failure:**
- **Abandon:** where they would give up, and what they would do instead

## Decisions asked about
| Choice in the work | Why, as the owner put it |
| --- | --- |

## Unknowns
What the artefact does not say and the review had to assume, or what capture could not
read. A long list here is a finding in its own right.
```
