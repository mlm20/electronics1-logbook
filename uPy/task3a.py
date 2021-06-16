# task3a.py

import time
from machine import Pin
from oled import OLED
from rotary_irq_esp import RotaryIRQ

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
        oled.draw_text(32, 32, "{:4d}".format(val_new), size = 2, space = 2)
        oled.display()
        time.sleep_ms(20)
