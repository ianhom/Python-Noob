#!/usr/bin/python

names = ["anne", "beth", "george", "damon"];
ages  = [12,45,32,102]

for i in range(len(names)):
    print names[i], "is", ages[i], "years old";
print;

for name, age in zip(names, ages):
    print name, "is", age, "years old"

# result
'''
anne is 12 years old
beth is 45 years old
george is 32 years old
damon is 102 years old

anne is 12 years old
beth is 45 years old
george is 32 years old
damon is 102 years old
'''
