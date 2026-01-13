#!/usr/bin/env bash
set -euo pipefail

sudo modprobe vcan
sudo ip link add dev vcan0 type vcan 2>/dev/null || true
sudo ip link set up vcan0

echo "vcan0 is up:"
ip -details link show vcan0
