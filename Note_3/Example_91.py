#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：时间函数举例1
'''

if __name__ == '__main__':
    import time
    print time.ctime(time.time())
    print time.asctime(time.localtime(time.time()))
    print time.asctime(time.gmtime(time.time()))



# Result
'''
Fri Jan 05 19:08:40 2018
Fri Jan 05 19:08:40 2018
Fri Jan 05 11:08:40 2018
'''
