#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog (v2).

Writes one single-line patch note for a bug in human biology to
/output/entry.txt. The entry is a fixed, authored line: the program's job
is to emit it byte-exactly, with no trailing newline, and to refuse to
produce output that would fail the competition gate (1-160 characters,
UTF-8, not only whitespace, exactly one line).
"""

import os
import sys

ENTRY = (
    "v2.0.4: fixed a bug where the brain replayed your most embarrassing "
    "moment from 2013 at 3 a.m. every night, with no skip button."
)

MAX_CHARS = 160


def validate(text: str) -> None:
    """Reject anything that would fail the gate, before writing it."""
    if not text or not text.strip():
        raise ValueError("entry is empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def verify_round_trip(path: str, expected: str) -> None:
    """Read the file back and confirm it is byte-exactly the entry.

    Catches silent truncation, encoding surprises, and stray newlines
    (e.g. a platform default that appends one) before the run is
    reported as a success.
    """
    with open(path, "rb") as f:
        raw = f.read()
    if raw != expected.encode("utf-8"):
        raise ValueError(
            f"round-trip mismatch: wrote {len(expected.encode('utf-8'))} bytes, "
            f"read back {len(raw)} bytes"
        )
    text = raw.decode("utf-8")
    if len(text) != len(expected) or text != expected:
        raise ValueError("round-trip mismatch: decoded text differs")
    if text.endswith("\n") or text.endswith("\r"):
        raise ValueError("round-trip mismatch: trailing newline present")


def main() -> int:
    validate(ENTRY)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    # newline="" + explicit encoding keeps the bytes exactly the entry text.
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    verify_round_trip(out_path, ENTRY)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (ValueError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        sys.exit(1)
