#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
一筐鸡蛋：
1个1个拿，正好拿完。
2个2个拿，正好拿完。
3个3个拿，正好拿完。
4个4个拿，还剩2个。
5个5个拿，还剩4个。
6个6个拿，正好拿完。
7个7个拿，还剩5个。
8个8个拿，还剩2个。
9个9个拿，正好拿完。
问筐里有多少鸡蛋？
'''

i = 0
a = [0,1,0,1,1,3,0,1,0]

while(1):
    i += 1
    for b in range(1,len(a)+1):
        if (i % b) != a[b - 1]:
            break
    else:
        print i
        break

# result
'''
441
'''
