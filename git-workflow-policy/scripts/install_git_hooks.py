#!/usr/bin/env python3
"""Install Git workflow policy hooks into the current repository."""

from __future__ import annotations

import argparse
import os
import shutil
import stat
import subprocess
import sys
from pathlib import Path

COMMIT_MSG_HOOK = """#!/bin/sh
set -eu

HOOK_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
SUBJECT="$(sed -n '1p' "$1")"

python3 "$HOOK_DIR/validate_git_policy.py" commit "$SUBJECT"
"""

PRE_PUSH_HOOK = """#!/bin/sh
set -eu

HOOK_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
ZERO_SHA="0000000000000000000000000000000000000000"
status=0

while read local_ref local_sha remote_ref remote_sha
do
  case "$local_ref" in
    refs/heads/*)
      branch="${local_ref#refs/heads/}"
      if ! python3 "$HOOK_DIR/validate_git_policy.py" branch "$branch"; then
        status=1
      fi

      if [ "$remote_sha" != "$ZERO_SHA" ] && [ "$local_sha" != "$ZERO_SHA" ]; then
        if ! git merge-base --is-ancestor "$remote_sha" "$local_sha"; then
          echo "Push rejected: non-fast-forward push detected. Never force push." >&2
          status=1
        fi
      fi
      ;;
  esac
done

exit "$status"
"""


def run_git(args: list[str], cwd: Path) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=cwd,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return result.stdout.strip()


def make_executable(path: Path) -> None:
    mode = path.stat().st_mode
    path.chmod(mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)


def write_file(path: Path, content: str, force: bool) -> None:
    if path.exists() and not force:
        raise FileExistsError(
            f"{path} already exists. Re-run with --force to overwrite it."
        )
    path.write_text(content, encoding="utf-8")
    make_executable(path)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--repo",
        default=".",
        help="Repository path where hooks should be installed. Defaults to cwd.",
    )
    parser.add_argument(
        "--hooks-dir",
        default=".githooks",
        help="Repo-relative hooks directory. Defaults to .githooks.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing managed hook files.",
    )
    args = parser.parse_args()

    repo_arg = Path(args.repo).expanduser().resolve()
    try:
        repo_root = Path(run_git(["rev-parse", "--show-toplevel"], repo_arg))
    except subprocess.CalledProcessError as exc:
        print(f"Not a Git repository: {repo_arg}", file=sys.stderr)
        print(exc.stderr.strip(), file=sys.stderr)
        return 1

    hooks_dir = repo_root / args.hooks_dir
    hooks_dir.mkdir(parents=True, exist_ok=True)

    script_dir = Path(__file__).resolve().parent
    validator_source = script_dir / "validate_git_policy.py"
    validator_target = hooks_dir / "validate_git_policy.py"

    if validator_target.exists() and not args.force:
        print(
            f"{validator_target} already exists. Re-run with --force to overwrite it.",
            file=sys.stderr,
        )
        return 1

    shutil.copy2(validator_source, validator_target)
    make_executable(validator_target)

    try:
        write_file(hooks_dir / "commit-msg", COMMIT_MSG_HOOK, args.force)
        write_file(hooks_dir / "pre-push", PRE_PUSH_HOOK, args.force)
    except FileExistsError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    run_git(["config", "core.hooksPath", args.hooks_dir], repo_root)

    print(f"Installed Git workflow hooks in {repo_root}")
    print(f"Configured core.hooksPath={args.hooks_dir}")
    print("Installed hooks: commit-msg, pre-push")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
