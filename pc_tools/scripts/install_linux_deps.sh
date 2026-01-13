#!/usr/bin/env bash
set -euo pipefail

if command -v apt-get >/dev/null 2>&1; then
  sudo apt-get update
  sudo apt-get install -y can-utils iproute2
else
  echo "Unsupported distro. Install can-utils and iproute2 manually."
  exit 1
fi

echo "Installed can-utils and iproute2."
