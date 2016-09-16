#!/usr/bin/python
# -*- coding: UTF-8 -*-

letter = ["A","B","C","D"];
for i in range(len(letter)):
	print "The letter is ", letter[i];
print "--------------------";
for i in range(len(letter)-1):
	print "The letter is ", letter[i];
print "--------------------";
for i in range(len(letter)-1):
	print "The letter is ", letter[i+1];
print "end";

# result
"""
The letter is A
The letter is B
The letter is C
The letter is D
--------------------
The letter is A
The letter is B
The letter is C
--------------------
The letter is B
The letter is C
The letter is D
end
"""
