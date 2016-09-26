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

# result
"""
The count of dog is 3
Name : John , Age : 5
3
"""
