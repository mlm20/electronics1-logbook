import machine, time
LED = machine.Pin(25,Pin.OUT)
while True:
    LED.on()
    time.sleep(1)
    LED.off()
    time.sleep(1)
