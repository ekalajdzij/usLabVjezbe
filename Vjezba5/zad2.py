import machine
from machine import PWM, Pin, ADC
import time


fotootpornik = ADC(Pin(26))
led0 = PWM(Pin(4))
led1 = PWM(Pin(5))
led2 = PWM(Pin(6))
led3 = PWM(Pin(7))
led4 = PWM(Pin(8))
led5 = PWM(Pin(9))
led6 = PWM(Pin(10))
led7 = PWM(Pin(11))

maxV = 60000


while 1:
    fotoV = fotootpornik.read_u16()
    time.sleep(0.1)
    if fotoV < 58000:
    led7.duty_u16(100)
    elif fotoV > 58000:
        led7.duty_u16(maxV)

    led6.duty_u16(int(fotoV/10))
    led5.duty_u16(int(fotoV/20))
    led4.duty_u16(int(fotoV/30))
    led3.duty_u16(int(fotoV/40))
    led2.duty_u16(int(fotoV/50))
    led1.duty_u16(int(fotoV/60))
    led0.duty_u16(int(fotoV/70))
    print(fotoV)
