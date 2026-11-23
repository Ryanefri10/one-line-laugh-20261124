#!/usr/bin/env python3
"""The One-Line Laugh -- make.fun bounty entry.

Writes a single funny line (one sentence, at most 200 characters) to
``entry.txt`` inside the output directory the harness provides
(``MAKEFUN_OUTPUT_DIR``, which is ``/output`` in the grading sandbox).

Stdlib only.
"""

import os

LINE = (
    "I downloaded a meditation app to calm my mind, and now it sends me "
    "daily reminders that stress me out for not meditating."
)


def main() -> None:
    # Gate: the scorer only accepts UTF-8 text of 1 to 200 characters,
    # not only white space, standing alone as a single sentence.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.strip() == LINE and LINE, "line must not be blank-padded"
    assert LINE.count(".") == 1 and LINE.endswith("."), "one sentence only"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    # The grader collects outputs as another user: leave the file readable.
    os.chmod(path, 0o644)
    print(f"Wrote {len(LINE)} characters to {path}")


if __name__ == "__main__":
    main()
