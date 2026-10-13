"""Where the owner's own work lives, kept out of the agent folder.

The agent folder holds the agent. Clients, the queue, reviews, evals and
private knowledge live in a work folder the owner picks on first run, named by
`work_dir` in `config.json` (gitignored; `config.example.json` shows the shape).
Run `python3 setup.py --status` to see where both folders are.
"""

import json
import os

ROOT = os.path.dirname(os.path.realpath(__file__))
CONFIG = os.path.join(ROOT, "config.json")

FOLDERS = {
    "clients": "01-clients",
    "queue": "02-queue",
    "reviews": "03-reviews",
    "evals": "04-evals",
    "knowledge": "05-knowledge",
}


def work_dir():
    """The configured work folder as an absolute path, or None before setup."""
    try:
        with open(CONFIG, encoding="utf-8") as fh:
            value = (json.load(fh) or {}).get("work_dir")
    except (OSError, ValueError):
        return None
    return os.path.abspath(os.path.expanduser(value)) if value else None


def path(kind, *parts):
    """A folder inside the work folder: path("reviews", "2026-01-01-x"). None before setup."""
    base = work_dir()
    return os.path.join(base, FOLDERS[kind], *parts) if base else None


def manifest_path():
    return path("queue", "stream.json")


def write_manifest():
    """Fill templates/stream.json with this machine's paths and write it into the work folder.

    The queue's manifest names its folder, lock and writer by absolute path
    because other readers resolve relative ones against the manifest, which no
    longer sits in the agent folder. Rewritten when the content differs, so a
    moved agent folder or work folder corrects itself.
    """
    target = manifest_path()
    if not target:
        return None
    with open(os.path.join(ROOT, "templates", "stream.json"), encoding="utf-8") as fh:
        text = fh.read()
    text = text.replace("<queue_dir>", path("queue")).replace("<agent_root>", ROOT)
    try:
        with open(target, encoding="utf-8") as fh:
            if fh.read() == text:
                return target
    except OSError:
        pass
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "w", encoding="utf-8") as fh:
        fh.write(text)
    return target
