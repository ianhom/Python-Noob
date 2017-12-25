#!/bin/usr/python
# -*- coding: UTF-8 -*-

'''
题目：取一个整数a从右端开始的4〜7位。
'''
 
if __name__ == '__main__':
    a = int(raw_input('input a number:\n'))
    b = a >> 4
    c = ~(~0 << 4)
    d = b & c
    print '%o\t%o' %(a,d)


# Result
'''
input a number:
3
3	0
'''
