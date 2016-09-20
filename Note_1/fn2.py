#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
# 可写函数说明
def changeme( mylist ):
   "修改传入的列表"
   mylist.append([1,2,3,4]);
   print "mylist in fn: ", mylist
   return
 
def lenof(l):
	"列表的长度"
	print len(l);
	return;

def AddOp(a,b,c):
	c = a + b;
	print c;
	return c;
	
# 调用changeme函数
mylist = [10,20,30];
a = 10;
b = 20;
c = 0;
print "mylist init:", mylist;
changeme( mylist );
print "mylist after: ", mylist;
lenof(mylist);
AddOp(a,b,c);
print c;
c = AddOp(a,b,c);
print c;

# result
"""
mylist init: [10, 20, 30]
mylist in fn: [10, 20, 30, [1, 2, 3, 4]]
mylist after: [10, 20, 30, [1, 2, 3, 4]]
4
30
0
30
30
"""
