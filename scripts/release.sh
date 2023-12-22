#!/usr/bin/env bash
set -e

TAG=$(python -c 'from src.splatbot import __version__; print("v" + __version__)')

read -p "Creating new release for $TAG. Do you want to continue? [Y/n] " prompt

if [[ $prompt == "y" || $prompt == "Y" || $prompt == "yes" || $prompt == "Yes" ]]; then
    python scripts/prepare_changelog.py
    git add -A
    git commit -m "build: release $TAG" || true && git push
    echo "Creating new git tag $TAG."
    git tag "$TAG" -m "$TAG"
    git push --tags
else
    echo "Cancelled."
    exit 1
fi
# git tag -l | xargs git tag -d && git fetch -t
