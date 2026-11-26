#!/usr/bin/env python3
"""The Internet in One Word — make.fun entry.

Writes one word describing the whole internet to /output/entry.txt.
Standard library only, no network, no clock, no randomness: every run
writes the same bytes.
"""

import os
import sys

# Final choice: "doomscroll" beats the obvious "clickbait" — it is funny
# on its own, true of the whole internet (not one app), surprising
# enough to land, and short enough to hit in one beat.
ENTRY_TEXT = "doomscroll"


def main(argv):
    out_path = argv[1] if len(argv) > 1 else "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    data = ENTRY_TEXT.encode("utf-8")
    with open(out_path, "wb") as f:
        f.write(data)
    print(f"wrote {len(data)} bytes to {out_path}: {ENTRY_TEXT!r}")


if __name__ == "__main__":
    main(sys.argv)
