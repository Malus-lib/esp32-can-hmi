import can

def open_bus(channel: str, interface: str) -> can.Bus:
    return can.interface.Bus(channel=channel, interface=interface)
