#!/usr/bin/python

while True:
    word = raw_input("Please enter a word: ");
    if not word:
        break;
    print "The word was " + word;

# result
'''
Please enter a word: Hi
The word was Hi
Please enter a word: Hello
The word was Hello
Please enter a word: World
The word was World
Please enter a word: 
'''
