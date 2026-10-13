---
name: ux-add-reference
description: Add a web reference to the UX agent's knowledge base. Fetches the page or collection, saves a local copy under the work folder's 05-knowledge/effects/ or 05-knowledge/patterns/ in the house format, and lists it in that folder's sources.md and INDEX.md. Also maintains the starter set in the agent's own knowledge/, only when asked to. Use whenever he gives a URL, article, glossary, heuristics list or framework to add as a source for the UX agent, or says "add this reference", "pull this into the knowledge base", "add this to the UX sources", "the agent should know about this". Also use to refresh a reference already in sources.md. Do not use it to record a correction, a pattern learnt from a review or a dispute, which is ux-learn, and do not use it to review a design, which is ux-review.
---

# Add a reference

The UX agent reasons with named sources, and a review never waits on a website, so every
reference is copied into the knowledge base once and read from there. This skill does the
copying, in one shape every time, and keeps the sources list true.

The **agent folder** is
`AGENT=$(dirname "$(dirname "$(realpath ~/.claude/skills/ux-add-reference)")")`.
`python3 "$AGENT/setup.py" --status` prints the work folder as `work_dir`.

The knowledge base has two layers, and this skill writes to one per run:

- **The owner's sources**, the default: the work folder's `05-knowledge/`, with its own
  `sources.md` and `INDEX.md`. Every source the owner gives, and every source a review finds,
  goes here, paid or free. If those two files are missing, run
  `python3 "$AGENT/setup.py" --work-dir <work_dir>` first, which creates them and changes
  nothing that exists.
- **The starter set**: the agent folder's `knowledge/`, which ships with the agent. Only when
  he says explicitly that he is maintaining the starter set. A starter source must be free to
  read without signing in, and its file is a summary with short quotes and a link, never a
  full copy.

Below, `<kb>` is whichever of the two this run writes to.

## 1. Settle three things before fetching

Ask for whichever are missing, as a question with options where you can.

- **The URL.**
- **One page or a collection.** One article gets one file. A glossary, a heuristics site or
  any list of linked entries gets an index file plus one file per entry.
- **Where it lives.** `<kb>/effects/` for psychological effects, heuristics and
  principles the agent reasons with. `<kb>/patterns/` for how a problem is solved, in a
  product or in the market. Ask if it is not obvious.

Read `sources.md` in both layers first. If the source is already listed in either, refresh the
existing files and update the pulled date there. Never add a second row.

## 2. Fetch

- One page: WebFetch, asking for the exact title, author, dates and the source's own wording.
- A collection: use `curl -sL -A "Mozilla/5.0"`, not Python's `urllib`, which fails on this
  machine's certificates. Check `robots.txt` for a sitemap. Listing pages often load only part
  of a collection (one glossary showed 24 of its 53 entries), and the sitemap or the
  page's structured data (`application/ld+json`) holds the rest.
- Fetch politely: one request at a time, a short pause between them.
- Compare what you got with any count the site states. If they differ, find the missing ones
  before writing anything.

## 3. Copy only what the page shows

Copy what a reader sees without paying or signing in. If the page shows a paywall or a sign-in
gate, the gated text stays out, even when it turns up in the page's data. Say in the file and
in the report that it was left out.

Keep the source's own wording, in quotes where it is a definition, and credit the author. The
agent's own reading of a source goes in `principles.md`, written by `ux-learn`, and never
into a reference file.

## 4. Write the files

Every file opens the same way:

```
# <Title>

Source: <url>. Pulled <today's date>. Page last updated <date, if the page shows one>.
```

Then the content, laid out as the source lays it out, with a table for a list of like things
(see `$AGENT/knowledge/effects/nng-10-usability-heuristics.md`). Links between entries of one
collection point at the local files.

- One page: `<kb>/<folder>/<source>-<topic>.md`.
- A collection: `<kb>/<folder>/<source>-<topic>.md` as the index (term, definition,
  local file, site link), and `<kb>/<folder>/<source>/<slug>.md` for each entry.

## 5. Update sources.md and INDEX.md

Add one row to the table in `<kb>/sources.md`: the source as a link, what it gives, where
the local copy is, and the date pulled. Keep the table in the order sources were added.

Then add a line for each new file to `<kb>/INDEX.md`, in the section that fits
(heuristics and guidelines, patterns, or effects). A review reads the index to pick its files,
so a source missing from it is never used.

## 6. Check, then report

- The number of entry files equals the number the site states, or the report says which are
  missing and why.
- No entry file is empty, and none holds a paywall prompt or navigation text.
- Every link between local files resolves.

Report in a few lines: what was added, how many files, anything left out and why. Nothing else.
