#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
'''

a = 2.0;
b = 1.0;
l = [];
for n in range(1,21):
    b,a = a,a + b;
    l.append(a / b);
print reduce(lambda x,y: x + y,l);

# result
'''
32.2782947888
'''
