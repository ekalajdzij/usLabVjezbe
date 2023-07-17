#include "mbed.h"
#include "lpc1114etf.h"

BusOut ledSvjetla(LED0, LED1, LED2, LED3, LED4, LED5, LED6, LED7);
DigitalIn Taster1(Taster_1);
int brojac = 0;
int smjer = 0;
DigitalOut enable (LED_ACT);

int main()
{
    enable = 0;
    bool tasterStari = 0;
    while(1){
        if(!tasterStari && Taster1) {
            smjer = !smjer;
            brojac--;
	}
        
        if(!smjer)
            brojac++;
        if(brojac > 255) brojac = 0;
        if(brojac < 0) brojac = 255;

        ledSvjetla = brojac;
        thread_sleep_for(1000);



    }    
}
