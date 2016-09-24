#!/usr/bin/python

f = open("readme.txt","w");
c = f.write("Hello, world!!");
f.close();
print c;

e = open("readme.txt","r");
s = e.read();
e.close();
print s;

# result
"""
14
'Hello, world'
"""
