#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：时间函数举例3。
'''

if __name__ == '__main__':
    import time
    start = time.clock()
    for i in range(10000):
        print i
    end = time.clock()
    print 'different is %6.3f' % (end - start)

# Result
'''
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
.....
'''
