#!/usr/bin/env bash
set -euo pipefail

BUS="${1:-vcan0}"
OUT="${2:-run.log}"

echo "Recording candump from ${BUS} to ${OUT} ..."
candump -tz "${BUS}" | tee "${OUT}"
