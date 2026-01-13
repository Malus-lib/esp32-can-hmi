# firmware

Firmware ESP-IDF para ESP32-S3 (ESP32-S3-LCD-7B).

## O que já existe
- TWAI RX task
- parser para mensagens do protocolo (IDs 0x180/0x181/0x200/0x210/0x700)
- state model com valid flags e last_seen + timeouts
- UI stub (printa snapshot periodicamente)

## Pré-requisitos
- ESP-IDF 5.x instalado
- `idf.py` no PATH

## Build/Flash/Monitor
```bash
cd firmware/esp32_s3_lcd_7b
idf.py set-target esp32s3
idf.py menuconfig
idf.py build
idf.py flash monitor
```

## Notas de hardware (CAN)
Ajuste os pinos `CAN_TX_GPIO` e `CAN_RX_GPIO` em `main/can/can_driver.c` conforme a sua placa.
