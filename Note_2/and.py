#!/usr/bin/python

while True:
    number = input("Enter a number between 1 and 10: ");

    if number == 0:
        break;
    if number > 1 and number <= 10:
        print "Great, it is ",number;
    else:
        print "Wrong!, it is ",number;

# result
'''
Enter a number between 1 and 10: 1
Wrong!, it is  1
Enter a number between 1 and 10: 12
Wrong!, it is  12
Enter a number between 1 and 10: 0
'''
