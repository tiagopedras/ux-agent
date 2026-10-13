"""The UX agent's part of an unattended run. The shared runner does the rest.

See `PACKAGES/agents-engine/RUNNER.md` for what the runner owns, and
`contracts/queue.md` for what a queue item holds. This file answers four things:
which items can be reviewed, what Claude is asked, what it may touch, and where
the review lands.

The clients, queue and reviews live in the work folder (`workdir.py`), not here.
One target per client folder in its `01-clients/`, so each client's reviews have their
own switch, hours and budget. An item's client is the folder it sits in, which
counts as the client being named, so the angle contract's "confirmed, never
assumed" holds without anyone in the room.
"""

import datetime as dt
import json
import os
import re

import workdir

ROOT = workdir.ROOT

ID = "ux-agent"
NAME = "UX agent"
BLURB = "reviews the journeys queued for it, one review per item, and leaves each one waiting for you"
HOURS_PREFERRED = list(range(19, 24)) + list(range(0, 7))
FIELDS = [
    {"key": "item_budget", "label": "Ceiling per review", "type": "number",
     "default": 3.0, "min": 0.5, "max": 20, "step": 0.5},
]

REQUIRED = ("actor", "job", "angle")
# The only shell command a review may run: it captures a page or copies a file,
# and refuses to write anywhere outside the work folder's reviews.
CAPTURE = "bin/capture.sh"

_dirs = {}


def targets():
    where = workdir.path("clients")
    if not where or not os.path.isdir(where):
        return []
    names = sorted(n for n in os.listdir(where)
                   if os.path.isdir(os.path.join(where, n)) and not n.startswith((".", "_")))
    return [{"id": n, "name": n, "subtitle": "01-clients/%s" % n, "where": "03-reviews/",
             "note": "reviews the work, never edits it"} for n in names]


def stream(target):
    return workdir.write_manifest()


def _brief(item):
    """The body without its title line."""
    return re.sub(r"\A\s*#[^\n]*\n", "", item["body"]).strip()


def _local(path):
    path = os.path.expanduser(path)
    if os.path.isabs(path):
        return path
    base = workdir.work_dir()
    if not base:
        raise ValueError("no work folder is set. Run: python3 %s" % os.path.join(ROOT, "setup.py"))
    return os.path.join(base, path)


def eligible(item, target):
    try:
        return _eligible(item, target)
    except ValueError as exc:
        return str(exc)


def _eligible(item, target):
    f = item["fields"]
    missing = [k for k in REQUIRED if not f.get(k)]
    if missing:
        return "no %s given. Add %s to the queue item" % (
            " or ".join(missing), "it" if len(missing) == 1 else "them")
    art = f.get("artefact", "")
    if not art and not _brief(item):
        return "nothing to review. Add an artefact (a URL or a file path) or write the brief under the frontmatter"
    if "figma.com" in art:
        return "Figma capture isn't built yet. Use screenshots as the artefact instead"
    if art and not art.startswith(("http://", "https://")) and not os.path.exists(_local(art)):
        return "the artefact %s does not exist" % art
    product = f.get("product")
    if product and not os.path.isdir(os.path.join(workdir.path("clients"), target["id"], "products", product)):
        return "01-clients/%s/products/%s does not exist" % (target["id"], product)
    return None


def _slug(title):
    return re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")[:50] or "review"


def review_dir(item):
    """<work>/03-reviews/<today>-<slug>, with -2, -3 when that folder is already taken."""
    if item["id"] in _dirs:
        return _dirs[item["id"]]
    base = workdir.path("reviews", "%s-%s" % (dt.date.today().isoformat(), _slug(item["title"])))
    out, n = base, 2
    while os.path.exists(out):
        out, n = "%s-%d" % (base, n), n + 1
    _dirs[item["id"]] = out
    return out


def prompt(item, target):
    f = item["fields"]
    t = target["id"]
    where = review_dir(item)
    client = os.path.join(workdir.path("clients"), t)
    product = f.get("product")
    lines = [
        "You are running unattended, off the UX agent's queue. Nobody will answer questions.",
        "",
        "Follow skills/ux-review/SKILL.md, with its \"Unattended\" section applied throughout:",
        "- Skip step 0. Do not create .welcomed.",
        "- Step 1 is answered below. Do not ask for anything.",
        "- Step 4: do not ask. Put the questions under \"Open questions\" at the top of review.md "
        "and mark the verdict provisional.",
        "- Step 7: no chat report. End with the JSON line described at the bottom.",
        "- Post nothing anywhere, including Figma.",
        "",
        "Actor: %s" % f["actor"],
        "Job: %s" % f["job"],
        "Angle: %s" % f["angle"],
        "Client: %s (confirmed). Apply %s/company.md and private.md." % (t, client),
    ]
    if product:
        lines.append("Product: %s (confirmed). Apply %s/products/%s/." % (product, client, product))
    else:
        lines.append("Product: none named. Apply no product folder.")
    if f.get("persona"):
        lines.append("Persona: %s" % f["persona"])
    if f.get("artefact"):
        lines.append("Artefact: %s" % f["artefact"])
    if _brief(item):
        lines += ["", "Brief, from the queue item:", _brief(item)]
    if f.get("feedback"):
        lines += ["", "Feedback from the owner on an earlier pass, to act on: %s" % f["feedback"]]
    lines += [
        "",
        "Write the review into %s/ (journey.md, review.md, evidence/)." % where,
        "To capture a page, or copy a local file into evidence, run "
        "`%s <url-or-file> %s/evidence/<name>.png [width,height]`. "
        "It is the only shell command you can run." % (CAPTURE, where),
        "",
        "Your final message must end with exactly one line of JSON and nothing after it:",
        '{"review": "%s/review.md", "verdict": "Ship|Fix these|Rethink", '
        '"findings": <number>, "open_questions": <number>}' % where,
    ]
    return "\n".join(lines)


def options(item, target):
    dirs = [workdir.work_dir()]
    art = item["fields"].get("artefact", "")
    if art and not art.startswith(("http://", "https://")):
        path = _local(art)
        dirs.append(path if os.path.isdir(path) else os.path.dirname(path))
    return {
        "tools": ["Read", "Glob", "Grep", "WebFetch", "WebSearch",
                  "Edit(/%s/**)" % workdir.path("reviews"),
                  "Edit(/%s/**)" % workdir.path("knowledge"), "Bash(%s:*)" % CAPTURE],
        "dirs": dirs,
        "budget": 3.0,
        "timeout": 20 * 60,
    }


def land(item, result, target):
    text = (result.get("text") or "").strip()
    answer = None
    for line in reversed(text.splitlines()):
        line = line.strip().strip("`")
        if line.startswith("{") and line.endswith("}"):
            try:
                answer = json.loads(line)
                break
            except ValueError:
                continue
    path = (answer or {}).get("review") or "%s/review.md" % review_dir(item)
    if not os.path.isfile(os.path.join(ROOT, path)):
        raise ValueError("no review was written at %s" % path)
    verdict = (answer or {}).get("verdict") or "no verdict given"
    questions = int((answer or {}).get("open_questions") or 0)
    findings = (answer or {}).get("findings")
    detail = "Provisional: %d question%s for you at the top." % (questions, "" if questions == 1 else "s") \
        if questions else "No open questions."
    if findings is not None:
        detail = "%s findings. %s" % (findings, detail)
    return {
        "ref": path,
        "label": "reviewed",
        "summary": "review written · %s" % verdict,
        "detail": detail,
        "fields": {"review": path},
    }
