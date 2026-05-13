import json
import os
import sys
from datetime import datetime

session_id = sys.argv[1] if len(sys.argv) > 1 else ""
custom_name = sys.argv[2] if len(sys.argv) > 2 else ""

project_dir = os.getcwd().replace("/", "-")
base = os.path.expanduser(f"~/.claude/projects/{project_dir}")

if not os.path.isdir(base):
    print(f"No session directory: {base}")
    sys.exit(1)

session_file = os.path.join(base, f"{session_id}.jsonl") if session_id else ""
if not session_file or not os.path.exists(session_file):
    files = sorted(
        [os.path.join(base, f) for f in os.listdir(base) if f.endswith(".jsonl")],
        key=os.path.getmtime,
        reverse=True,
    )
    if not files:
        print("No session files found")
        sys.exit(1)
    session_file = files[0]
    session_id = os.path.basename(session_file).replace(".jsonl", "")

out = []
with open(session_file) as f:
    for line in f:
        entry = json.loads(line)
        if entry.get("type") not in ("user", "assistant"):
            continue
        msg = entry.get("message", {})
        role = msg.get("role", "")
        content = msg.get("content", "")
        if isinstance(content, list):
            content = "\n".join(c.get("text", "") for c in content if c.get("type") == "text")
        if role and content.strip():
            out.append(f"## {role.capitalize()}\n\n{content.strip()}\n")

export_dir = os.path.expanduser("~/Documents/claude/export")
os.makedirs(export_dir, exist_ok=True)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
project_name = os.path.basename(os.getcwd())
prefix = custom_name or f"{project_name}_{timestamp}"
filename = f"{prefix}_{session_id[:8]}.md"
output_path = os.path.join(export_dir, filename)

header = (
    f"# Conversation Export\n\n"
    f"Session: `{session_id}`  \n"
    f"Exported: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n---\n\n"
)
with open(output_path, "w") as f:
    f.write(header + "\n---\n\n".join(out))

print(f"✅ {len(out)} messages saved to {output_path}")