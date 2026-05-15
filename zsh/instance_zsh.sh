#!/bin/bash
set -e

# Install zsh and oh-my-zsh dependencies
sudo apt-get update
sudo apt-get install -y zsh git curl

# Install oh-my-zsh (unattended)
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended

ZSH_CUSTOM="${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}"

# Install zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-autosuggestions \
  $ZSH_CUSTOM/plugins/zsh-autosuggestions

# Install zsh-syntax-highlighting
git clone https://github.com/zsh-users/zsh-syntax-highlighting \
  $ZSH_CUSTOM/plugins/zsh-syntax-highlighting

# Enable plugins in .zshrc
sed -i 's/^plugins=(git)/plugins=(git zsh-autosuggestions zsh-syntax-highlighting)/' ~/.zshrc

# Set zsh as default shell
chsh -s $(which zsh)

echo "Done. Restart terminal or run: zsh"

