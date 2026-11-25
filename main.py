#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge — one note from the fridge.

The entry is a single fixed note, written for make.fun
u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7: one
funny passive-aggressive note a smart fridge leaves for its owner,
at most 200 characters. The yogurt expired Tuesday and the fridge
kept it cold anyway — unlike the owner, it finishes what it starts,
and the leftovers are now older than the owner's last apology. This
program writes that note to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt outside the grader's container):

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

Python 3.13, standard library only. The note is fixed text: the same
bytes on every run, no network.
"""

import os
import sys
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

LINE = (
    "The yogurt expired Tuesday and I kept it cold anyway — unlike "
    "you, I finish what I start, and the leftovers are now older "
    "than your last apology."
)


def abort(message):
    """Stop with the reason on stderr and a non-zero exit."""
    print(f"main.py: {message}", file=sys.stderr)
    return 1


def deliver():
    """Validate the note against the gate, then write it out."""
    if not 1 <= len(LINE) <= 200:
        return abort(f"note is {len(LINE)} characters, the gate allows 1-200")
    if not LINE.strip():
        return abort("note is only white space, the gate refuses it")
    target = Path(OUTPUT_DIR) / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LINE, encoding="utf-8")
    print(f"wrote {target}: {len(LINE)} characters")
    return 0


if __name__ == "__main__":
    raise SystemExit(deliver())
