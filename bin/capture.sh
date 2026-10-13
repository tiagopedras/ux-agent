#!/bin/bash
# Evidence for an unattended review, and the only shell command one may run.
#
#   bin/capture.sh <url> <work folder>/03-reviews/<dir>/evidence/<name>.png [width,height]
#   bin/capture.sh <file> <work folder>/03-reviews/<dir>/evidence/<name>.png
#
# A URL is screenshotted with headless Chrome, killed after 20 seconds because
# pages that poll never finish loading. A file is copied. Either way it writes
# under the work folder's 03-reviews/ and nowhere else, which is why the runner can allow
# it. The work folder is `work_dir` in config.json at the agent root.

set -uo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC="${1:-}"; OUT="${2:-}"; SIZE="${3:-1600,1100}"

WORK="$(python3 -c 'import json,os,sys; print(os.path.abspath(os.path.expanduser(json.load(open(sys.argv[1]))["work_dir"])))' "$ROOT/config.json" 2>/dev/null)"
[ -n "$WORK" ] || { echo "no work_dir in $ROOT/config.json. Run: python3 $ROOT/setup.py" >&2; exit 2; }
REVIEWS="$WORK/03-reviews"

case "$OUT" in "$REVIEWS"/*) ;; *) echo "the output must be under $REVIEWS/" >&2; exit 2 ;; esac
case "$OUT" in *..*) echo "the output path cannot contain .." >&2; exit 2 ;; esac
[ -n "$SRC" ] || { echo "usage: bin/capture.sh <url-or-file> <out.png> [width,height]" >&2; exit 2; }

mkdir -p "$(dirname "$OUT")"
if [ -f "$SRC" ]; then
  cp "$SRC" "$OUT" && echo "copied to $OUT"
  exit $?
fi

PROFILE="$(mktemp -d)"
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu \
  --user-data-dir="$PROFILE" --hide-scrollbars --window-size="$SIZE" \
  --virtual-time-budget=5000 --screenshot="$OUT" "$SRC" >/dev/null 2>&1 &
PID=$!
( sleep 20; kill "$PID" 2>/dev/null ) &
KILLER=$!
wait "$PID" 2>/dev/null
kill "$KILLER" 2>/dev/null
rm -rf "$PROFILE"
if [ -f "$OUT" ]; then echo "saved $OUT"; else echo "no screenshot was taken of $SRC" >&2; exit 1; fi
