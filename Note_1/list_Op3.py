#!/usr/bin/python
# -*- coding: UTF-8 -*-

list1, list2 = [123, 'xyz'], [456, 'abc']

print cmp(list1, list2);
print cmp(list2, list1);
list3 = list2 + [786];
print cmp(list2, list3)

print max(list1);
print min(list1);

list1.append(123);  # 追加元素
print list1;

print list1.count(123);  # 统计有多少个123

print list1.index("xyz"); # 返回第一个匹配的元素位置
print list1.index(123);

list1.insert(1,456);  # 插入一个元素
print list1;
print list1.pop(-2);  # 删除一个位置的元素
print list1;
list1.remove(123);    # 删除第一个匹配的元素
print list1;
list1.reverse();      # 反转list
print list1;
list1.reverse();     
list1.insert(1,"sdfsdf");
print list1;
list1.sort();         # 排序list
print list1;

	
# result
"""
-1
1
-1
xyz
123
[123, 'xyz', 123]
2
1
0
[123, 456, 'xyz', 123]
xyz
[123, 456, 123]
[456, 123]
[123, 456]
[456, 'sdfsdf', 123]
[123, 456, 'sdfsdf']
"""
