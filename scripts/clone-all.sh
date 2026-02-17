#!/usr/bin/env bash
# Clone all Humans Not Required service repos as siblings of this repo.
# Run from the humans-not-required directory.
#
# Usage:
#   ./scripts/clone-all.sh
#   ./scripts/clone-all.sh --ssh   # Use SSH instead of HTTPS

set -euo pipefail

ORG="Humans-Not-Required"
REPOS=(
  qr-service
  kanban
  app-directory
  blog
  agent-docs
  local-agent-chat
  watchpost
  private-dashboard
)

PARENT_DIR="$(cd "$(dirname "$0")/../.." && pwd)"
USE_SSH=false

if [[ "${1:-}" == "--ssh" ]]; then
  USE_SSH=true
fi

echo "Cloning into: $PARENT_DIR"
echo ""

for repo in "${REPOS[@]}"; do
  target="$PARENT_DIR/$repo"
  if [[ -d "$target" ]]; then
    echo "✓ $repo (already exists)"
  else
    if $USE_SSH; then
      url="git@github.com:${ORG}/${repo}.git"
    else
      url="https://github.com/${ORG}/${repo}.git"
    fi
    echo "⬇ Cloning $repo..."
    git clone "$url" "$target"
    echo "✓ $repo"
  fi
done

echo ""
echo "All repos cloned. Build with:"
echo "  docker compose -f docker-compose.yml -f docker-compose.build.yml up -d --build"
