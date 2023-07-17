/* mbed Microcontroller Library
 * Copyright (c) 2019 ARM Limited
 * SPDX-License-Identifier: Apache-2.0
 */
#include "mbed.h"
#include "lpc1114etf.h"


DigitalOut led0(LED0);


DigitalIn taster1(Taster_1);
DigitalIn taster2(Taster_2);


DigitalOut ledSvjetla[8] = {LED0,LED1,LED2,LED3,LED4,LED5,LED6,LED7};


int main() {
    bool taster1_stari = 0;
    bool taster2_stari = 0;
    for(int i = 0; i<8; i++) 
		ledSvjetla[i] = 0;
	
	int j = 0;
    while (1) {
        if(!taster1_stari&&taster1) {
	    thread_sleep_for(100);
		if (j == 0) {
		    ledSvjetla[j] = 1;
		    j++;
		} else {
		
		ledSvjetla[j] = 1;
		ledSvjetla[j-1] = 0;
		j++;
		if (j == 8) {
			for (int i = 0; i < 8; i++)
				ledSvjetla[i] = 1;
			j = 7;
			int x = 7;
			while (x != -1) {
				thread_sleep_for(100);
				ledSvjetla[j] = 0;
				thread_sleep_for(100);
				j--;
				x--;
			    }
		    }
		}
            
        } else if(!taster2_stari&&taster2){
            thread_sleep_for(500);
		    if (j == 0) {
		        ledSvjetla[j] = 1;
		        j++;
		} else {
		
                ledSvjetla[j] = 1;
                ledSvjetla[j-1] = 0;
                j++;
		        if (j == 8) {
			        for (int i = 0; i < 8; i++)
				    ledSvjetla[i] = 1;
			        j = 7;
			        int x = 7;
			        while (x != -1) {
				        thread_sleep_for(500);
				        ledSvjetla[j] = 0;
				        thread_sleep_for(500);
				        j--;
				        x--;
			        }
		        }
		    }
        } else{
            led0 = !led0;
            thread_sleep_for(400);
            led0 = !led0;
        }
        thread_sleep_for(600);
    }
}