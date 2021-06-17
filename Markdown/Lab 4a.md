# Setting up MicroPython

**[Homepage](./index.html)**

## Task 1 & 2

The ESP32 device was flashed with micropython as per the instructions.

![](./media/upython code.jpg)

### Step 3

```python
from machine import Pin
LED = Pin(25, Pin.OUT)
LED.on()
```



![](./media/pic10.jpg)

The LED light turned on as expected

### Step 4

The code was written as per the instructions and the light blinked as expected

## Task 4

The uPy classes and functions were explored. I completed the mini challenge, using PWM to change the brightness of the LED. The brightness changed when I changed the value of `duty_cycle`

```python
import machine
from machine import Pin, PWM

frequency = 5000
duty_cycle = 1023 # 0 - 1023 || 1023 = 100%

led = PWM(Pin(25, Pin.OUT), frequency)

led.duty(duty_cycle)
```

![](./media/pic10.jpg)

![](./media/pic.jpg)

## Task 5

### Step 1 & 2

The files were created and flashed as expected.

### Step 3

The uPy files were recreated in Mu and flashed across to ESP32. The screen displayed the `Hello World!` message.

<img src="./media/Scan - 2021-06-16 13_05_21.jpeg" style="zoom: 25%;" />

**[Homepage](./index.html)**

