#!/usr/bin/python

import os

f = open("hi.txt","w");
f.write("Hi everybody\n\n");
f.close();

e = open("hi.txt");
s = e.read();
e.close();

print s;
