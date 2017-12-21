#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：学习使用按位或 | 。
'''
 
if __name__ == '__main__':
    a = 077
    b = a | 3
    print 'a | b is %d' % b
    b |= 7
    print 'a | b is %d' % b

# Result
'''
a | b is 63
a | b is 63
'''
