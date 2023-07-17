#include "mbed.h"
#include "lpc1114etf.h"

PwmOut led1(dp18);
AnalogIn potenciometar(dp9);
DigitalOut enable(dp14);
BusOut leds(LED0,LED1,LED2,LED3,LED4,LED5,LED6,LED7);

int main () {
    leds = 0;
    led1.period_ms(500);
    //led1.period_ms(500);
    while(1) {
        led1.write(potenciometar.read());
    }
}