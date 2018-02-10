#!/usr/bin/python
# -*- coding: UTF-8 -*-

from time import *
from os   import mkdir,chdir,getcwd

# Create folder named by time.
timestr =  strftime("%Y%m%d-%H%M%S", localtime())

if getcwd()[-11:] != "Code Module":
    mkdir('Code Module')
    chdir("Code Module")

module_name = raw_input("What would like to call this module?")
mkdir(module_name + timestr)
chdir(module_name + timestr)

c_file = open(module_name + '.c', "w+")
h_file = open(module_name + '.h', "w+")


# return
c_file.close()
h_file.close()
chdir("../")
print getcwd()
