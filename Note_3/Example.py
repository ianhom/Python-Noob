#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：回答结果（结构体变量传递）。
'''

if __name__ == '__main__':
    n = 1
    while n <= 7:
        a = int(raw_input('input a number:\n'))
        while a < 1 or a > 50:
            a = int(raw_input('input a number:\n'))
        print a * '*'
        n += 1
    
# Result
'''
input a number:
1
*
input a number:
2
**
input a number:
3
***
input a number:
4
****
input a number:
5
*****
input a number:
6
******
input a number:
7
*******
'''
