#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：求100之内的素数。
'''

lower = int(input("输入区间最小值: "))
upper = int(input("输入区间最大值: "))
 
for num in range(lower,upper + 1):
    # 素数大于 1
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print(num)

# result
'''
输入区间最小值: 2
输入区间最大值: 78
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
'''
