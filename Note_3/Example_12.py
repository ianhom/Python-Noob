#!/usr/bin/python
# -*- coding: UTF-8 -*-

h = 0;
leap = 1;
from math import sqrt
from sys import stdout

print "题目：判断101-300之间有多少个素数，并输出所有素数。";
for m in range(101,301):
    k = int(sqrt(m + 1))
    for i in range(2,k + 1):
        if m % i == 0:
            leap = 0;
            break;
    if leap == 1:
        print '%-4d' % m;
        h += 1;
        if h % 10 == 0:
            print '';
    leap = 1;
print 'The total is %d' % h;

# result
'''
题目：判断101-300之间有多少个素数，并输出所有素数。
101 
103 
107 
109 
113 
127 
131 
137 
139 
149 

151 
157 
163 
167 
173 
179 
181 
191 
193 
197 

199 
211 
223 
227 
229 
233 
239 
241 
251 
257 

263 
269 
271 
277 
281 
283 
293 
The total is 37
'''
