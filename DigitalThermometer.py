import time

RS = 5
RW = 6
EN = 7
ale = 3
oe = 4
start = 1
eoc = 0
clk = 2
chc = 7
chb = 6
cha = 5

def delay(t):
    time.sleep(t)

def lcd_init():
    lcd_command(0x38)
    lcd_command(0x01)
    lcd_command(0x0f)
    lcd_command(0x06)
    lcd_command(0x0c)
    lcd_command(0x80)

def lcd_command(c):
    pass

def lcd_data(d):
    pass

def str(a):
    for j in range(len(a)):
        lcd_data(a[j])

def print(p):
    pass

k = 0
q = 0
r = 0
x = 0
y = 0
z = 0

def timer0():
    clk = not clk

lcd_init()
str("DIGITALTHERMOMETER")
lcd_command(0x01)
str("Temp:")
lcd_command(96)
lcd_data(0x10)
lcd_data(0x07)
lcd_data(0x08)
lcd_data(0x08)
lcd_data(0x08)
lcd_data(0x08)
lcd_data(0x07)
lcd_command(0x8b)
lcd_data(4)
eoc = 1
ale = 0
oe = 0
start = 0
TMOD = 0x02
TH0 = 0xc2
IE = 0x82
TR0 = 1

while True:
    chc = 0
    chb = 0
    cha = 0
    ale = 1
    start = 1
    delay(1)
    ale = 0
    start = 0
    while eoc == 1:
        pass
    while eoc == 0:
        pass
    oe = 1
    k = P1
    lcd_command(0x85)
    print(k)
    oe = 0
k = P1
lcd_command(0x85)
print(k)
oe = 0

def str(a):
    j = 0
    while a[j] != '\0':
        lcd_data(a[j])
        j += 1

def lcd_init():
    lcd_command(0x38)
    lcd_command(0x01)
    lcd_command(0x0f)
    lcd_command(0x06)
    lcd_command(0x0c)
    lcd_command(0x80)

def lcd_command(c):
    P3 = c
    RS = 0
    RW = 0
    EN = 1
    delay(5)
    EN = 0
    delay(5)

def lcd_data(d):
    P3 = d
    RS = 1
    RW = 0
    EN = 1
    delay(5)
    EN = 0
    delay(5)

def delay(t):
    j = 0
    while j < t * 400:
        j += 1

def print(p):
    x = p * 10
    if x >= 1000:
        q = x / 1000
        q = q + 48
        y = (x % 1000) / 100
        y = y + 48
        z = ((x % 1000) % 100) / 10
        z = z + 48
        r = x % 10
        r = r + 48
        lcd_data(q)
        lcd_data(y)
        lcd_data(z)
        lcd_data(46)
        lcd_data(r)
    else:
        q = x / 100
        q = q + 48
        y = (x % 100) / 10
        y = y + 48
        z = x % 10
        z = z + 48
        lcd_data(q)
        lcd_data(y)
        lcd_data(46)
        lcd_data(z)
        r = 0
        lcd_data(r)

