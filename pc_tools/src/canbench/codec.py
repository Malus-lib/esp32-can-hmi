from dataclasses import dataclass

def u16_le(x: int) -> bytes:
    return int(x).to_bytes(2, "little", signed=False)

def i16_le(x: int) -> bytes:
    return int(x).to_bytes(2, "little", signed=True)

def clamp_int(x: int, lo: int, hi: int) -> int:
    return lo if x < lo else hi if x > hi else x

@dataclass
class PtFast:
    rpm: int
    motor_current_a_x10: int  # corrente * 10
    flags: int = 0
    counter: int = 0

    def pack(self) -> bytes:
        data = bytearray(8)
        data[0:2] = u16_le(clamp_int(self.rpm, 0, 65535))
        data[2:4] = i16_le(clamp_int(self.motor_current_a_x10, -32768, 32767))
        data[6] = self.flags & 0xFF
        data[7] = self.counter & 0xFF
        return bytes(data)

@dataclass
class PtSlow:
    motor_temp_c_x10: int
    flags: int = 0
    counter: int = 0

    def pack(self) -> bytes:
        data = bytearray(8)
        data[0:2] = i16_le(clamp_int(self.motor_temp_c_x10, -32768, 32767))
        data[6] = self.flags & 0xFF
        data[7] = self.counter & 0xFF
        return bytes(data)

@dataclass
class VehSpeed:
    speed_kmh_x100: int
    flags: int = 0
    counter: int = 0

    def pack(self) -> bytes:
        data = bytearray(8)
        data[0:2] = u16_le(clamp_int(self.speed_kmh_x100, 0, 65535))
        data[4] = self.flags & 0xFF
        data[7] = self.counter & 0xFF
        return bytes(data)

@dataclass
class Energy:
    dc_bus_v_x100: int
    flags: int = 0
    counter: int = 0

    def pack(self) -> bytes:
        data = bytearray(8)
        data[0:2] = u16_le(clamp_int(self.dc_bus_v_x100, 0, 65535))
        data[4] = self.flags & 0xFF
        data[7] = self.counter & 0xFF
        return bytes(data)

@dataclass
class Heartbeat:
    node_state: int
    main_error: int
    uptime_s: int
    proto_ver: int = 1
    fw_ver: int = 1

    def pack(self) -> bytes:
        data = bytearray(8)
        data[0] = self.node_state & 0xFF
        data[1] = self.main_error & 0xFF
        data[2:4] = u16_le(clamp_int(self.uptime_s, 0, 65535))
        data[4] = self.proto_ver & 0xFF
        data[5:7] = u16_le(clamp_int(self.fw_ver, 0, 65535))
        data[7] = 0
        return bytes(data)

def decode_u16_le(b: bytes) -> int:
    return int.from_bytes(b, "little", signed=False)

def decode_i16_le(b: bytes) -> int:
    return int.from_bytes(b, "little", signed=True)
