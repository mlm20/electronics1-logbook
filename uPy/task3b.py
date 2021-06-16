# task3b.py

import time
from machine import Pin, PWM
from oled import OLED
from rotary_irq_esp import RotaryIRQ

rLED = PWM(Pin(33), freq = 1000)
gLED = PWM(Pin(32), freq = 1000)

oled = OLED()
oled.init_display()

r = RotaryIRQ(
        pin_num_clk = 23,
        pin_num_dt = 19,
        min_val = -100,
        max_val = 100,
        reverse = True,
        range_mode = RotaryIRQ.RANGE_BOUNDED
)

val_old = r.value()

while True:
    val_new = r.value()

    if val_old != val_new:
        val_old = val_new
        oled.draw_text(
            32, 32, "{:4d}".format(val_new), size = 2, space = 2
        )
        oled.display()
        rLED.duty(val_new)
        gLED.duty(val_new)
        time.sleep_ms(20)
