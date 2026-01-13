import time
import argparse
import can

from canbench.ids import PT_FAST, PT_SLOW, VEH_SPEED, ENERGY, HEARTBEAT
from canbench.codec import PtFast, PtSlow, VehSpeed, Energy, Heartbeat
from canbench.bus import open_bus

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--channel", default="vcan0")
    ap.add_argument("--interface", default="socketcan")
    args = ap.parse_args()

    bus = open_bus(args.channel, args.interface)

    t0 = time.time()
    ctr = 0

    next_fast = t0
    next_speed = t0
    next_slow = t0
    next_energy = t0
    next_hb = t0

    while True:
        now = time.time()

        if now >= next_fast:
            msg = can.Message(arbitration_id=PT_FAST, data=PtFast(rpm=2500, motor_current_a_x10=123, counter=ctr).pack(), is_extended_id=False)
            bus.send(msg)
            next_fast += 0.02

        if now >= next_speed:
            msg = can.Message(arbitration_id=VEH_SPEED, data=VehSpeed(speed_kmh_x100=int(35.67 * 100), counter=ctr).pack(), is_extended_id=False)
            bus.send(msg)
            next_speed += 0.05

        if now >= next_slow:
            msg = can.Message(arbitration_id=PT_SLOW, data=PtSlow(motor_temp_c_x10=int(62.3 * 10), counter=ctr).pack(), is_extended_id=False)
            bus.send(msg)
            next_slow += 0.10

        if now >= next_energy:
            msg = can.Message(arbitration_id=ENERGY, data=Energy(dc_bus_v_x100=int(52.34 * 100), counter=ctr).pack(), is_extended_id=False)
            bus.send(msg)
            next_energy += 0.10

        if now >= next_hb:
            uptime = int(now - t0)
            msg = can.Message(arbitration_id=HEARTBEAT, data=Heartbeat(node_state=1, main_error=0, uptime_s=uptime).pack(), is_extended_id=False)
            bus.send(msg)
            next_hb += 1.0

        ctr = (ctr + 1) & 0xFF
        time.sleep(0.001)

if __name__ == "__main__":
    main()
