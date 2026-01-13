SHELL := /bin/bash

BUS ?= vcan0
OUT ?= run.log
LOG ?= run.log

.PHONY: help linux-deps vcan pc-venv pc-test run-nominal run-stress run-dropouts run-fuzz record replay

help:
	@echo "Targets:"
	@echo "  make linux-deps       Install Linux deps (can-utils, iproute2)"
	@echo "  make vcan             Setup vcan0 interface"
	@echo "  make pc-venv          Create venv + install pc_tools deps"
	@echo "  make pc-test          Run Python tests"
	@echo "  make run-nominal      Run nominal scenario on BUS=$(BUS)"
	@echo "  make run-stress       Run stress scenario on BUS=$(BUS)"
	@echo "  make run-dropouts     Run dropouts scenario on BUS=$(BUS)"
	@echo "  make run-fuzz         Run fuzz scenario on BUS=$(BUS)"
	@echo "  make record           Record candump to OUT=$(OUT) from BUS=$(BUS)"
	@echo "  make replay           Replay LOG=$(LOG) into BUS=$(BUS)"

linux-deps:
	@cd pc_tools && ./scripts/install_linux_deps.sh

vcan:
	@cd pc_tools && ./scripts/setup_vcan.sh

pc-venv:
	@cd pc_tools && python3 -m venv .venv
	@cd pc_tools && source .venv/bin/activate && python -m pip install --upgrade pip
	@cd pc_tools && source .venv/bin/activate && pip install -r requirements.txt

pc-test:
	@cd pc_tools && source .venv/bin/activate && pytest -q

run-nominal:
	@cd pc_tools && source .venv/bin/activate && python -m canbench.scenarios.nominal --channel $(BUS) --interface socketcan

run-stress:
	@cd pc_tools && source .venv/bin/activate && python -m canbench.scenarios.stress --channel $(BUS) --interface socketcan

run-dropouts:
	@cd pc_tools && source .venv/bin/activate && python -m canbench.scenarios.dropouts --channel $(BUS) --interface socketcan

run-fuzz:
	@cd pc_tools && source .venv/bin/activate && python -m canbench.scenarios.fuzz_invalid --channel $(BUS) --interface socketcan

record:
	@cd pc_tools && ./scripts/record_bus.sh $(BUS) $(OUT)

replay:
	@cd pc_tools && source .venv/bin/activate && python -m canbench.tools.replay --channel $(BUS) --interface socketcan --log $(LOG) --speed 1.0
