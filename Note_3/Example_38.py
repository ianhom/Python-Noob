#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：求一个3*3矩阵对角线元素之和。
'''
 
if __name__ == '__main__':
    a = []
    sum = 0.0
    for i in range(3):
        a.append([])
        for j in range(3):
            a[i].append(float(raw_input("input num:\n")))
    for i in range(3):
        sum += a[i][i]
    print sum

# result
'''
input num:
1
input num:
2
input num:
3
input num:
4
input num:
5
input num:
6
input num:
7
input num:
8
input num:
9
15.0
'''
