# esp32-can-hmi (ESP32-S3-LCD-7B)

Repositório de referência para:
- Definir e versionar um protocolo CAN (spec + DBC opcional)
- Simular e testar tráfego CAN via PC (Linux + SocketCAN + Python)
- Firmware ESP-IDF para ESP32-S3 (TWAI/CAN RX + parser + state model + UI stub/LVGL)

## Estrutura
- `protocol/`: fonte de verdade do protocolo (IDs, payloads, escalas, timeouts)
- `pc_tools/`: simuladores de nós e cenários (nominal/stress/dropouts/fuzz)
- `firmware/`: projeto ESP-IDF (TWAI RX, parser e base da HMI)
- `docs/`: arquitetura e diagramas

## Quick start (Linux)
### 1) Instalar dependências do sistema (SocketCAN tools)
```bash
make linux-deps
```

### 2) Subir CAN virtual (vcan0)
```bash
make vcan
```

### 3) Criar venv e instalar deps Python
```bash
make pc-venv
```

### 4) Rodar cenário nominal
```bash
make run-nominal
```

### 5) Rodar stress / dropouts / fuzz
```bash
make run-stress
make run-dropouts
make run-fuzz
```

### 6) Gravar tráfego e reproduzir
```bash
make record BUS=vcan0 OUT=run.log
make replay BUS=vcan0 LOG=run.log
```

## Firmware (ESP-IDF)
Veja `firmware/README.md`.

## Licença
MIT (veja `LICENSE`).
