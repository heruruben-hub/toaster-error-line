#!/usr/bin/env python3
"""The Funniest Toaster Error Message — make.fun entry.

Writes a single-line toaster error message to /output/entry.txt.
The line must be one line, 1-120 characters, and not only whitespace.
After writing, the file is read back and checked byte-for-byte
against what was written; any mismatch fails the run.
"""

import os
import sys

LINE = "Error E07: the bread has unionized. Toasting suspended until further notice."
MAX_CHARS = 120
OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    line = LINE

    if not line or not line.strip():
        print("error: entry line is empty", file=sys.stderr)
        return 1
    if line != line.strip():
        print("error: entry must not start or end with whitespace", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(
            "error: entry is %d characters, max is %d" % (len(line), MAX_CHARS),
            file=sys.stderr,
        )
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(line)

    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        back = f.read()
    if back != line:
        print("error: read-back mismatch", file=sys.stderr)
        return 1

    print("wrote %d characters to %s" % (len(line), OUTPUT_PATH))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
