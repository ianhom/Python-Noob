#!/usr/bin/python

a = [2,3,1,5,4];
b = a;
b.sort();
print a;
print b;
print

a = [2,3,1,5,4];
b = a[:];
b.sort();
print a;
print b;
print

a = [2,3,1,5,4];
b = sorted(a);
print a;
print b;

# result
'''
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]

[2, 3, 1, 5, 4]
[1, 2, 3, 4, 5]

[2, 3, 1, 5, 4]
[1, 2, 3, 4, 5]
'''
