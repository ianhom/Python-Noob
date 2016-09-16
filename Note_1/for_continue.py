#!/usr/bin/python
# -*- coding: UTF-8 -*-

for letter in 'Python':     # 第一个实例
   if letter == 'o':
      continue;
   print '当前字母 :', letter;

var = 10                    # 第二个实例
while var > 0:              
   var = var -1;
   if var == 3:
      continue
   print '当前变量值 :', var;
print "End";

# result
"""
当前字母 : P
当前字母 : y
当前字母 : t
当前字母 : h
当前字母 : n
当前变量值 : 9
当前变量值 : 8
当前变量值 : 7
当前变量值 : 6
当前变量值 : 5
当前变量值 : 4
当前变量值 : 2
当前变量值 : 1
当前变量值 : 0
End
"""
