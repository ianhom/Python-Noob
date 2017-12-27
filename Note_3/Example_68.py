#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数
'''
 
if __name__ == '__main__':
    n = int(raw_input('整数 n 为:\n'))
    m = int(raw_input('向后移 m 个位置为:\n'))
 
    def move(array,n,m):
        array_end = array[n - 1]
        for i in range(n - 1,-1,- 1):
            array[i] = array[i - 1]
        array[0] = array_end
        m -= 1
        if m > 0:move(array,n,m)
        
    number = []
    for i in range(n):
        number.append(int(raw_input('输入一个数字:\n')))
    print '原始列表:',number
 
    move(number,n,m)
 
    print '移动之后:',number


# Result
'''
整数 n 为:
5
向后移 m 个位置为:
2
输入一个数字:
2
输入一个数字:
3
输入一个数字:
4
输入一个数字:
5
输入一个数字:
6
原始列表: [2, 3, 4, 5, 6]
移动之后: [5, 6, 2, 3, 4]
'''
