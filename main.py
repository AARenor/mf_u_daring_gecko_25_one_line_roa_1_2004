"""Write one short roast line for a make.fun bounty entry."""

import os
import sys
from pathlib import Path

TEXT = "My watch congratulated me on a twelve-hour stand goal I hit standing at the fridge."


def main() -> int:
    assert 1 <= len(TEXT) <= 280, "entry text must be between 1 and 280 characters"

    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    destination = Path(out_dir)
    destination.mkdir(parents=True, exist_ok=True)

    (destination / "entry.txt").write_text(TEXT, encoding="utf-8", newline="")

    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
