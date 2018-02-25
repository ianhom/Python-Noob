#!/usr/bin/python
# -*- coding: UTF-8 -*-

from time   import *
from os     import mkdir,chdir,getcwd
from common import *

# Create folder named by time.
timestr =  strftime("%Y%m%d-%H%M%S", localtime())

if getcwd()[-11:] != "Code Module":
    mkdir('Code Module')
    chdir("Code Module")
print "/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/"
print "Code Module Generator V0.10"
print "/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/\n"

Author_name = raw_input("May I have you name?\n")
module_name = raw_input("What would like to call this module?\n")
module_desp = raw_input("Please say something about this module\n")

mkdir(module_name + "_" + timestr)
chdir(module_name + "_" + timestr)

timestr = strftime("%Y-%m-%d", localtime())

c_file = open(module_name + '.c', "w+")
h_file = open(module_name + '.h', "w+")

file_name = "* Name   : "+ module_name + ".c\n"
file_Cprt = "* Copyright (C) 2018 MOE\n"
file_ID   = "* ID     : N/A\n"
file_desp = "* Descrp : "+ module_desp+"\n"
file_ver  = "* Version: V1.00\n"
file_Auth = "* Author : "+ Author_name+"\n"
file_date = "* Date   : "+ timestr +"\n"
banner_bg = "/***************************************\n"
banner_ed = "***************************************/\n\n"

file_head = banner_bg + file_Cprt + file_name + file_ID + file_desp + file_ver + file_Auth + file_date + banner_ed

file_init = "BYTE " + module_name + "_Init(void)\n{\n\n    return SW_OK;\n}\n\n"
file_proc = "BYTE " + module_name + "_Process(BYTE ucChNo)\n{\n\n    return SW_OK;\n}\n\n"

# Make c-file
file_all = file_head + file_init + file_proc
c_file.write(file_all)

file_name = "* Name   : "+ module_name + ".c\n"
file_head = banner_bg + file_Cprt + file_name + file_ID + file_desp + file_ver + file_Auth + file_date + banner_ed

# Make h-file
file_init = "BYTE " + module_name + "_Init(void);\n\n"
file_proc = "BYTE " + module_name + "_Process(BYTE ucChNo);\n\n"

file_all = file_head + h_head_start(module_name) + h_cpp_start + file_init + file_proc + h_cpp_end + h_head_end(module_name)
h_file.write(file_all)

# Make a readme-file
r_file = open("readme.txt","w+")

# clear up
c_file.close()
h_file.close()
chdir("../")
print getcwd()

