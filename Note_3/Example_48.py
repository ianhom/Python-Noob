#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：数字比较。
'''
if __name__ == '__main__':
    i = 123
    j = 456
    if i > j:
        print '%d 大于 %d' % (i,j)
    elif i == j:
        print '%d 等于 %d' % (i,j)
    elif i < j:
        print '%d 小于 %d' % (i,j)
    else:
        print '未知'

# Result
'''
123 大于 456
'''
