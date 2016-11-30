#!/usr/bin/python
# -*- coding: UTF-8 -*-

print "题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5";

def reduceNum(n):
    print '{} = '.format(n),
    if not isinstance(n, int) or n <= 0 :
        print '请输入一个正确的数字 !'
        exit(0)
    elif n in [1] :
        print '{}'.format(n)
    while n not in [1] : # 循环保证递归
        for index in xrange(2, n + 1) :
            if n % index == 0:
                n /= index # n 等于 n/index
                if n == 1: 
                    print index 
                else : # index 一定是素数
                    print '{} *'.format(index),
                break;
reduceNum(90);
reduceNum(100);

# result
'''
题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5
90 =  2 * 3 * 3 * 5
100 =  2 * 2 * 5 * 5
>>> reduceNum(110)
110 =  2 * 5 * 11
'''
