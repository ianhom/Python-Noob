#!/usr/bin/python
# -*- coding: UTF-8 -*-

f = open("hi.txt", "w");
str = "人生苦短，我用python"

f.write(str);

f.close();

e = open("hi.txt","r");
line = e.readline();

e.close();
print line;

# Result
'''
浜虹敓鑻︾煭锛屾垜鐢╬ython
'''
