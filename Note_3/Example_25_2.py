#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：求1+2!+3!+...+20!的和。
'''

s = 0
l = range(1,21)
def op(x):
    r = 1
    for i in range(1,x + 1):
        r *= i
    return r
s = sum(map(op,l))
print '1! + 2! + 3! + ... + 20! = %d' % s

# result
'''
1! + 2! + 3! + ... + 20! = 2561327494111820313
'''
