---
name: export-conversation
description: Export the current conversation to a markdown file in ~/Documents/claude/export/. Use when the user asks to export, save, or download the conversation.
disable-model-invocation: true
allowed-tools: Bash(python3 *)
argument-hint: "[optional filename]"
---

Export the current conversation to `~/Documents/claude/export/` by running the bundled script:

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/export.py ${CLAUDE_SESSION_ID} $ARGUMENTS
```

Report the output path to the user.