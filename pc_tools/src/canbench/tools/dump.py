import argparse
from canbench.bus import open_bus

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--channel", default="vcan0")
    ap.add_argument("--interface", default="socketcan")
    args = ap.parse_args()

    bus = open_bus(args.channel, args.interface)
    print(f"Listening on {args.interface}:{args.channel} ... Ctrl+C to stop")

    while True:
        msg = bus.recv(timeout=1.0)
        if msg is None:
            continue
        print(f"ID=0x{msg.arbitration_id:03X} DLC={msg.dlc} DATA={msg.data.hex()}")

if __name__ == "__main__":
    main()
