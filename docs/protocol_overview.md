# Protocolo CAN (visão geral)

Mensagens principais (IDs 11-bit):
- 0x180 PT_FAST (20ms): RPM + corrente (rápido)
- 0x181 PT_SLOW (100ms): temperatura
- 0x200 VEH_SPEED (50ms): velocidade
- 0x210 ENERGY (100ms): tensão do barramento
- 0x700 HEARTBEAT (1000ms): saúde do nó

As definições formais (escala/offset, etc.) estão em `protocol/spec/`.
