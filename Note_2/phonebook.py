#!/usr/bin/python

people = {

    'Alice': {
       'phone': '2341',
       'addr' : 'Foo drive 23'
    },

    'Beth' : {
       'phone': '0123',
       'addr' : 'Foo street 03'
    },
    'Cecil' : {
       'phone': '9999',
       'addr' : 'Aoti street 69'
    }
}

labels = {
    'phone': 'phone number',
    'addr' : 'address'
}

name = raw_input('name: ');

request = raw_input('Phone number(p) or address(a)?');

if request == 'p': key = 'phone';
if request == 'a': key = 'addr';

if name in people: print "%s's %s is %s." % (name, labels[key], people[name][key]);
else: print"Name is wrong!!";
