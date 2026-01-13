#!/usr/bin/env bash
set -euo pipefail
source .venv/bin/activate
python -m canbench.scenarios.dropouts --channel vcan0 --interface socketcan
