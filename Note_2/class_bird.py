#!/usr/bin/python

class Bird:
    song = "Squaawk!";
    def sing(self):
        "This is a function of bird singing."
        print self.song;

bird = Bird();
print bird.sing.__doc__;
bird.sing();
print;

birdsong = bird.sing;
print birdsong.__doc__;
birdsong();

# result
'''
This is a function of bird singing.
Squaawk!

This is a function of bird singing.
Squaawk!
'''

