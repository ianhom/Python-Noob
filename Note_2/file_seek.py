#!/usr/bin/python
# -*- coding: UTF-8 -*-

f = open("hi.txt", "r");

line = f.readline()
print "What I read is %s" % (line);

line = f.readline()
print "What I read is %s" % (line);

f.seek(0,0);
line = f.readline()
print "What I read is %s" % (line);

line = f.readline()
print "What I read is %s" % (line);

f.seek(1,1);
line = f.readline()
print "What I read is %s" % (line);

f.seek(20,2);
line = f.readline()
print "What I read is %s" % (line);


f.close();


# result
'''
What I read is hello 1

What I read is hello 2

What I read is hello 1

What I read is hello 2

What I read is ello 3

What I read is 
'''

