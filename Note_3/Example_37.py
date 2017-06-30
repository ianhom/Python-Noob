#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：对10个数进行排序。
'''

if __name__ == "__main__":
    N = 10
    # input data
    print '请输入10个数字:\n'
    l = []
    for i in range(N):
        l.append(int(raw_input('输入一个数字:\n')))
    print
    for i in range(N):
        print l[i]
    print
 
    # 排列10个数字
    for i in range(N - 1):
        min = i
        for j in range(i + 1,N):
            if l[min] > l[j]:min = j
        l[i],l[min] = l[min],l[i]
    print '排列之后：'
    for i in range(N):
        print l[i]

# result
'''
请输入10个数字:

输入一个数字:
2
输入一个数字:
5
输入一个数字:
23
输入一个数字:
45
输入一个数字:
73
输入一个数字:
23
输入一个数字:
7
输入一个数字:
325
输入一个数字:
3
输入一个数字:
4

2
5
23
45
73
23
7
325
3
4

排列之后：
2
3
4
5
7
23
23
45
73
325
'''
