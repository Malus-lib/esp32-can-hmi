from canbench.codec import PtFast, decode_u16_le, decode_i16_le

def test_ptfast_pack_layout():
    msg = PtFast(rpm=2500, motor_current_a_x10=123, flags=0xAA, counter=0x55).pack()
    assert len(msg) == 8
    assert decode_u16_le(msg[0:2]) == 2500
    assert decode_i16_le(msg[2:4]) == 123
    assert msg[6] == 0xAA
    assert msg[7] == 0x55
