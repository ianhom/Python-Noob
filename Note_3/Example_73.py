#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：反向输出一个链表。
'''
if __name__ == '__main__':
    ptr = []
    for i in range(5):
        num = int(raw_input('please input a number:\n'))
        ptr.append(num)
    print ptr
    ptr.reverse()
    print ptr

# Result
'''
please input a number:
12
please input a number:
23
please input a number:
34
please input a number:
45
please input a number:
56
[12, 23, 34, 45, 56]
[56, 45, 34, 23, 12]
'''