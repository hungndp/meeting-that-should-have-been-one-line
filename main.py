#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line.

Writes the single sentence that could have replaced an entire pointless
meeting to /output/entry.txt (gate: 1-200 UTF-8 characters, one line).

Why this line: the decision is already made (client approved Tuesday,
deadline moved Friday), so the meeting has nothing left to decide — its
only remaining activity is reading the email aloud. One incident, one
airtight timeline, and the reversal IS the line, with the sting
("reading that same email out loud") as the last words.
"""

import os

# Drafting notes (from past one-liner post-mortems):
# - Concrete incident + reversal: the approval already happened, so the
#   meeting is a re-enactment, not a decision. Specifics do the work:
#   Tuesday / Friday, twelve people, a room booked for an hour.
# - Understatement beats escalation: no shouting, no second clause after
#   the joke lands. The twist word ("out loud") closes the sentence.
# - No $ amounts, no setup, no explanation: the line stands alone.
SETUP = (
    "The client approved it on Tuesday, the deadline moved to Friday, "
    "and this meeting is twelve people in a room we booked for an hour "
)
PUNCH = "taking turns reading that same email out loud."


def build_line() -> str:
    """Compose the single meeting-killing sentence."""
    return SETUP + PUNCH


def validate(line: str) -> None:
    """Enforce the sealed gate: 1-200 chars, one line, not blank."""
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry is {len(line)} chars, gate is 1-200")
    if "\n" in line or not line.strip():
        raise ValueError("entry must be a single non-blank line")


def main() -> None:
    line = build_line()
    validate(line)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(line)


if __name__ == "__main__":
    main()
