#!/usr/bin/env python3
"""Write the one-word entry for the internet to the output directory.

Entry for make.fun's "The Internet in One Word" bounty
(u-ronigrv-the-internet-in-one-word-e388f33b): a single word that
describes the whole internet, funny and fitting at once.
"""
import os

WORD = "Doomscroll"
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
DST = os.path.join(OUT, "entry.txt")

os.makedirs(OUT, exist_ok=True)
with open(DST, "w", encoding="utf-8") as f:
    f.write(WORD + "\n")

# The gate wants one word of 1 to 30 characters, so read the file back
# and refuse to leave a broken entry behind: a word with a space in it
# would lose to any single word, and a file that is only whitespace
# would fail the gate outright.
with open(DST, encoding="utf-8") as f:
    seen = f.read()
if not (1 <= len(seen.strip()) <= 30):
    raise SystemExit(f"entry is {len(seen.strip())} characters, gate wants 1-30")
if len(seen.split()) != 1:
    raise SystemExit("entry is not a single word")
print("verified one word:", seen.strip())
