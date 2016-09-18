#!/usr/bin/python
# -*- coding: UTF-8 -*-

list1 = [1,2,3];
list2 = ["four", "five", "six"];

print len(list1);
print list1+ list2;
print list1*4
print 3 in list1

for x in list2: print x;
	
# result
"""
3
[1, 2, 3, 'four', 'five', 'six']
[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
True
four
five
six
"""
