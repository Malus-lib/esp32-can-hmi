import argparse
import time
from canbench.bus import open_bus

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--channel", default="vcan0")
    ap.add_argument("--interface", default="socketcan")
    ap.add_argument("--out", default="candump.log")
    args = ap.parse_args()

    bus = open_bus(args.channel, args.interface)
    t0 = time.time()

    with open(args.out, "w", encoding="utf-8") as f:
        print(f"Recording to {args.out} ... Ctrl+C to stop")
        while True:
            msg = bus.recv(timeout=1.0)
            if msg is None:
                continue
            ts = time.time() - t0
            f.write(f"{ts:.6f} 0x{msg.arbitration_id:03X} {msg.data.hex()}\n")
            f.flush()

if __name__ == "__main__":
    main()
