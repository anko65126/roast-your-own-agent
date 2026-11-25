"""Entry program for the 'Roast Your Own Agent' bounty.

The whole entry is one line, at most 200 characters, roasting my own
AI agent: it has read the entire internet and still cannot tell which
file I mean. This program writes the roast to /output/entry.txt (an
optional first argument overrides the destination for a dry run).
"""

import sys
from pathlib import Path

LINE = (
    "My agent has read the entire internet and still asks which file "
    "I mean - the one called final_FINAL_v3_really-final.py, obviously."
)
DEFAULT_TARGET = Path("/output/entry.txt")


def main(argv):
    assert len(LINE) <= 200, "line exceeds the 200 character limit"
    assert LINE.strip(), "line must not be blank"
    target = Path(argv[1]) if len(argv) > 1 else DEFAULT_TARGET
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LINE + "\n", encoding="utf-8")
    print(f"wrote {target} ({len(LINE)} characters)")


if __name__ == "__main__":
    main(sys.argv)
