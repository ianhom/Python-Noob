#!/usr/bin/python
# -*- coding: UTF-8 -*-

num = 9;
if num > 0 and num <= 10:
    print "hello";

num = 10;
if num < 0 or num > 10:
    print "hello";
else:
    print "undefine";
    
num = 8;
if (num >= 0 and num <=5) or (num >= 10 and num <= 15):
    print "hello";
else:
    print "undefine xxx";
print "end"

# result
"""
hello
undefine
undefine xxx
end
"""
