#!/usr/bin/python

fibs = [0,1];
num = input("How many Fibonacci numbers do you want? ");
for i in range(num - 2):
    fibs.append(fibs[-2] + fibs[-1]);
print fibs;

# result
'''
How many Fibonacci numbers do you want? 10
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
'''
