#!/usr/bin/python
# -*- coding: UTF-8 -*-

f = open("Hi.txt","w");
strs = ["Hello 1", "Hello 2"];

f.writelines(strs);

f.close();
f = open("Hi.txt","r");

line = f.readline();
print line;
line = f.readline();
print line;

f.close();

# Result
'''
Hello 1Hello 2
'''
