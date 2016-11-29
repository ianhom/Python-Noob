#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time

print "题目：暂停一秒输出。 ";

print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

print "此处暂停一秒";
time.sleep(1)


print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

# result
'''
题目：暂停一秒输出。 
2016-11-29 17:42:56
此处暂停一秒
2016-11-29 17:42:57
'''
