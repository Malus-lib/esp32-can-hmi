import argparse
import time
import can
from canbench.bus import open_bus

def parse_line(line: str):
    parts = line.strip().split()
    if len(parts) < 3:
        return None
    ts = float(parts[0])
    arb = int(parts[1], 16)
    data = bytes.fromhex(parts[2])
    return ts, arb, data

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--channel", default="vcan0")
    ap.add_argument("--interface", default="socketcan")
    ap.add_argument("--log", required=True)
    ap.add_argument("--speed", type=float, default=1.0, help="1.0 = real time; 2.0 = 2x faster")
    args = ap.parse_args()

    bus = open_bus(args.channel, args.interface)

    with open(args.log, "r", encoding="utf-8") as f:
        lines = [ln for ln in f if ln.strip() and not ln.strip().startswith("#")]

    events = []
    for ln in lines:
        parsed = parse_line(ln)
        if parsed:
            events.append(parsed)

    if not events:
        raise SystemExit("No events found in log.")

    t_start = time.time()
    base_ts = events[0][0]

    for ts, arb, data in events:
        target = (ts - base_ts) / max(args.speed, 1e-6)
        while (time.time() - t_start) < target:
            time.sleep(0.0005)
        bus.send(can.Message(arbitration_id=arb, data=data, is_extended_id=False))

    print("Replay done.")

if __name__ == "__main__":
    main()
