#!/usr/bin/env python3
"""First-run setup for the UX agent's work folder.

  python3 setup.py --status                 where the agent and the work folder are, as JSON
  python3 setup.py --default                the suggested work folder
  python3 setup.py --work-dir <folder> [--force]   write config.json, create the numbered folders and empty knowledge files

Safe to run again: it never overwrites or deletes anything in the folder.
"""

import argparse
import json
import os
import shutil
import sys

import workdir


def default_dir():
    """Outside the agent folder, in the home folder."""
    return os.path.join(os.path.expanduser("~"), "ux_agent_work")


def status():
    base = workdir.work_dir()
    return {"agent_root": workdir.ROOT, "configured": bool(base), "work_dir": base,
            "default_work_dir": default_dir()}


def setup(folder, force=False):
    folder = os.path.abspath(os.path.expanduser(folder))
    current = workdir.work_dir()
    if current and current != folder and not force:
        raise SystemExit("config.json already points at %s. Pass --force to change it to %s." % (current, folder))
    if os.path.commonpath([folder, workdir.ROOT]) == workdir.ROOT:
        raise SystemExit("the work folder must be outside the agent folder (%s)" % workdir.ROOT)
    os.makedirs(folder, exist_ok=True)
    with open(workdir.CONFIG, "w", encoding="utf-8") as fh:
        json.dump({"work_dir": folder}, fh, indent=2)
        fh.write("\n")
    for name in workdir.FOLDERS.values():
        os.makedirs(os.path.join(folder, name), exist_ok=True)
    workdir.write_manifest()
    # STARTER-KNOWLEDGE: the owner's own knowledge layer. The starter set ships in the agent's
    # knowledge/; ux-review then lists it and offers to add the owner's sources.
    knowledge_skeleton()
    return status()


def knowledge_skeleton():
    """Create 05-knowledge's empty files and folders, leaving anything already there alone."""
    for name in ("disputes", "effects", "patterns"):
        os.makedirs(workdir.path("knowledge", name), exist_ok=True)
    principles = workdir.path("knowledge", "principles.md")
    if not os.path.exists(principles):
        open(principles, "w", encoding="utf-8").close()
    for name in ("INDEX.md", "sources.md"):
        target = workdir.path("knowledge", name)
        if not os.path.exists(target):
            shutil.copyfile(os.path.join(workdir.ROOT, "templates", "knowledge", name), target)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--status", action="store_true")
    ap.add_argument("--default", action="store_true")
    ap.add_argument("--work-dir")
    ap.add_argument("--force", action="store_true", help="replace a work_dir that is already configured")
    args = ap.parse_args()
    if args.default:
        print(default_dir())
    elif args.work_dir:
        print(json.dumps(setup(args.work_dir, args.force), indent=2))
    else:
        print(json.dumps(status(), indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
