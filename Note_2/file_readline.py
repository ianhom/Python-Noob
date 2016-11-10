#!/usr/bin/python
# -*- coding: UTF-8 -*-

f = open("hi.txt", "r");

line = f.readline();
print "The content is: ", line;

line = f.readline();
print "The content is: ", line;


line = f.readline(3);
print "The content is: ", line;


line = f.readline(13);
print "The content is: ", line;

f.close();

# result
'''
The content is:  hello 1

The content is:  hello 2

The content is:  hel
The content is:  lo 3

'''
