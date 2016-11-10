#!/usr/bin/python
# -*- coding: UTF-8 -*-

f = open("hi.txt","r");
print "We are opening the \"", f.name, "\"";

for index in range(5):
    line = f.next();
    print "Line-%d : %s" % (index, line);

f.close();

# result
'''
We are opening the " hi.txt "
Line-0 : hello 1

Line-1 : hello 2

Line-2 : hello 3

Line-3 : hello 4

Line-4 : hello 5
'''
