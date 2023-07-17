import machine
from machine import Pin,PWM,Timer
import time
izlaz=PWM(Pin(16))
D1=Pin(4,Pin.OUT)
D2=Pin(5,Pin.OUT)
D3=Pin(6,Pin.OUT)
D4=Pin(7,Pin.OUT)
A=Pin(8,Pin.OUT)
B=Pin(9,Pin.OUT)
C=Pin(10,Pin.OUT)
D=Pin(11,Pin.OUT)
E=Pin(12,Pin.OUT)
F=Pin(13,Pin.OUT)
G=Pin(14,Pin.OUT)
DP=Pin(15, Pin.OUT)
red1=Pin(0,Pin.OUT)
red2=Pin(1,Pin.OUT)
red3=Pin(2,Pin.OUT)
red4=Pin(3,Pin.OUT)
kolona1=Pin(21,Pin.IN,Pin.PULL_DOWN)
kolona2=Pin(22,Pin.IN,Pin.PULL_DOWN)
kolona3=Pin(26,Pin.IN,Pin.PULL_DOWN)
kolona4=Pin(27,Pin.IN,Pin.PULL_DOWN)

def led(brojac1):
    if brojac1==0:
        A.off()
        B.off()
        C.off()
        D.off()
        E.off()
        F.off()
        G.on()
       
    elif brojac1==1:
        A.on()
        B.off()
        C.off()
        D.on()
        E.on()
        F.on()
        G.on()
   
    elif brojac1==2:
        A.off()
        B.off()
        C.on()
        D.off()
        E.off()
        F.on()
        G.off()
       
    elif brojac1==3:
        A.off()
        B.off()
        C.off()
        D.off()
        E.on()
        F.on()
        G.off()
   
    elif brojac1==4:
        A.on()
        B.off()
        C.off()
        D.on()
        E.on()
        F.off()
        G.off()  
   
    elif brojac1==5:
        A.off()
        B.on()
        C.off()
        D.off()
        E.on()
        F.off()
        G.off()
       
    elif brojac1==6:
        A.off()
        B.on()
        C.off()
        D.off()
        E.off()
        F.off()
        G.off()
       
    elif brojac1==7:
        A.off()
        B.off()
        C.off()
        D.on()
        E.on()
        F.on()
        G.on()
       
    elif brojac1==8:
        A.off()
        B.off()
        C.off()
        D.off()
        E.off()
        F.off()
        G.off()
       
    elif brojac1==9:
        A.off()
        B.off()
        C.off()
        D.off()
        E.on()
        F.off()
        G.off()
   
DP.on()
pozicije=[1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1]
brojac=0
br=0
k=0
def fun(p):
    if izlaz.freq() > 96 and izlaz.freq() < 101:
        izlaz.freq(100)
    if izlaz.freq() > 700 and izlaz.freq() < 1001:
        izlaz.freq(1000)
    brojac=(int)(1/izlaz.freq()*1000)
    print(brojac)
    D4.on()
    led(0)
    D1.off()
    time.sleep_ms(2)
    D1.on()
    led(0)
    D2.off()
    time.sleep_ms(2)
    D2.on()
    led((brojac/10)%10)
    D3.off()
    time.sleep_ms(2)
    D3.on()
    led(brojac%10)
    D4.off()
    time.sleep_ms(2)

t=Timer(period=10,callback=fun)
izlaz.duty_u16(32767)
izlaz.freq(1000)
j=0
while True:
    for i in range(0,16,4):
        red1.value(pozicije[i])
        red2.value(pozicije[i+1])
        red3.value(pozicije[i+2])
        red4.value(pozicije[i+3])
        if kolona1.value()==1:
            if red4.value():
                if i==12:
                    izlaz.duty_u16(32767-izlaz.duty_u16())
            else:
                j=i//4+2
                izlaz.freq((int)((1/j)*1000))
                print(i//4+1)
            time.sleep_ms(200)
        elif kolona2.value()==1:
            j=i//4+5
            izlaz.freq((int)((1/j)*1000))
            time.sleep_ms(200)
        elif kolona3.value()==1:
            j=i//4+8
            if red4.value():
                if izlaz.freq() > 100:
                    izlaz.freq((int)(1/((1/izlaz.freq())*1000+1)*1000))
            else:
                izlaz.freq((int)((1/j)*1000))
            time.sleep_ms(200)
        elif kolona4.value()==1:
            if red4.value():
                if izlaz.freq() < 700:
                    izlaz.freq((int)(1/((1/izlaz.freq())*1000-1)*1000))    
            elif red2.value():
                izlaz.freq(1000)
            time.sleep_ms(200)