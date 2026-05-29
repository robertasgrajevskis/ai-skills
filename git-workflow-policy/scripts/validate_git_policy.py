#!/usr/bin/env python3
"""Validate branch names, commit messages, and PR titles for the Git workflow."""

from __future__ import annotations

import argparse
import re
import sys

TYPES = ("feat", "bugfix", "chore")
TYPE_PATTERN = "|".join(TYPES)

BRANCH_WITH_TICKET = re.compile(
    rf"^({TYPE_PATTERN})/DEV-[0-9]+-[a-z0-9]+(?:-[a-z0-9]+)*$"
)
BRANCH_WITHOUT_TICKET = re.compile(
    rf"^({TYPE_PATTERN})/[a-z0-9]+(?:-[a-z0-9]+)*$"
)
TITLE_WITH_TICKET = re.compile(r"^DEV-[0-9]+: .+\S$")
TITLE_WITHOUT_TICKET = re.compile(rf"^({TYPE_PATTERN}): .+\S$")
MERGE_COMMIT = re.compile(
    r"^(Merge (branch|remote-tracking branch) .+|Merge pull request #[0-9]+ .+)$"
)


def valid_branch(value: str) -> bool:
    return bool(BRANCH_WITH_TICKET.match(value) or BRANCH_WITHOUT_TICKET.match(value))


def valid_title(value: str, allow_merge: bool) -> bool:
    return bool(
        TITLE_WITH_TICKET.match(value)
        or TITLE_WITHOUT_TICKET.match(value)
        or (allow_merge and MERGE_COMMIT.match(value))
    )


def message_for(kind: str) -> str:
    if kind == "branch":
        return (
            "Invalid branch name. Use type/DEV-1234-short-description when a ticket "
            "exists, or type/short-description without a ticket. Allowed types: "
            "feat, bugfix, chore."
        )
    return (
        "Invalid title. Use DEV-1234: short description when a ticket exists, "
        "or type: short description without a ticket. Allowed types: feat, "
        "bugfix, chore."
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("kind", choices=("branch", "commit", "pr-title"))
    parser.add_argument("value", help="Value to validate")
    args = parser.parse_args()

    value = args.value.strip()
    if args.kind == "branch":
        ok = valid_branch(value)
    else:
        ok = valid_title(value, allow_merge=args.kind == "commit")

    if ok:
        return 0

    print(message_for(args.kind), file=sys.stderr)
    print(f"Received: {value}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
