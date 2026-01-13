#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/../esp32_s3_lcd_7b"
idf.py flash
