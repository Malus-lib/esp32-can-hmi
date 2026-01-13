#include "ui_stub.h"
#include <stdio.h>
#include "state/state_model.h"
#include "util/timebase.h"

void ui_stub_init(void) {
    printf("UI stub init\n");
}

void ui_stub_tick(void) {
    uint32_t now = timebase_now_ms();
    telemetry_t t = state_model_snapshot();

    printf("[%u ms] RPM=%u(%d) I=%.1fA T=%.1fC SPD=%.2fkm/h V=%.2fV HB=%d state=%u err=%u\n",
           now,
           t.rpm, (int)t.valid_fast,
           t.motor_current_a,
           t.motor_temp_c,
           t.vehicle_speed_kmh,
           t.dc_bus_voltage_v,
           (int)t.valid_hb,
           (unsigned)t.node_state,
           (unsigned)t.main_error
    );
}
