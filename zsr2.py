import machine
from machine import Pin
import time

g = Pin(12,Pin.OUT)
b = Pin(13,Pin.OUT)
r = Pin(14,Pin.OUT)
korak = 0
vrijeme = 0

while True:
    korak = 0.1
    vrijeme = 0.1
    for i in range(2):
        for j in range(9):
           
            g.on()
            time.sleep(vrijeme)
            g.off()
           
            b.on()
            time.sleep(vrijeme)
            b.off()
           
            r.on()
            time.sleep(vrijeme)
            r.off()
           
            g.on()
            b.on()
            time.sleep(vrijeme)
            g.off()
            b.off()
           
           
            g.on()
            r.on()
            time.sleep(vrijeme)
            g.off()
            r.off()
           
           
            r.on()
            b.on()
            time.sleep(vrijeme)
            r.off()
            b.off()
           
           
            g.on()
            b.on()
            r.on()
            time.sleep(vrijeme)
            g.off()
            b.off()
            r.off()
           
            if i == 1:  
                vrijeme -= korak
            else :
                vrijeme += korak
            