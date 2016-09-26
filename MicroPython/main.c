print('Hello, world, I am micropython')
print('who are you!')

import time

import machine
p = machine.Pin(2,machine.Pin.OUT)
p.high()

def toggle(p):
    p.value(not p.value())

toggle(p)
time.sleep_ms(500)

toggle(p)
time.sleep_ms(500)

toggle(p)
time.sleep_ms(500)

toggle(p)
time.sleep_ms(500)

def led(a,b,c):
    a *= 2
    while a != 0:
        a -= 1
        time.sleep_ms(b)
        toggle(c)
    return


