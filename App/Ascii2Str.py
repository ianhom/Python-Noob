#!/usr/bin/python
'''
test = [65,66,67,68];

def Ascii2Str():
    while(1):
        lst = input("Please input:");
        c = [];
        for a in lst:
            b = chr(a);
            c.append(b);
        d =''.join(c)
        print d;

# Ascii2Str();
'''
import binascii

def Ascii2Str():
    "Transfer Ascii to string to check hex-file"
    while True:
        a = raw_input("Please input the bin: ");

        if a == "stop":
            print "Function is over!"
            return;
        print binascii.a2b_hex(a).decode("ascii");
    return;

