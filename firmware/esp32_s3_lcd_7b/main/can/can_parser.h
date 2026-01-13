#pragma once
#include <stdint.h>
#include <stdbool.h>
#include "driver/twai.h"

bool can_parser_handle(const twai_message_t *msg, uint32_t now_ms);
