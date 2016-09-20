#!/usr/bin/python
# -*- coding: UTF-8 -*-

def AddOp(a, *v):
	t = a;
	for val in v:
		t += val;
		print t;
	print;
	return t;

AddOp(10,1);
AddOp(1,2,3,4,5);
AddOp(123,12,4,23,56,567,5,3,42,4,5645,64,52,423,434,423,99);

# result

"""
11

3
6
10
15

135
139
162
218
785
790
793
835
839
6484
6548
6600
7023
7457
7880
7979

"""
