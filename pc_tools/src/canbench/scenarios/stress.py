import time
import argparse
import can
import random

from canbench.ids import PT_FAST, PT_SLOW, VEH_SPEED, ENERGY
from canbench.codec import PtFast, PtSlow, VehSpeed, Energy
from canbench.bus import open_bus

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--channel", default="vcan0")
    ap.add_argument("--interface", default="socketcan")
    ap.add_argument("--duration_s", type=float, default=10.0)
    args = ap.parse_args()

    bus = open_bus(args.channel, args.interface)

    t0 = time.time()
    ctr = 0

    while time.time() - t0 < args.duration_s:
        rpm = random.randint(0, 8000)
        cur = random.randint(-500, 1500)
        spd = random.randint(0, 20000)
        vdc = random.randint(0, 8000)
        tmp = random.randint(-200, 1200)

        bus.send(can.Message(arbitration_id=PT_FAST, data=PtFast(rpm=rpm, motor_current_a_x10=cur, counter=ctr).pack(), is_extended_id=False))
        bus.send(can.Message(arbitration_id=VEH_SPEED, data=VehSpeed(speed_kmh_x100=spd, counter=ctr).pack(), is_extended_id=False))
        bus.send(can.Message(arbitration_id=ENERGY, data=Energy(dc_bus_v_x100=vdc, counter=ctr).pack(), is_extended_id=False))
        bus.send(can.Message(arbitration_id=PT_SLOW, data=PtSlow(motor_temp_c_x10=tmp, counter=ctr).pack(), is_extended_id=False))

        ctr = (ctr + 1) & 0xFF
        time.sleep(0.001)

if __name__ == "__main__":
    main()
