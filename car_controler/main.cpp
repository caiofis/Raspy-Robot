#include "mbed.h"

#include "mbed.h"
#include "TFC.h"
 
 
//This macro is to maintain compatibility with Codewarrior version of the sample.   This version uses the MBED libraries for serial port access
Serial PC(USBTX,USBRX);
 
#define TERMINAL_PRINTF     PC.printf
 
 
 //This ticker code is used to maintain compability with the Codewarrior version of the sample.   This code uses an MBED Ticker for background timing.
 
#define NUM_TFC_TICKERS 4

 
Ticker TFC_TickerObj;
 
volatile uint32_t TFC_Ticker[NUM_TFC_TICKERS];
 
void TFC_TickerUpdate()
{
    int i;
 
    for(i=0; i<NUM_TFC_TICKERS; i++)
     {
        if(TFC_Ticker[i]<0xFFFFFFFF) 
        {
            TFC_Ticker[i]++;
        }
    }
}

char sb = 'S';               //define o starbit  da comunicação
//char eb = 'EB';               //Define o errorbit da comunicação
char commands[] = {1,0,1,0,1,0,0};        //array of the commands bytes [M1h,M1l,M2h,M2l,steerh,steerl, leds]
float motors[] =  {0.0,0.0,0.0};         // array of values to the motors [Ma,Mb,Servo]
int i = 0;
int count = 0;      //Number of encoder steps
void update()
{
    motors[0] = (((commands[0]*10+commands[1])-10)/10.0);
    motors[1] = (((commands[2]*10+commands[3])-10)/10.0);
    motors[2] = (((commands[4]*10+commands[5])-10)/10.0);
    commands[6] = commands[6];

    TFC_SetMotorPWM(motors[0],motors[1]);
    TFC_SetServo(0,motors[2]);
    TFC_SetBatteryLED_Level(commands[6]);
}
void comm(char *commands) 
{   
    int temp[7];        //Temporary commnads array
    int checksum[2];    // 2bytes checksum array    
    int sum = 0;        //sum of the income data
    newbit:
    if(PC.readable())
    {
        sum = 0; 
        char income = PC.getc(); 
        while(income!=sb)             // read until find the start byte
            income = PC.getc();
        //PC.printf("a");
        for(i=0;i<=6;i++)             // read 7 bytes, the temporary commands
            temp[i] = PC.getc()-'0';
        for(i=0;i<2;i++)               // read 2 bytes of checksum
            checksum[i] = PC.getc()-'0';
        for(i=0;i<=4;i=i+2)
            sum += temp[i]*10 + temp[i+1];
        sum+=temp[6];
        if(checksum[0]*10+checksum[1] == sum)
        {
            for(i=0;i<=6;i++)             // update the commands array
                commands[i] = temp[i];
            update();
            PC.printf("%02i",count);
            count = 0;
        }
        else
        {
            PC.printf("EB");
            goto newbit;
        }
     }
}

void flip()
{
    count++;
}
int main()
{  
    PC.baud(115200);
    TFC_TickerObj.attach_us(&TFC_TickerUpdate,2000); // update ticker array every 2mS (2000 uS)
    TFC_Init();
    TFC_HBRIDGE_ENABLE;
    InterruptIn button(PTA17);//Interrupção no pino
    button.rise(&flip);  // attach the address of the flip function to the rising edge
    TFC_Ticker[0] = 0;
    update();
    while(1)
    {      
        //PC.printf("Hello World!\n");
        
       //button.rise(NULL);      // Disable interruptions
       comm(&commands[0]);    //Pass commands as a parameter of comm  
       //update();
        
        
        //TFC_Task must be called in your main loop.  This keeps certain processing happy (I.E. Serial port queue check)
         //   TFC_Task();
    }    
 
}