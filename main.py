"""The Houseplant Out-of-Office — make.fun entry.

Writes one funny out-of-office auto-reply, as if a houseplant wrote it,
to /output/entry.txt. The line is the whole entry: at most 120 characters,
a single line, UTF-8.
"""

import os

ENTRY = (
    "Out of office: I'm a fern, ignored since March. "
    "Water me and I'll reply. "
    "Until then I'm wilting here and judging you."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = ENTRY.strip()
    # Validation guard: the gate requires 1-120 chars, a single line,
    # UTF-8 text that is not only whitespace.
    assert 1 <= len(line) <= 120, f"entry is {len(line)} chars, must be 1-120"
    assert "\n" not in line and "\r" not in line, "entry must be a single line"
    assert line.strip(), "entry must not be only whitespace"
    line.encode("utf-8")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
