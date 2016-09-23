#!/usr/bin/python

f = open("readme.txt","w");
f.write("Hello, world!!");
f.close();

e = open("readme.txt","r");
e.read();
e.close();

# result
"""
14
'Hello, world'
"""
