#include "state_model.h"
#include "freertos/FreeRTOS.h"
#include "freertos/semphr.h"

static telemetry_t g_t;
static SemaphoreHandle_t g_lock;

#define TMO_FAST_MS   100
#define TMO_SPEED_MS  200
#define TMO_TEMP_MS   500
#define TMO_ENERGY_MS 500
#define TMO_HB_MS     3000

void state_model_init(void) {
    g_lock = xSemaphoreCreateMutex();
    g_t = (telemetry_t){0};
}

static void lock(void){ xSemaphoreTake(g_lock, portMAX_DELAY); }
static void unlock(void){ xSemaphoreGive(g_lock); }

telemetry_t state_model_snapshot(void) {
    lock();
    telemetry_t copy = g_t;
    unlock();
    return copy;
}

void state_model_update_fast(uint16_t rpm, float current_a, uint32_t now_ms) {
    lock();
    g_t.rpm = rpm;
    g_t.motor_current_a = current_a;
    g_t.last_seen_ms_fast = now_ms;
    g_t.valid_fast = true;
    unlock();
}

void state_model_update_temp(float temp_c, uint32_t now_ms) {
    lock();
    g_t.motor_temp_c = temp_c;
    g_t.last_seen_ms_temp = now_ms;
    g_t.valid_temp = true;
    unlock();
}

void state_model_update_speed(float speed_kmh, uint32_t now_ms) {
    lock();
    g_t.vehicle_speed_kmh = speed_kmh;
    g_t.last_seen_ms_speed = now_ms;
    g_t.valid_speed = true;
    unlock();
}

void state_model_update_energy(float voltage_v, uint32_t now_ms) {
    lock();
    g_t.dc_bus_voltage_v = voltage_v;
    g_t.last_seen_ms_energy = now_ms;
    g_t.valid_energy = true;
    unlock();
}

void state_model_update_hb(uint8_t node_state, uint8_t main_error, uint32_t now_ms) {
    lock();
    g_t.node_state = node_state;
    g_t.main_error = main_error;
    g_t.last_seen_ms_hb = now_ms;
    g_t.valid_hb = true;
    unlock();
}

void state_model_apply_timeouts(uint32_t now_ms) {
    lock();
    if (g_t.valid_fast && (now_ms - g_t.last_seen_ms_fast > TMO_FAST_MS)) g_t.valid_fast = false;
    if (g_t.valid_speed && (now_ms - g_t.last_seen_ms_speed > TMO_SPEED_MS)) g_t.valid_speed = false;
    if (g_t.valid_temp && (now_ms - g_t.last_seen_ms_temp > TMO_TEMP_MS)) g_t.valid_temp = false;
    if (g_t.valid_energy && (now_ms - g_t.last_seen_ms_energy > TMO_ENERGY_MS)) g_t.valid_energy = false;
    if (g_t.valid_hb && (now_ms - g_t.last_seen_ms_hb > TMO_HB_MS)) g_t.valid_hb = false;
    unlock();
}
