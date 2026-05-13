# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A personal dotfiles collection for Linux (Ubuntu) and macOS. There is no build system, test suite, or install script — files are manually symlinked or sourced from their target locations.

## Structure

- **zsh/** — Zsh configuration. `zsh.sh` is the main entry point; it auto-sources every file under `public_config/` (committed) and `private_config/` (git-ignored, for secrets/private env vars).
- **vim/vimrc** — Standalone Vim config. Intended to live at `~/.vim/vimrc`.
- **docker/** — Install scripts for Docker on Ubuntu (`install_docker.sh`, `install_docker_compose.sh`) and reference markdown.
- **macos/** — macOS tool setup notes (Teleport, Colima-based Docker CLI).

## Key conventions

- `zsh/public_config/` holds self-contained `.sh`/`.zsh` snippets. Each file sets up one concern (Go paths, Java version switching, Warp aliases, OpenStack aliases). Add new topics as separate files here.
- `zsh/private_config/` is git-ignored — put secrets, tokens, and machine-specific overrides there, never in `public_config/`.
- The `zsh.sh` loader uses `CONFIG_DIR` hardcoded to `/home/hungnv/Documents/project/github/dotfiles/zsh` — update that path if the repo moves.
- Undo persistence for Vim requires `mkdir -p ~/.local/share/vim/undo` on first use.

## Java version switching (zsh/public_config/java.sh)

Three aliases switch the active JDK and prepend Maven 3.6.3:
- `Java11` — system OpenJDK 11
- `Java17` — `~/Documents/thirdparty/jdk-17.0.11`
- `Java21` — `~/Documents/thirdparty/jdk-21.0.8`

Default is Java11 (set at the bottom of the file).

## Go path (zsh/public_config/go.sh)

`GOROOT` points to `~/Documents/thirdparty/go-lib/go1.22.4.linux-amd64/go`. Update this file when upgrading Go versions.
