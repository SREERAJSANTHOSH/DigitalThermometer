#include<stdio.h>

#include<reg51.h>

#include<string.h>

 

sbit RS = P2^5; 

sbit RW = P2^6;

sbit EN = P2^7;

sbit ale=P2^3;  

sbit oe=P2^4; 

sbit start=P2^1; 

sbit eoc=P2^0;  

sbit clk=P2^2; 

sbit chc=P0^7; 

sbit chb=P0^6;

sbit cha=P0^5;

 

void delay(int t); 

void lcd_init(void);

void lcd_command(char c);

void lcd_data(char d);

void str(char a[]);

void print( long float p);

long float k;

unsigned long int q,r,x,y,z;

 

void timer0() interrupt 1  
{

    clk=~clk;

}

 

void main()

{

lcd_init();

str("DIGITALTHERMOMETER");

lcd_command(0x01);  

str("Temp:");

lcd_command(96);

lcd_data(0x10);

lcd_data(0x07);

lcd_data(0x08);

lcd_data(0x08);

lcd_data(0x08);

lcd_data(0x08);

lcd_data(0x07);

lcd_command(0x8b);

lcd_data(4);

eoc=1;            

ale=0;

oe=0;

start=0;

TMOD=0x02;   

TH0=0xc2;

IE=0x82; 

TR0=1;   

while(1)

{ 

chc=0; 

chb=0;

cha=0;

ale=1;  

start=1;

delay(1);

ale=0;

start=0;

while(eoc==1);    

while(eoc==0); 

oe=1;

k=P1;

lcd_command(0x85);

print(k); 

oe=0;

}

}

void str(char a[]) 

{

int j;

for(j=0;a[j]!='\0';j++)

{

lcd_data(a[j]);

}

}

void lcd_init(void)

{

lcd_command(0x38);  

lcd_command(0x01);   

lcd_command(0x0f);

lcd_command(0x06);

lcd_command(0x0c); 

lcd_command(0x80); 

}

void lcd_command(char c) 

{

P3=c;

RS=0;

RW=0;   

EN=1;

delay(5);

EN=0;

delay(5);

}

void lcd_data(char d) 
{

P3=d;

RS=1;

RW=0;

EN=1;

delay(5);

EN=0;

delay(5);

}

void delay(int t)

{

int j;

for(j=0;j<t*400;j++);

}

void print( long float p)  
{

x=p*10;

if(x>=1000)

{

q=x/1000;

q=q+48;

y=(x%1000)/100;

y=y+48;

z=((x%1000)%100)/10;

z=z+48;

r=x%10;

r=r+48;

lcd_data(q);

lcd_data(y);

lcd_data(z);

lcd_data(46);

lcd_data(r);

}

else

{

q=x/100;

q=q+48;

y=(x%100)/10;

y=y+48;

z=x%10;

z=z+48;

lcd_data(q);

lcd_data(y);

lcd_data(46); 

lcd_data(z);

r=0;

lcd_data(r);

}

}

