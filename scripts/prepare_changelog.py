#!/usr/bin/env python
from datetime import datetime
from pathlib import Path

from src.splatbot import __version__


def main():
    changelog = Path("CHANGELOG.md")

    with changelog.open() as fp:
        lines = fp.readlines()

    insert_idx = -1
    for i in range(len(lines)):
        line = lines[i]
        if line.startswith("## [Unreleased]"):
            insert_idx = i + 1
        elif line.startswith(f"## [{__version__}]"):
            print("CHANGELOG.md already up-to-date.")
            return

        elif line.startswith("## ["):
            break

    if insert_idx < 0:
        raise RuntimeError("Couldn't find [Unreleased] section.")

    lines.insert(insert_idx, "\n")
    lines.insert(insert_idx + 1, f"## [{__version__}] - {datetime.now().strftime('%Y-%m-%d')}\n")

    with changelog.open("w") as fp:
        fp.writelines(lines)


if __name__ == "__main__":
    main()
