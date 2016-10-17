#!/usr/bin/python

class Filter:
    def init(self):
        "This function is useless!"
        self.blocked = [];
    def filter(self, sequence):
        "Filter rule"
        return [x for x in sequence if x not in self.blocked];

class SPAMFilter(Filter):  # SPAMFilter is child class of Filter.
    def init(self):        # Override the method of init.
        "The parent class 'init'function is over rided!"
        self.blocked = ["SPAM"];

# result
'''
f = Filter()
>>> f.init()
>>> f.filter([1,2,3])
[1, 2, 3]
>>> s = SPAMFilter()
>>> s.init()
>>> s.filter(["SPAM","SPAM","SPAM","eggs","bacon","SPAM"])
['eggs', 'bacon']
'''

        
