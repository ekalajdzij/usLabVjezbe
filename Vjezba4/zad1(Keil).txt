#include "mbed.h"
#include "lpc1114etf.h"

DigitalOut ledSvjetla[8] = {LED0, LED1, LED2, LED3, LED4, LED5, LED6, LED7};
AnalogIn potenciometar(AD1);
DigitalOut enable(LED_ACT);

int main() {
    enable = 0;
    for(int i = 0; i<8; i++) 
        ledSvjetla[i] = 0;
    
    int j = 0;
    while (1) {
        thread_sleep_for((potenciometar.read()*1.9f + 0.1f)*1000);
        if (j == 0) {
            ledSvjetla[j] = 1;
            j++;
        } else {
            ledSvjetla[j-1] = 0;
            ledSvjetla[j] = 1;
            j++;
            if(j== 9) {
                while(j != -1) {
                    ledSvjetla[j-1] = 1;
                    ledSvjetla[j] = 0;
                    thread_sleep_for((potenciometar.read()*1.9f + 0.1f)*1000);
                    j--;
                }
                j=0;
            }
        }
    }
}