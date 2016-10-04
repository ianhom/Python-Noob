#!/usr/bin/python

name = raw_input("What is your name? ");
if name.endswith("Gumby"):
    if name.startswith("Mr."):
        print "Hello, Mr. Gumby";
    elif name.startswith("Mrs."):
        print "Hello, Mrs. Gumby";
    else:
        print "Hello, Gumby";
else:
    print "Hello, stranger!";

# result
'''
What is your name? Mr. Gumby
Hello, Mr. Gumby

What is your name? Mrs. Gumby
Hello, Mrs. Gumby

What is your name? Gumby
Hello, Gumby

What is your name? Ian
Hello, stranger!

'''
