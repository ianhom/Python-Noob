#!/usr/bin/python
# -*- coding: UTF-8 -*-

import string

print "题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。";

s = raw_input('input a string:\n');
letters = 0;
space = 0;
digit = 0;
others = 0;
for c in s:
    if c.isalpha():
        letters += 1;
    elif c.isspace():
        space += 1;
    elif c.isdigit():
        digit += 1;
    else:
        others += 1;
print 'char = %d,space = %d,digit = %d,others = %d' % (letters,space,digit,others);

# result
'''
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
input a string:
Hello world * 123$%^&*()
char = 10,space = 3,digit = 3,others = 8
'''
