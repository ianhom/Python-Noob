#!/usr/bin/python

while True:
    a = raw_input("Please input a letter: ");
    if not a:
        break;
    s = "Hello world!!";
    for n in s:
        print n;
        if n == a:
            break;
    else:    # If no break happens, else code will run 
        print "I didn't find the \"" + a + "\", and I am NOT breaked!!"
    
# result
'''
Please input a letter: a
H
e
l
l
o
 
w
o
r
l
d
!
!
I didn't find the "a", and I am NOT breaked!!
Please input a letter: d
H
e
l
l
o
 
w
o
r
l
d
Please input a letter: 
'''
