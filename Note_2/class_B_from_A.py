#!/usr/bin/python

class A:
    def hello(self):
        "This is a function from A"
        print "Hello, I'm A.";

class B(A):
    pass

a = A();
b = B();
a.hello();
b.hello();

# result
'''
Hello, I'm A.
Hello, I'm A.
'''
