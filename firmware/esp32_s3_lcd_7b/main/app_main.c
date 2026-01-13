#include <stdio.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"

#include "can/can_driver.h"
#include "state/state_model.h"
#include "ui/ui_stub.h"

void app_main(void)
{
    printf("ESP32-S3 CAN HMI starting...\n");

    state_model_init();
    ui_stub_init();

    can_driver_init();
    can_driver_start_tasks();

    while (1) {
        ui_stub_tick();
        vTaskDelay(pdMS_TO_TICKS(200));
    }
}
