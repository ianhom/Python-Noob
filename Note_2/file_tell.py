#!/usr/bin/python
# -*- coding: UTF-8 -*-

f = open("hi.txt", "r");

line = f.readline();
line2 = f.read(3);

pos = f.tell()
print "We are at", pos;

f.close();


# Result
'''
We are at 12
'''
