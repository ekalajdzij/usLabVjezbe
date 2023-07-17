#include "mbed.h"
#include "lpc1114etf.h"

#define WAIT_TIME_MS 500 
DigitalOut enable(LED_ACT);
DigitalOut ledSvjetla[8] = {LED0, LED1, LED2, LED3, LED4, LED5, LED6, LED7};


int main()
{
    enable = 0;
    for (int i = 0; i<8; i++)
        ledSvjetla[i] = 0;
    int j = 0;
    while (1) {
        thread_sleep_for(100);
        if(j == 0) {
            ledSvjetla[j] = 1;
            j++;
        }
        else {
            ledSvjetla[j] = 1;
            ledSvjetla[j-1] = 0;
            j++;
            if (j == 8) {
                for(int i = 0; i<8; i++)
                    ledSvjetla[i] = 1;
                j = 7;
                int x = 7;
                while(x != -1) {
                    thread_sleep_for(100);
                    ledSvjetla[j] = 0;
                    thread_sleep_for(100);
                    j--;
                    x--;
                }
            }
        }
    }

}