# Encode/Decode Examples

## PT_FAST (0x180)
- rpm: uint16 little-endian
- motor_current: int16 little-endian, scale 0.1 A/LSB

Exemplo:
- rpm = 2500 -> 0xC4 0x09
- current = 12.3 A -> 123 -> 0x7B 0x00

Frame (8 bytes):
[ C4 09  7B 00  00 00  00  01 ]
