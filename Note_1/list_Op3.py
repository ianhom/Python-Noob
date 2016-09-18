#!/usr/bin/python
# -*- coding: UTF-8 -*-

list1, list2 = [123, 'xyz'], [456, 'abc']

print cmp(list1, list2);
print cmp(list2, list1);
list3 = list2 + [786];
print cmp(list2, list3)

print max(list1);
print min(list1);
	
# result
"""
-1
1
-1
xyz
123
"""
