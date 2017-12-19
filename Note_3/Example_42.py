#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：学习使用auto定义变量的用法。
'''

num = 2
def autofunc():
    num = 1
    print 'internal block num = %d' % num
    num += 1
for i in range(3):
    print 'The num = %d' % num
    num += 1
    autofunc()


# Result
'''
The num = 2
internal block num = 1
The num = 3
internal block num = 1
The num = 4
internal block num = 1
'''
