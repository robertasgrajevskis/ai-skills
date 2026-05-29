---
name: git-workflow-policy
description: Follow and enforce the team's Git workflow for branch names, commit messages, PR titles/descriptions, branch updates, reviews, signed commits, push safety, and squash merges. Use when Codex works with Git branches, commits, pull requests, code reviews, branch synchronization, merge preparation, release cleanup, or repository hook setup.
---

# Git Workflow Policy

Use this skill whenever Git workflow decisions affect branch names, commit messages, pull requests, reviews, pushes, or merge preparation.

## Required Conventions

- Use `feat` for new features.
- Use `bugfix` for bug fixes.
- Use `chore` for tooling, config, cleanup, dependency bumps, refactoring, tests, and docs.
- Include a ClickUp ticket ID when one exists.
- Use short, clear descriptions in lowercase kebab-case for branch descriptions.
- Sign commits when committing.
- Never force push unless the user explicitly overrides this policy.
- Update feature branches by pulling the main branch and merging `origin/main` into the feature branch.
- Use squash merge only for PRs.

## Branch Names

- With ticket: `type/DEV-1234-short-description`
- Without ticket: `type/short-description`

Valid examples:

```text
feat/DEV-3333-warranty-toggle
bugfix/DEV-1201-price-rounding
chore/DEV-999-clean-checkout-state
chore/clean-checkout-state
```

Invalid examples:

```text
feature/DEV-3333-warranty-toggle
feat/dev-3333-warranty-toggle
feat/DEV-3333 Warranty Toggle
```

## Commit Messages And PR Titles

- With ticket: `DEV-1234: short description`
- Without ticket: `type: short description`
- Keep the summary imperative and specific.
- Allow ordinary merge commit messages created while merging `origin/main`.

Valid examples:

```text
DEV-3333: add warranty toggle
DEV-1202: correct total calculation
DEV-3331: simplify response handling
chore: clean checkout state
```

Invalid examples:

```text
add warranty toggle
DEV3333: add warranty toggle
feat add warranty toggle
```

## Pull Requests

- Use the same format as commit messages for PR titles.
- Prefer the template:

```markdown
## Ticket
DEV-1234

## What
What was implemented.

## How to test
1.
2.
3.

## Notes
Anything important for reviewers.
```

- Keep PRs as drafts until they are built, tested, and ready for review when repository tooling supports draft PRs.
- Require at least one approval before merge.
- Merge using squash merge only.

## Branch Update Workflow

Use this sequence when updating a feature branch:

```bash
git switch main
git pull
git switch <feature-branch>
git merge origin/main
```

Resolve conflicts carefully. Do not overwrite changes that are not understood. Build and test after the merge, then commit the merge result and push normally.

## Code Review Comments

Use Conventional Comments labels when writing review feedback:

- `nitpick:` for minor non-blocking issues.
- `suggestion:` for improvement ideas.
- `question:` for clarification requests.
- `issue:` for definite problems that should be fixed.

## Validation Script

Use `scripts/validate_git_policy.py` to validate branch names, commit messages, and PR titles:

```bash
python3 /path/to/git-workflow-policy/scripts/validate_git_policy.py branch feat/DEV-3333-warranty-toggle
python3 /path/to/git-workflow-policy/scripts/validate_git_policy.py commit "DEV-3333: add warranty toggle"
python3 /path/to/git-workflow-policy/scripts/validate_git_policy.py pr-title "chore: clean checkout state"
```

## Hook Installer

Use `scripts/install_git_hooks.py` when the user asks to install, set up, enable, or enforce this Git policy in a repository.

Run it from the target repo:

```bash
python3 /path/to/git-workflow-policy/scripts/install_git_hooks.py
```

Or pass an explicit repo path:

```bash
python3 /path/to/git-workflow-policy/scripts/install_git_hooks.py --repo /path/to/repo
```

The installer:

- Creates `.githooks/commit-msg`.
- Creates `.githooks/pre-push`.
- Copies `validate_git_policy.py` into `.githooks/` so the installed hooks are repo-local.
- Runs `git config core.hooksPath .githooks`.
- Refuses to overwrite existing managed files unless `--force` is passed.

The installed `commit-msg` hook validates the first line of each commit message. The installed `pre-push` hook validates pushed branch names and rejects non-fast-forward pushes.
