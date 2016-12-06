#!/usr/bin/python
# -*- coding: UTF-8 -*-

print "题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。";

Tn = 0;
Sn = [];
n = int(raw_input('n = :\n'));
a = int(raw_input('a = :\n'));
for count in range(n):
    Tn = Tn + a;
    a = a * 10;
    Sn.append(Tn);
    print Tn;

Sn = reduce(lambda x,y : x + y,Sn);
print Sn;

# result
'''
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。
n = :
10
a = :
2
2
22
222
2222
22222
222222
2222222
22222222
222222222
2222222222
2469135800
'''
