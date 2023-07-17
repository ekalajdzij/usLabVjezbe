import machine
from machine import Pin
g = Pin(12, Pin.OUT)
g.value(1)
b = Pin(13, Pin.OUT)
b.value(1)
r = Pin(14, Pin.OUT)
r.value(1)
r.value(0)