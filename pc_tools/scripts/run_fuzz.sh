#!/usr/bin/env bash
set -euo pipefail
source .venv/bin/activate
python -m canbench.scenarios.fuzz_invalid --channel vcan0 --interface socketcan
