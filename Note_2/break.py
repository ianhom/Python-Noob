#!/usr/bin/python

from math import sqrt

for n in range(99, 0, -1):
    root = sqrt(n);
    if root == int(root):
        print n;
        if n == 9:
            break;

# result
'''
81
64
49
36
25
16
9
'''
