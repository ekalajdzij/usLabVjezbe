#include "mbed.h"
#include "lpc1114etf.h"

#define WAIT_TIME_MS 500 
DigitalOut Enable (LED_ACT);
DigitalOut led0(LED0);
DigitalOut led1(LED1);
DigitalOut led2(LED2);
DigitalOut led3(LED3);


int main()
{
    Enable = 0;

    while(1){
        led0 = 1;
        thread_sleep_for(1000);
        led0 = 0;
        thread_sleep_for(1000);


        led1 = 1;
        thread_sleep_for(1000);
        led1 = 0;
        thread_sleep_for(1000);


        led2 = 1;
        thread_sleep_for(1000);
        led2 = 0;
        thread_sleep_for(1000);

        led3 = 1;
        thread_sleep_for(1000);
        led3 = 0;
        thread_sleep_for(1000);

    }

}

