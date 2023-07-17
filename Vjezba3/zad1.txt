/* mbed Microcontroller Library
 * Copyright (c) 2019 ARM Limited
 * SPDX-License-Identifier: Apache-2.0
 */

#include "mbed.h"
#include "lpc1114etf.h"

#define WAIT_TIME_MS 500 
DigitalOut led1(LED1);
BusOut redovi(dp16, dp15, dp17);
BusIn kolone(dp9, dp10, dp11);
BusOut ledSvjetla(LED0, LED1, LED2, LED3, LED4, LED5, LED6, LED7);
DigitalOut enable(LED_ACT);


int main()
{
    enable = 0;
    ledSvjetla = 255;
    
    
    while(1){
        redovi[0] = 1;
        redovi[1] = 0;
        redovi[2] = 0;
        if(kolone[0]){
            ledSvjetla[0] = 0;
        }
        else ledSvjetla[0] = 1;

        if(kolone[1]){
            ledSvjetla[1] = 0;
        }
        else ledSvjetla[1] = 1;  
        
        if(kolone[2]){
            ledSvjetla[2] = 0;
        }
        else ledSvjetla[2] = 1;

        
        
        redovi[0] = 0;
        redovi[1] = 1;
        redovi[2] = 0;
        if(kolone[0]){
            ledSvjetla[3] = 0;
        }
        else ledSvjetla[3] = 1;

        if(kolone[1]){
            ledSvjetla[4] = 0;
        }  
        else ledSvjetla[4] = 1;

        if(kolone[2]){
            ledSvjetla[5] = 0;
        }
        else ledSvjetla[5] = 1;


        redovi[0] = 0;
        redovi[1] = 0;
        redovi[2] = 1;
        if(kolone[0]){
            ledSvjetla[6] = 0;
        }
        else ledSvjetla[6] = 1;

        if(kolone[1]){
            ledSvjetla[7] = 0;
        }
        else ledSvjetla[7] = 1;

    }
}