#!/usr/bin/python
# -*- coding: UTF-8 -*-

tup1 = (12, 34.56);
tup2 = ('abc', 'xyz');
list = [1,2,3,4,5];

# 创建一个新的元组
tup3 = tup1 + tup2;
print tup3;

del tup3;

tup3 = tup1 + tup2;

print tup3[2];
print tup3[-1];
print tup3[1:];

print cmp(tup1,tup2);
print max(tup1,tup2);
print min(tup1,tup2);
print tuple(list);


# 以下修改元组元素操作是非法的。
tup1[0] = 100;

# result
"""
(12, 34.56, 'abc', 'xyz')
abc
xyz
(34.56, 'abc', 'xyz')
-1
('abc', 'xyz')
(12, 34.56)
(1, 2, 3, 4, 5)
Traceback (most recent call last): File "/usercode/file.py", line 27, in tup1[0] = 100; TypeError: 'tuple' object does not support item assignment 
"""
