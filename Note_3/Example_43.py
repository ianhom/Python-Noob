#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：模仿静态变量(static)另一案例。
'''

class Num:
    nNum = 1
    def inc(self):
        self.nNum += 1
        print 'nNum = %d' % self.nNum

if __name__ == '__main__':
    nNum = 2
    inst = Num()
    for i in range(3):
        nNum += 1
        print 'The num = %d' % nNum
        inst.inc()

# Result
'''
The num = 3
nNum = 2
The num = 4
nNum = 3
The num = 5
nNum = 4
'''
