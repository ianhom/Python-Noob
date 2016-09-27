print('***************************************************************')
print('*            Hello, world, I am micropython ESP8266           *')
print('***************************************************************')

import time
import os
import machine

ls = "Sorry! I am python, NOT shell!"
sl = "Wowwow!!! I am a train~~:P"
    
p = machine.Pin(2,machine.Pin.OUT)
p.high()

def toggle(p):
    p.value(not p.value())

def led(a,b,c):
    a *= 2
    while a != 0:
        a -= 1
        time.sleep_ms(b)
        toggle(c)
    return
     
led(3,500,p) 


