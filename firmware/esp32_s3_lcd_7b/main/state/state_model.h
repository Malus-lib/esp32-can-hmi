#pragma once
#include <stdint.h>
#include <stdbool.h>

typedef struct {
    uint16_t rpm;
    float motor_current_a;
    float motor_temp_c;
    float vehicle_speed_kmh;
    float dc_bus_voltage_v;

    uint8_t node_state;
    uint8_t main_error;

    uint32_t last_seen_ms_fast;
    uint32_t last_seen_ms_temp;
    uint32_t last_seen_ms_speed;
    uint32_t last_seen_ms_energy;
    uint32_t last_seen_ms_hb;

    bool valid_fast;
    bool valid_temp;
    bool valid_speed;
    bool valid_energy;
    bool valid_hb;
} telemetry_t;

void state_model_init(void);
telemetry_t state_model_snapshot(void);

void state_model_update_fast(uint16_t rpm, float current_a, uint32_t now_ms);
void state_model_update_temp(float temp_c, uint32_t now_ms);
void state_model_update_speed(float speed_kmh, uint32_t now_ms);
void state_model_update_energy(float voltage_v, uint32_t now_ms);
void state_model_update_hb(uint8_t node_state, uint8_t main_error, uint32_t now_ms);

void state_model_apply_timeouts(uint32_t now_ms);
