import time
import argparse
import can

from canbench.ids import PT_FAST, VEH_SPEED
from canbench.codec import PtFast, VehSpeed
from canbench.bus import open_bus

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--channel", default="vcan0")
    ap.add_argument("--interface", default="socketcan")
    ap.add_argument("--run_s", type=float, default=20.0)
    args = ap.parse_args()

    bus = open_bus(args.channel, args.interface)

    t0 = time.time()
    ctr = 0
    next_fast = t0
    next_speed = t0

    while time.time() - t0 < args.run_s:
        now = time.time()
        phase = (now - t0) % 7.0
        in_dropout = phase >= 5.0

        if not in_dropout:
            if now >= next_fast:
                bus.send(can.Message(arbitration_id=PT_FAST, data=PtFast(rpm=2400, motor_current_a_x10=110, counter=ctr).pack(), is_extended_id=False))
                next_fast += 0.02

            if now >= next_speed:
                bus.send(can.Message(arbitration_id=VEH_SPEED, data=VehSpeed(speed_kmh_x100=int(42.50 * 100), counter=ctr).pack(), is_extended_id=False))
                next_speed += 0.05

        ctr = (ctr + 1) & 0xFF
        time.sleep(0.001)

if __name__ == "__main__":
    main()
