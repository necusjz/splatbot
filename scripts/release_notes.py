#!/usr/bin/env python
import os

import packaging.version

TAG = os.environ["TAG"]


def get_changelog_notes():
    is_current_section = False
    section_notes = []

    with open("CHANGELOG.md") as changelog:
        for line in changelog:
            if line.startswith("## "):
                if line.startswith("## [Unreleased]"):
                    continue

                if line.startswith(f"## [{TAG[1:]}]"):
                    is_current_section = True
                    continue

                break

            if is_current_section:
                section_notes.append(line)

    assert section_notes

    return "## What's new\n\n" + "".join(section_notes).strip() + "\n"


def get_commit_history():
    version = packaging.version.parse(TAG)

    os.popen("git fetch --tags")
    tags = os.popen("git tag -l --sort=-version:refname 'v*'").read().split("\n")

    prev_tag = None
    for tag in tags:
        if not tag.strip():  # blank line
            continue

        curr_version = packaging.version.parse(tag)
        if version.pre is None and curr_version.pre is not None:  # ignore pre-release
            continue

        if curr_version < version:
            prev_tag = tag
            break

    if prev_tag is not None:
        commits = os.popen(f"git log {prev_tag}..{TAG} --oneline --first-parent").read()
    else:
        commits = os.popen("git log --oneline --first-parent").read()

    return "## Commits\n\n" + commits


def main():
    print(get_changelog_notes())
    print(get_commit_history())


if __name__ == "__main__":
    main()
