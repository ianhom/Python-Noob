#!/usr/bin/python
# -*- coding: UTF-8 -*-

from sys import stdout

print "题目：一个数如果恰好等于它的因子之和，这个数就称为完数。例如6=1＋2＋3.编程找出1000以内的所有完数。";

for j in range(2,1001):
    k = [];
    n = -1;
    s = j;
    for i in range(1,j):
            if j % i == 0:
                n += 1;
                s -= i;
                k.append(i);
    
    if s == 0:
        print j;
        for i in range(n):
            stdout.write(str(k[i]));
            stdout.write(' ');
        print k[n];

# result
'''
题目：一个数如果恰好等于它的因子之和，这个数就称为完数。例如6=1＋2＋3.编程找出1000以内的所有完数。
6
1 2 3
28
1 2 4 7 14
496
1 2 4 8 16 31 62 124 248
'''
