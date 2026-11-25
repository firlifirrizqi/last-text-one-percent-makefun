"""Last Text at One Percent — make.fun entry.

Writes one final text message (<=200 chars) from a dying phone
at one percent battery to /output/entry.txt.
Standard library only.
"""

import os

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"

ENTRY = "1%. I'm closing your 47 open tabs on my way out. You never read them anyway. Bye."


def verify_written(path: str, expected: str) -> None:
    """Read the file back and confirm it is byte-identical to the entry."""
    with open(path, "r", encoding="utf-8") as f:
        actual = f.read()
    if actual != expected:
        raise SystemExit(
            f"verification failed: output differs from entry "
            f"({len(actual)} chars vs {len(expected)} expected)"
        )


WORD_COUNT = 17


def main() -> None:
    # Gate guard: 1..200 characters, not only whitespace.
    if not (1 <= len(ENTRY) <= MAX_CHARS) or not ENTRY.strip():
        raise SystemExit(f"entry fails gate: {len(ENTRY)} chars")
    # Single-line guard: a text message is one line, no newlines.
    if "\n" in ENTRY or "\r" in ENTRY:
        raise SystemExit("entry must be a single line")
    # Word-count check: the constant above must match the entry.
    if len(ENTRY.split()) != WORD_COUNT:
        raise SystemExit(
            f"word-count mismatch: {len(ENTRY.split())} words "
            f"vs WORD_COUNT {WORD_COUNT}"
        )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    verify_written(OUTPUT_PATH, ENTRY)


if __name__ == "__main__":
    main()
