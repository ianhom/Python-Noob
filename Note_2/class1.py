#!/usr/bin/python
# -*- coding: UTF-8 -*-

class dog:
    'This is a dog class'  #函数提示
    dogcnt = 1;
    
    def __init__(self, name, age):  #构造函数
        self.name = name
        self.age  = age
        dog.dogcnt += 1
      
    def ShowCnt(self):
        print "The count of dog is %d" % dog.dogcnt
        
    def ShowDog(self):
        print "Name : ", self.name, ", Age : ", self.age
        
dog1 = dog("Mike",4)
dog2 = dog("John",5)

dog1.ShowCnt()
dog2.ShowDog()
print dog.dogcnt 

print "dog.__doc__:", dog.__doc__
print "dog.__name__:", dog.__name__
print "dog.__module__:", dog.__module__
print "dog.__bases__:", dog.__bases__
print "dog.__dict__:", dog.__dict__

# result
"""
The count of dog is 3
Name : John , Age : 5
3
dog.__doc__: This is a dog class
dog.__name__: dog
dog.__module__: __main__
dog.__bases__: ()
dog.__dict__: {'__module__': '__main__', 'ShowCnt': , 'dogcnt': 3, 'ShowDog': , '__doc__': 'This is a dog class', '__init__': }
"""
