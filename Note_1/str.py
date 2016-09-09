#!/usr/bin/python
# -*- coding: UTF-8 -*-

str = '01234566789!'

print str # 输出完整字符串
print str[0] # 输出字符串中的第一个字符
print str[2:5] # 输出字符串中第三个至第五个之间的字符串
print str[2:] # 输出从第三个字符开始的字符串
print str * 2 # 输出字符串两次
print str + "TEST" # 输出连接的字符串 

# 运行结果
"""
01234566789!
0
234
234566789!
01234566789!01234566789!
01234566789!TEST
"""
