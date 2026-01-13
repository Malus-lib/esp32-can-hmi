#include "can_parser.h"
#include "state/state_model.h"

static uint16_t u16_le(const uint8_t *p) {
    return (uint16_t)p[0] | ((uint16_t)p[1] << 8);
}
static int16_t i16_le(const uint8_t *p) {
    return (int16_t)((uint16_t)p[0] | ((uint16_t)p[1] << 8));
}

bool can_parser_handle(const twai_message_t *msg, uint32_t now_ms) {
    if (!msg) return false;
    if (msg->extd) return false;
    if (msg->data_length_code != 8) return false;

    const uint32_t id = msg->identifier;
    const uint8_t *d = msg->data;

    switch (id) {
        case 0x180: {
            uint16_t rpm = u16_le(&d[0]);
            int16_t cur_x10 = i16_le(&d[2]);
            float cur_a = ((float)cur_x10) / 10.0f;
            state_model_update_fast(rpm, cur_a, now_ms);
            return true;
        }
        case 0x181: {
            int16_t tmp_x10 = i16_le(&d[0]);
            float tmp_c = ((float)tmp_x10) / 10.0f;
            state_model_update_temp(tmp_c, now_ms);
            return true;
        }
        case 0x200: {
            uint16_t spd_x100 = u16_le(&d[0]);
            float spd = ((float)spd_x100) / 100.0f;
            state_model_update_speed(spd, now_ms);
            return true;
        }
        case 0x210: {
            uint16_t v_x100 = u16_le(&d[0]);
            float v = ((float)v_x100) / 100.0f;
            state_model_update_energy(v, now_ms);
            return true;
        }
        case 0x700: {
            uint8_t node_state = d[0];
            uint8_t main_error = d[1];
            state_model_update_hb(node_state, main_error, now_ms);
            return true;
        }
        default:
            return false;
    }
}
