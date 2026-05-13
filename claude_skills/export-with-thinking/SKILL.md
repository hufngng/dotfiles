---
name: export-with-thinking
description: Export the current conversation including Claude's thinking/reasoning blocks to a markdown file in ~/Documents/claude/export/. Use when the user wants to see Claude's internal reasoning alongside the conversation.
disable-model-invocation: true
allowed-tools: Bash(python3 *)
argument-hint: "[optional filename]"
---

Export the current conversation (with thinking blocks) to `~/Documents/claude/export/` by running the bundled script:

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/export.py ${CLAUDE_SESSION_ID} $ARGUMENTS
```

Report the output path to the user.
