#!/usr/bin/python

class Calculator:
    def calculate(self, expression):
        "Calculate the value of expression";
        self.value = eval(expression);

class Talker:
    def talk(self):
        "Print the value"
        print "Hi, my value is ", self.value;

class TalkingCalculator(Calculator, Talker):
    pass;

# result
'''
>>> tc = TalkingCalculator()
>>> tc.calculate("1+2+3+4")
>>> tc.talk()
Hi, my value is  10
'''
