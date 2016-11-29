#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time

print "题目：暂停一秒输出。 ";

myD = {1: 'a', 2: 'b'};
for key, value in dict.items(myD):
	print key, value;
	time.sleep(1); # 暂停 1 秒
	print "此处暂停 1 秒";

# result
'''
题目：暂停一秒输出。 
1 a
此处暂停 1 秒
2 b
此处暂停 1 秒
'''
