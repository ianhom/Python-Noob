#!/usr/bin/python
# -*- coding: UTF-8 -*-

a = "Hello"
b = "Python"

print "a + b 输出结果：", a + b 
print "a * 2 输出结果：", a * 2 
print "a[1] 输出结果：", a[1] 
print "a[1:4] 输出结果：", a[1:4] 

if( "H" in a) :
    print "H 在变量 a 中" 
else :
	print "H 不在变量 a 中" 

if( "M" not in a) :
    print "M 不在变量 a 中" 
else :
	print "M 在变量 a 中"

print r'\n'   # 打印r之后的原始内容 
print R'\n'   # 打印R之后的原始内容

# result
"""
a + b 输出结果： HelloPython
a * 2 输出结果： HelloHello
a[1] 输出结果： e
a[1:4] 输出结果： ell
H 在变量 a 中
M 不在变量 a 中
\n
\n
"""
