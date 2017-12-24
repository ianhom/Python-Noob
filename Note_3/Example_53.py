#!/bin/usr/python
# -*- coding: UTF-8 -*-

'''
题目：学习使用按位异或 ^ 。
'''

if __name__ == '__main__':
    a = 077
    b = a ^3
    print 'The a ^ 3 = %d' % b
    b ^= 7
    print 'The a ^ b = %d' % b
    
# Result
'''
The a ^ 3 = 60
The a ^ b = 59
'''
