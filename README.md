# dotfiles

Personal dotfiles and config for Linux (Ubuntu) and macOS.

## Structure

```
zsh/                    Zsh configuration
  zsh.sh                Entry point — sources all files in public_config/ and private_config/
  public_config/        Committed configs (Go, Java, OpenStack aliases, Warp)
  private_config/       Git-ignored — secrets and machine-specific overrides

vim/vimrc               Vim config (~/.vim/vimrc)

docker/                 Docker install scripts for Ubuntu + cheat sheet
macos/tools.md          macOS tool setup notes (Teleport, Colima)

claude_skills/          Reusable Claude Code skills
  export-conversation/  Export current conversation to markdown
  export-with-thinking/ Export conversation including Claude's reasoning blocks
```

## Zsh setup

Source `zsh/zsh.sh` from your `.zshrc`:

```zsh
source ~/Documents/project/dotfiles/zsh/zsh.sh
```

Update `CONFIG_DIR` inside `zsh.sh` if the repo is cloned to a different path.

Private configs (tokens, env vars) go in `zsh/private_config/` — that directory is git-ignored.

## Vim setup

```bash
mkdir -p ~/.local/share/vim/undo
cp vim/vimrc ~/.vim/vimrc
```

## Docker (Ubuntu)

```bash
bash docker/install_docker.sh
```

## Claude Skills

Copy a skill folder to `~/.claude/skills/` to activate it in Claude Code:

```bash
cp -r claude_skills/export-conversation ~/.claude/skills/
cp -r claude_skills/export-with-thinking ~/.claude/skills/
```

| Skill | Command | Description |
|---|---|---|
| export-conversation | `/export-conversation` | Export conversation to markdown |
| export-with-thinking | `/export-with-thinking` | Export with Claude's reasoning blocks |

Exported files are saved to `~/Documents/claude/export/`.