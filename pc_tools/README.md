# pc_tools

Ferramentas de PC para simular tráfego CAN usando SocketCAN.

## Requisitos
- Linux
- can-utils
- Python 3.10+

## Setup
```bash
./scripts/install_linux_deps.sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
./scripts/setup_vcan.sh
```

## Cenários
- nominal: tráfego normal
- stress: alta carga e bursts
- dropouts: simula perda de mensagens / pausas
- fuzz_invalid: injeta frames inválidos (DLC e IDs inesperados)

Rodar:
```bash
./scripts/run_nominal.sh
./scripts/run_stress.sh
./scripts/run_dropouts.sh
./scripts/run_fuzz.sh
```

## Record / Replay
```bash
./scripts/record_bus.sh vcan0 run.log
./scripts/replay_log.sh vcan0 run.log
```
