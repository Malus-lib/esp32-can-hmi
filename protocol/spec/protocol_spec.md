# CAN Protocol Specification

## Link layer
- CAN 2.0
- Standard ID (11-bit)
- Bitrate: TBD (default 500 kbps)
- Endianness: little-endian for multi-byte fields

## Timeouts (HMI)
- PT_FAST: 100 ms
- VEH_SPEED: 200 ms
- PT_SLOW: 500 ms
- ENERGY: 500 ms
- HEARTBEAT: 3000 ms

## Messages
See `message_matrix.csv` and `signals.csv`.
