"""Router confession entry.

Writes the router's one-line confession to /output/entry.txt.
The line is a fixed constant; the program checks it against the
competition gate (1-200 chars, single line, no em dash) and writes
it out byte-for-byte, then verifies the written file matches.
"""

import os
import sys

CONFESSION = "Sometimes I blink my amber light for no reason just to watch two roommates blame each other for forgetting to pay the internet bill."

GATE_MIN = 1
GATE_MAX = 200


def gate_ok(text):
    """Return True when the line passes the competition gate."""
    if not (GATE_MIN <= len(text) <= GATE_MAX):
        return False
    if text.strip() == "":
        return False
    if "\n" in text or "\r" in text:
        return False
    if "\u2014" in text:
        return False
    return True


def verify(path, expected):
    """Re-read the written file and compare it byte-for-byte."""
    with open(path, "rb") as handle:
        written = handle.read()
    return written.decode("utf-8") == expected


def main():
    line = CONFESSION
    if not gate_ok(line):
        sys.stderr.write("gate failed: line does not satisfy 1-200 chars, single line\n")
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    os.chmod(path, 0o644)
    if not verify(path, line):
        sys.stderr.write("verify failed: entry.txt does not match the confession\n")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
