#!/usr/bin/python
# -*- coding: UTF-8 -*-

tup1 = (12, 34.56);
tup2 = ('abc', 'xyz');

# 创建一个新的元组
tup3 = tup1 + tup2;
print tup3;

# 以下修改元组元素操作是非法的。
tup1[0] = 100;

# result
"""
(12, 34.56, 'abc', 'xyz')
Traceback (most recent call last): File "/usercode/file.py", line 12, in tup1[0] = 100; TypeError: 'tuple' object does not support item assignment 
"""
