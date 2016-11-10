#!/usr/bin/python
# -*- coding: UTF-8 -*-

f = open("hi.txt","r");

line = f.read(20);
print "I get ", line;

f.close();

# result
'''
I get  hello 1
hello 2
hell
'''
