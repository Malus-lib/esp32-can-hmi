#!/usr/bin/env bash
set -euo pipefail

BUS="${1:-vcan0}"
LOG="${2:-run.log}"

source .venv/bin/activate
python -m canbench.tools.replay --channel "${BUS}" --interface socketcan --log "${LOG}" --speed 1.0
