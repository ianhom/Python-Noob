#!/usr/bin/python

database = [
    ['albert',  '1234'],
    ['dilbert', '2342'],
    ['smith',   '3423'],
    ['jones',   '9843']
];
usrname = raw_input("User name: ");
pin     = raw_input("PIN code: ");

if [usrname, pin] in database:
    print "Access granted";
else:
    print "Wrong user name or PIN";


