import machine
from machine import Pin
import time
t4 = Pin(3, Pin.IN)
led7 = Pin(11, Pin.OUT)

while True :
	led7.value(t4.value())


