import time
import argparse
import can
import random

from canbench.bus import open_bus

VALID_IDS = [0x180, 0x181, 0x200, 0x210, 0x700]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--channel", default="vcan0")
    ap.add_argument("--interface", default="socketcan")
    ap.add_argument("--duration_s", type=float, default=10.0)
    args = ap.parse_args()

    bus = open_bus(args.channel, args.interface)

    t0 = time.time()
    while time.time() - t0 < args.duration_s:
        kind = random.choice(["bad_id", "bad_dlc", "random_payload"])

        if kind == "bad_id":
            arb_id = random.randint(0x001, 0x7FF)
            while arb_id in VALID_IDS:
                arb_id = random.randint(0x001, 0x7FF)
            data = bytes([random.randint(0, 255) for _ in range(8)])
            bus.send(can.Message(arbitration_id=arb_id, data=data, is_extended_id=False))

        elif kind == "bad_dlc":
            arb_id = random.choice(VALID_IDS)
            dlc = random.choice([0, 1, 2, 3, 4, 5, 6, 7])
            data = bytes([random.randint(0, 255) for _ in range(dlc)])
            bus.send(can.Message(arbitration_id=arb_id, data=data, is_extended_id=False))

        else:
            arb_id = random.choice(VALID_IDS)
            data = bytes([random.randint(0, 255) for _ in range(8)])
            bus.send(can.Message(arbitration_id=arb_id, data=data, is_extended_id=False))

        time.sleep(0.01)

if __name__ == "__main__":
    main()
