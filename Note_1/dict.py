#!/usr/bin/python
# -*- coding: UTF-8 -*-

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
dict2 = {'fruit': 'Apple','price': 20};
 
dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School"; # Add new entry
 
 
print "dict['Age']: ", dict['Age'];
print "dict['School']: ", dict['School'];

print dict;
print cmp(dict,dict2);
print len(dict);
print str(dict);
print type(dict);

print dict.values();

# result
"""
dict['Age']: 8
dict['School']: DPS School
{'School': 'DPS School', 'Age': 8, 'Name': 'Zara', 'Class': 'First'}
1
4
{'School': 'DPS School', 'Age': 8, 'Name': 'Zara', 'Class': 'First'}

['DPS School', 8, 'Zara', 'First']
"""
