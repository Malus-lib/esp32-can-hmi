# Arquitetura

## Objetivo
O ESP32-S3-LCD-7B recebe frames CAN (TWAI), faz parsing do protocolo, atualiza um modelo de estado e a HMI renderiza a partir de snapshots do estado.

## Princípios
- RX de CAN nunca deve depender do render da UI
- UI lê snapshot do estado em intervalos fixos (ex.: 50 ms)
- Timeouts invalidam sinais e evitam valores "congelados" enganosos
- Logs e contadores permitem diagnóstico (drops, bus-off, etc.)

## Diagrama de contexto
Ver `diagrams/system_context.mmd`.

## Diagrama de tasks
Ver `diagrams/firmware_tasks.mmd`.
