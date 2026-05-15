---
name: push-code
description: Stage all changes, auto-generate a commit message based on the diff, commit as Claude, and push to origin master. Use when the user asks to push, commit, or ship code.
argument-hint: "[optional commit message]"
---

Push all current changes to GitHub:

1. Run `git status --short` and `git diff --stat` to see what changed.
2. Run `git log --oneline -3` to match the repo's commit message style.
3. If `$ARGUMENTS` is provided, use it as the commit message. Otherwise generate a concise conventional commit message (feat/fix/refactor/chore) based on the diff — focus on the "why", not the "what".
4. Stage all changed files with `git add` (specific files, not `git add -A` blindly — exclude any .env or secrets).
5. Commit using the command below. Do NOT append any `Co-Authored-By` trailer:
   ```
   git commit --author="Claude <claude@anthropic.com>" -m "<message>"
   ```
6. Push with `git push origin master`.
7. Report the commit hash and pushed branch to the user.
