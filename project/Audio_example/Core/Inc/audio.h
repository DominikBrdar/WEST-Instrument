#include <stdlib.h>
#include "i2c.h"
#include "i2s.h"
#include "gpio.h"

extern int16_t sine_table[];
//extern uint16_t sine_table[];

#define AUDIO_RESET_PIN GPIO_PIN_4
#define AUDIO_I2C_ADDRESS 0x94

void configAudio();
void init_AudioReset();
