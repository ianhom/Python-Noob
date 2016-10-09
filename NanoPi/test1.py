#!/usr/bin/python

while True:
    name = raw_input("Please input your name: ");
    if name:
        if name == "Bye":
            print "Goodbye!!";
            break;
        print "Hello, dear " + name;
    
# result
'''
Please input your name: Ian
Hello, dear Ian
Please input your name: Jane
Hello, dear Jane
Please input your name:
Please input your name: Bye
Goodbye!!
'''
