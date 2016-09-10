#!/usr/bin/python
# -*- coding: UTF-8 -*-

list = [ 'abcd', 123, 1.23, 'Ian' ]
smalllist = [ 123, 'Jane' ]

print list              # print all elements
print list[0]           # print the first element
print list[1:3]         # print the second one to the third one
print list[2:]          # print the third and following elements
print smalllist * 2     # print small list twice
print list + smalllist  # print both list

# result
""""
['abcd', 123, 1.23, 'Ian']
abcd
[123, 1.23]
[1.23, 'Ian']
[123, 'Jane', 123, 'Jane']
['abcd', 123, 1.23, 'Ian', 123, 'Jane']
""""
