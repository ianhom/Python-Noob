#!/usr/bin/python

try:
    x = input("Please enter a number: ");
    y = input("Please enter another number ");

    print x/y;
except ZeroDivisionError:
    print "The second number can not be zero!!";

# result
'''
Please enter a number: 1
Please enter another number 2
Please enter a number: 1
Please enter another number 0
The second number can not be zero!!
'''
