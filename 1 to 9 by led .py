import RPi.GPIO as GPIO
import time
import led

led.A1()
led.get_GPIO()

while True:

    led.one()
    time.sleep(1)
    led.two()
    time.sleep(1)
    led.three()
    time.sleep(1)
    led.four()
    time.sleep(1)
    led.five()
    time.sleep(1)
    led.six()
    time.sleep(1)
    led.seven()
    time.sleep(1)
    led.eight()
    time.sleep(1)
    led.nine()
    time.sleep(1)
