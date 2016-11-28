#!/usr/bin/python
# -*- coding: UTF-8 -*-

print "题目：输出前 10 个斐波那契数列 ";


def fib(n):
    if n == 1:
        return [1];
    if n == 2:
        return [1, 1];
    fibs = [1, 1];
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2]);
    return fibs;

print fib(10);

# result
'''
题目：输出前 10 个斐波那契数列 
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
'''
