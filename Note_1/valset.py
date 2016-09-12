#!/usr/bin/python
# -*- coding: UTF-8 -*-

a = 5
b = 4
c = 0

c = a + b
print "1 - c 的值为：", c

c += a
print "2 - c 的值为：", c 

c *= a
print "3 - c 的值为：", c 

c /= a 
print "4 - c 的值为：", c 

c = 2
c %= a
print "5 - c 的值为：", c

c **= a
print "6 - c 的值为：", c

c //= a
print "7 - c 的值为：", c

# result
"""
1 - c 的值为： 9
2 - c 的值为： 14
3 - c 的值为： 70
4 - c 的值为： 14
5 - c 的值为： 2
6 - c 的值为： 32
7 - c 的值为： 6
"""
