#!/usr/bin/python

while True:
    name = raw_input("What is your name? ");

    if name == "stop":
        break;

    if "I" in name:
        print "There is an \"I\" in your name.";
    else:
        print "There is NOT an \"I\" in your name"

# result
'''
What is your name? Ian
There is an "I" in your name.
What is your name? Jane
There is NOT an "I" in your name
What is your name? stop
'''
