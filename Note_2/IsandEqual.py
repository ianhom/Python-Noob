#!/usr/bin/python

x = [1,2,3];
y = [2,4];
print "x = [1,2,3]"
print "y = [2,4]"
print "---- x is not y?         ",x is not y,"\n";
del x[2];
y[1] = 1;
y.reverse();
print "del x[2];";
print "y[1] = 1;";
print "y.reverse();";
print "---- x is equal to y?    ",x == y;
print "---- x is y?             ",x is y;

# result
'''
x = [1,2,3]
y = [2,4]
---- x is not y?          True 

del x[2];
y[1] = 1;
y.reverse();
---- x is equal to y?     True
---- x is y?              False
'''
