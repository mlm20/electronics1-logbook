from machine import Pin, ADC, PWM

rLED = PWM(Pin(33), freq = 1000)

pot = ADC(Pin(38))
pot.atten(ADC.ATTN_11DB)
pot.width(ADC.WIDTH_9BIT)

while True:
    duty = int((pot.read() / 511) * 1023)
    rLED.duty(duty)
