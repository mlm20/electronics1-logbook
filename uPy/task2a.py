# uses the switch to turn on and off the rLED
from machine import Pin

rLED = Pin(33, Pin.OUT)
button = Pin(22, Pin.IN, Pin.PULL_UP)

while True: # loop forever
    if button.value() == 0:
        rLED.on()
    elif button.value() == 1:
        rLED.off()
