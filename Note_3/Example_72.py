#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：创建一个链表。
'''
if __name__ == '__main__':
    ptr = []
    for i in range(5):
        num = int(raw_input('please input a number:\n'))
        ptr.append(num)
    print ptr

# Result
'''
please input a number:
2
please input a number:
3
please input a number:
4
please input a number:
5
please input a number:
6
[2, 3, 4, 5, 6]
'''
