#include "can_driver.h"
#include <stdio.h>

#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "driver/twai.h"

#include "can/can_parser.h"
#include "state/state_model.h"
#include "util/timebase.h"

#ifndef CAN_TX_GPIO
#define CAN_TX_GPIO 20
#endif
#ifndef CAN_RX_GPIO
#define CAN_RX_GPIO 19
#endif

static TaskHandle_t s_rx_task = NULL;

static void can_rx_task(void *arg) {
    (void)arg;
    twai_message_t msg;

    while (1) {
        esp_err_t r = twai_receive(&msg, pdMS_TO_TICKS(100));
        uint32_t now = timebase_now_ms();

        if (r == ESP_OK) {
            (void)can_parser_handle(&msg, now);
        }

        state_model_apply_timeouts(now);
    }
}

void can_driver_init(void) {
    twai_general_config_t g_config = TWAI_GENERAL_CONFIG_DEFAULT(CAN_TX_GPIO, CAN_RX_GPIO, TWAI_MODE_NORMAL);
    twai_timing_config_t t_config = TWAI_TIMING_CONFIG_500KBITS();
    twai_filter_config_t f_config = TWAI_FILTER_CONFIG_ACCEPT_ALL();

    esp_err_t err = twai_driver_install(&g_config, &t_config, &f_config);
    if (err != ESP_OK) {
        printf("twai_driver_install failed: %d\n", (int)err);
        return;
    }

    err = twai_start();
    if (err != ESP_OK) {
        printf("twai_start failed: %d\n", (int)err);
        return;
    }

    printf("TWAI started (default 500kbps) TX=%d RX=%d\n", CAN_TX_GPIO, CAN_RX_GPIO);
}

void can_driver_start_tasks(void) {
    xTaskCreate(can_rx_task, "can_rx_task", 4096, NULL, 10, &s_rx_task);
}
