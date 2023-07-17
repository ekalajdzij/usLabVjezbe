#include "mbed.h"
#include "lpc1114etf.h"

#define WAIT_TIME_MS 500 
DigitalOut enable(LED_ACT);
DigitalOut led(LED1);
int main()
{
    enable = 0;
    float T = 1.0; // početno vrijeme uključenosti u sekundama
    float on_time = T;
    float off_time = T/10;
    float increment = 0.06*T; // 30T sekundi za dostizanje 1.9T vremena uključenosti
    float decrement = increment; // ista brzina za povećavanje i smanjivanje
    
    while(1) {
    // uključi LED na on_time sekundi
    led = 1;
    thread_sleep_for(on_time);
    
    // isključi LED na off_time sekundi
    led = 0;
    thread_sleep_for(off_time);
    
    // postupno povećavaj vrijeme uključenosti sve dok ne dostigne 1.9T sekundi
    if (on_time < 1.9*T) {
        on_time += increment;
        off_time = T - on_time/10;
    }
    // postupno smanjuj vrijeme uključenosti sve dok ne dostigne 0.1T sekundi
    else if (on_time > 0.1*T) {
        on_time -= decrement;
        off_time = T - on_time/10;
    }
    // resetuj vrijeme uključenosti i isključenosti kako bi proces počeo iznova
    else {
        on_time = 0.1*T;
        off_time = 1.9*T;
    }
}
}