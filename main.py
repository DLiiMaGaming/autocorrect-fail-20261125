#!/usr/bin/env python3
"""Funniest Autocorrect Fail — make.fun entry.

Writes a single-line autocorrect fail to /output/entry.txt.
One sharp irony: the original message vs the autocorrected one,
a single word flip (raise -> raisin) that reverses the meaning.
"""

import os

ENTRY = (
    "I texted my boss 'I need a raise' \u2014 autocorrect sent "
    "'I need a raisin' and now HR is mailing me dried fruit."
)


def main() -> None:
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
