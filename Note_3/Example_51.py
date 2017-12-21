#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：学习使用按位与 & 。
'''
 
if __name__ == '__main__':
    a = 077
    b = a & 3
    print 'a & b = %d' % b
    b &= 7
    print 'a & b = %d' % b

# Result
'''
a & b = 3
a & b = 3
'''
