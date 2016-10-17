#!/usr/bin/python

class Secretive:
    def __inaccessible(self):
        'Inaccessible function';
        print "Bet you can't see me...";

    def accessible(self):
        'Accessible function';
        print "The secret message is: ";
        self.__inaccessible();

# result
'''
>>> s = Secretive()
>>> s.__inaccessible()

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    s.__inaccessible()
AttributeError: Secretive instance has no attribute '__inaccessible'
>>> s.accessible()
The secret message is: 
Bet you can't see me...
>>> s._Secretive__inaccessible()
Bet you can't see me...
'''
