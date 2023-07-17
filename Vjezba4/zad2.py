"""
Ugradbeni sistemi 2023
Demo prikaza na TFT displeju ILI9341
rezolucija displeja 320x240
"""


from ili934xnew import ILI9341, color565
from machine import Pin, SPI
from machine import ADC
from micropython import const
import os
import time
import glcdfont
import tt14
import tt24
import tt32
import time

# Dimenzije displeja
SCR_WIDTH = const(320)
SCR_HEIGHT = const(240)
SCR_ROT = const(3)
CENTER_Y = int(SCR_WIDTH/2)
CENTER_X = int(SCR_HEIGHT/2)

# Podešenja SPI komunikacije sa displejem
TFT_CLK_PIN = const(18)
TFT_MOSI_PIN = const(19)
TFT_MISO_PIN = const(16)
TFT_CS_PIN = const(17)
TFT_RST_PIN = const(20)
TFT_DC_PIN = const(15)
# Fontovi na raspolaganju
fonts = [glcdfont,tt14,tt24,tt32]

text = 'RPi Pico/ILI9341'

for f in fonts:
    print(f.__name__)

spi = SPI(
    0,
    baudrate=62500000,
    miso=Pin(TFT_MISO_PIN),
    mosi=Pin(TFT_MOSI_PIN),
    sck=Pin(TFT_CLK_PIN))

display = ILI9341(
    spi,
    cs=Pin(TFT_CS_PIN),
    dc=Pin(TFT_DC_PIN),
    rst=Pin(TFT_RST_PIN),
    w=SCR_WIDTH,
    h=SCR_HEIGHT,
    r=SCR_ROT)

# Brisanje displeja i odabir pozicije (0,0)
display.erase()

display.set_pos(0,0)
display.set_font(glcdfont)
display.set_color(color565(255,255,255), color565(0,0,0))

def draw_vline(x,y):
    for i in range(y,SCR_HEIGHT-y):
        display.pixel(x,i+y,color565(255,255,255))

def draw_hline(x,y):
    for i in range(x,SCR_WIDTH-x):
        display.pixel(x+i,y,color565(255,255,255))

def display_init():
    display.set_pos(0,0)
    display.set_font(glcdfont)
    display.set_color(color565(255,255,255), color565(0,0,0))
    draw_vline(10,10)
    draw_hline(0,230)
    display.set_pos(15,15)
    display.print('40')

    display.set_pos(15,110)
    display.print('30')

    display.set_pos(15,215)
    display.print('20')

    display.set_pos(230,0)
    display.print('Napon:')

    display.set_pos(230,15)
    display.print('Temp:')

    display.set_pos(230,30)
    display.print('Vrijeme:')

display_init()

def draw_circle(xpos0, ypos0, rad, col=color565(255, 255, 255)):
    x = rad - 1
    y = 0
    dx = 1
    dy = 1
    err = dx - (rad << 1)
    while x >= y:
        # Prikaz pojedinačnih piksela
        display.pixel(xpos0 + x, ypos0 + y, col)
        display.pixel(xpos0 + y, ypos0 + x, col)
        display.pixel(xpos0 - y, ypos0 + x, col)
        display.pixel(xpos0 - x, ypos0 + y, col)
        display.pixel(xpos0 - x, ypos0 - y, col)
        display.pixel(xpos0 - y, ypos0 - x, col)
        display.pixel(xpos0 + y, ypos0 - x, col)
        display.pixel(xpos0 + x, ypos0 - y, col)
        if err <= 0:
            y += 1
            err += dy
            dy += 2
        if err > 0:
            x -= 1
            dx += 2
            err += dx - (rad << 1)

def ispisiTemp(temperatura):
    display.set_pos(260, 15)
    display.print("{:.1f}".format(temperatura) + " C")

def ispisiVrijeme(vrijeme):
    display.set_pos(280, 30)
    display.print("{:.0f}".format(vrijeme) + " s")
   
def ispisiNapon(napon):
    display.set_pos(270,0)
    display.print("{:.0f}".format(napon) + " mV")

brojacV = 1
tempSensor = ADC(Pin(28))
temperaturaX = 0
br = 0

while 1:
    temperatura = ((tempSensor.read_u16())/65535)*3300*0.1
    temperaturaX =  brojacV
    temperaturaY = (280 - ((temperatura-20) * 11 + 50))
    br = br + 1
    if br == 10:
        br = 1
        draw_circle(int(temperaturaX), int(temperaturaY), 3, color565(255,255,255))
        ispisiTemp(temperatura)
        ispisiVrijeme(brojacV/10)
        ispisiNapon(temperatura*10)
    else:
        display.pixel(int(temperaturaX), int(temperaturaY), color565(0,123,44))
    brojacV = brojacV + 1
    time.sleep(0.1)
    if brojacV == 330:
        display.erase()
        display_init()
        brojacV = 0