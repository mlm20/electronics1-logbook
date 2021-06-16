# task2b.py - switch bouncs effect

from machine import Pin

# instantiate Pin objects
button = Pin(22, Pin.IN, Pin.PULL_UP)

while True:
    if button.value() == 1:
        print("+", end = "")
        while button.value() == 1:
            pass
        print("-", end = "")
