#!/usr/bin/python

def fibs(num):
    'This function output fibs'
    result = [0,1];
    for i in range(num-2):
        result.append(result[-2]+result[-1]);
    return result

print fibs(20);

# result
'''
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]
>>> fibs(3)
[0, 1, 1]
>>> fibs(10)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
>>> fibs.__doc__
'This function output fibs'
>>> help(fibs)
Help on function fibs in module __main__:

fibs(num)
    This function output fibs
'''
