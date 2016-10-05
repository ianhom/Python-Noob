#!/usr/bin/python

while True:
    name = "";
    while not name:
        name = raw_input("Please enter your name ");
    if name == "stop":
        break;
    print "Hello, %s!" % name,"\n";

# result
'''
Please enter your name Ian
Hello, Ian! 

Please enter your name 
Please enter your name 
Please enter your name Jane
Hello, Jane! 

Please enter your name stop
'''
