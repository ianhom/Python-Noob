#!/usr/bin/python
# -*- coding: UTF-8 -*-

from time import *
from os   import mkdir,chdir,getcwd

common_file_head= '''/******************************************************************************
* Copyright (C) 2018 MOE
* Name   : To be done
* ID     : None
* Descrp : To be done
* Version: V1.00
* Author :      
* Date   ：To be done
******************************************************************************/'''



# Create folder named by time.
timestr =  strftime("%Y%m%d-%H%M%S", localtime())

if getcwd()[-11:] != "Code Module":
    mkdir('Code Module')
    chdir("Code Module")
print "/_/_/_/_/_/_/_/_/_/_/_/_/_//_/_/_/_/"
print "Code Module Generator V0.10"
print "/_/_/_/_/_/_/_/_/_/_/_/_/_//_/_/_/_\n"

Author_name = raw_input("May I have you name?")
module_name = raw_input("What would like to call this module?")
module_desp = raw_input("Please say something about this module")

mkdir(module_name + timestr)
chdir(module_name + timestr)

c_file = open(module_name + '.c', "w+")
h_file = open(module_name + '.h', "w+")

file_name = "* Name   : "+ module_name + ".c\n"
file_ID   = "* ID     : N/A\n"
file_desp = "* Descrp : "+ module_desp+"\n"
file_ver  = "* Version: V1.00\n"
file_Auth = "* Author : "+ Author_name+"\n"
file_date = "* Date   ："+ timestr[0:8]+"\n"
banner_bg = "/***************************************\n"
banner_ed = "***************************************/\n"

file_head = banner_bg + file_name + file_ID + file_desp + file_ver + file_Auth + file_date + banner_ed
c_file.write(file_head)

file_name = "* Name   : "+ module_name + ".c\n"
file_head = banner_bg + file_name + file_ID + file_desp + file_ver + file_Auth + file_date + banner_ed
h_file.write(file_head)

# return
c_file.close()
h_file.close()
chdir("../")
print getcwd()


