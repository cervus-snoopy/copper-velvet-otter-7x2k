#!/usr/bin/env python3
"""Write one satirical sentence to /output/entry.txt.

The entry roasts a lawmaker who regulates artificial intelligence while
being unable to convert a file to PDF. Pure Python 3 standard library,
no network access.

SPDX-License-Identifier: MIT
"""

import os
import stat
import sys

ENTRY = (
    "The senator chairing the committee that will decide how artificial "
    "intelligence is allowed to think spent his morning faxing his own bill "
    "to his own office, because nobody in the building could show him the "
    "button that turns a document into a PDF."
)


def validate(text):
    """Check the entry against the bounty gate before anything is written."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= 320):
        raise ValueError("entry must be 1-320 characters, got %d" % len(text))
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    if "?" in text or "!" in text:
        raise ValueError("entry must be exactly one sentence")
    text.encode("utf-8")
    return text


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = validate(ENTRY)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    os.chmod(path, 0o644)
    with open(path, "r", encoding="utf-8", newline="") as handle:
        back = handle.read()
    if back != text:
        raise ValueError("re-read mismatch after writing entry.txt")
    mode = stat.S_IMODE(os.stat(path).st_mode)
    if mode != 0o644:
        raise ValueError("entry.txt mode is %o, expected 644" % mode)
    return 0


if __name__ == "__main__":
    sys.exit(main())
