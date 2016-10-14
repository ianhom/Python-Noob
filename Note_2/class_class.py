#!/usr/bin/python

class Class:
    def method(self):
        'This is a method of class'
        print "I have a self!";

def function():
    'This is just a function'
    print "I don't have a self";

instance = Class();
print instance.method.__doc__;
instance.method();
print
instance.method = function;
print instance.method.__doc__;
instance.method();

# result
'''
This is a method of class
I have a self!

This is just a function
I don't have a self
'''

