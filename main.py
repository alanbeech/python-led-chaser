# LED Chaser in MicroPython

from machine import Pin
from time import sleep

LED = [25, 33, 32, 27, 14]

del_time = 0.1

for i in range(len(LED)):
    LED[i] = Pin(LED[i], Pin.OUT)

while True:
    for i in range(len(LED)):
        LED[i].value(1)
        sleep(del_time)
        LED[i].value(0)
