# Lab 4b - ESP32, Sensors, Drivers

## Task 1

The LEDs were installed as instructed. They lit up and PWM was used to alter their brightness.

![](C:\Users\MaxLM\OneDrive\Documents\University\DE1\Electronics 1\electronics1-logbook\media\IMG_20210616_172809.jpg)

![](C:\Users\MaxLM\OneDrive\Documents\University\DE1\Electronics 1\electronics1-logbook\media\IMG_20210616_172818.jpg)

I rewrote the varying brightness program `task1.py` in the editor and flashed it to ESP32. It worked as expected.

## Task 2

The code from Step 1 was tested.

For step 2 I wrote the following code in `task2a.py`, it functioned as expected.

```python
# uses the switch to turn on and off the rLED
from machine import Pin

rLED = Pin(33, Pin.OUT)
button = Pin(22, Pin.IN, Pin.PULL_UP)

while True: # loop forever
    if button.value() == 0:
        rLED.on()
    elif button.value() == 1:
        rLED.off()
```

![](C:\Users\MaxLM\OneDrive\Documents\University\DE1\Electronics 1\electronics1-logbook\media\IMG_20210616_175625.jpg)

![](C:\Users\MaxLM\OneDrive\Documents\University\DE1\Electronics 1\electronics1-logbook\media\IMG_20210616_175629.jpg)

In Step 3 the provided script was flashed onto the ESP32 and it yielded the expected results.

![](C:\Users\MaxLM\OneDrive\Documents\University\DE1\Electronics 1\electronics1-logbook\media\IMG_20210616_181316.jpg)

However when the capacitor was removed no “contact bounce” was noted, it acted the same as before.

## Task 3

For steps 1 and 2 the files were coppied and transcribed respectively. The program was flashed and worked as expected.

![](C:\Users\MaxLM\OneDrive\Documents\University\DE1\Electronics 1\electronics1-logbook\media\IMG_20210616_183854.jpg)

In Step 4 `task3b.py` was altered to be the following code:

```python
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

```

![](C:\Users\MaxLM\OneDrive\Documents\University\DE1\Electronics 1\electronics1-logbook\media\Scan - 2021-06-16 18_45_07.jpeg)

![](C:\Users\MaxLM\OneDrive\Documents\University\DE1\Electronics 1\electronics1-logbook\media\Scan - 2021-06-16 18_45_30.jpeg)

## Task 4

