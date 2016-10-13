#!/usr/bin/python

def factorial_1(n):
    'Do factorial with for operation'
    result = n;
    for i in range(1,n):
        result *= i;
    return result;

def factorial_2(n):
    'Do factorial with recursion'
    if n == 1:
        return 1;
    else:
        return n * factorial_2(n-1);
    return result

def factorial_test(n):
    'Compare two functions with the result'
    print factorial_1(n);
    print factorial_2(n);
    return;

print "Let's try 10:"
factorial_test(10);

# result
'''
Let's try 10:
3628800
3628800
'''
