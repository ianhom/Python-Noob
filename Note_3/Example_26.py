#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
利用递归方法求5!。
'''
 
def fact(j):
    sum = 0
    if j == 0:
        sum = 1
    else:
        sum = j * fact(j - 1)
    return sum
 
for i in range(5):
    print '%d! = %d' % (i,fact(i))

# result
'''
0! = 1
1! = 1
2! = 2
3! = 6
4! = 24
'''
