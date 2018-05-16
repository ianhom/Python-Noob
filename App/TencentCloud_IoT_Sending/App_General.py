#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import time
import json
from RestAPI.iotcloud import IoTCloud
import Tkinter as tk  # Use for Python2

region    = 'gz'  # 目前只能填写gz
secretId  = '请至控制台‘API密钥’处创建并填写此处'
secretkey = '请至控制台‘API密钥’处创建并填写此处'

i = IoTCloud(region,secretId,secretkey)

window = tk.Tk()
window.title('LiteOS IoT to TencentCloud')
window.geometry('600x400')

# Show the Title
l = tk.Label(window, 
    text='LiteOS IoT to TencentCloud',# Text of Label
    bg='white',                       # Background color
    font=('Arial', 24),               # Font and Size
    width=35, height=2)               # Size of Lable
l.pack()                              # center in winodw

# Show the input entries
proID  = tk.StringVar()  
entry = tk.Entry(window, textvariable=proID,width=35).pack()  
proID.set('Please input the Product ID here...')

devID  = tk.StringVar()  
entry = tk.Entry(window, textvariable=devID,width=35).pack()  
devID.set('Please input the Device Name here...')

datastr  = tk.StringVar()  
entry = tk.Entry(window, textvariable=datastr,width=35).pack()  
datastr.set('Please input the string to be sent here...')

# Create a button to start generating code
def Start():
    i.publish(proID.get()+'/'+devID.get()+'/control', datastr.get(), proID.get(), devID.get())
    

b = tk.Button(window, 
    text='Send to STM32 with LiteOS!',          # Text on the button
    width=25, height=2, 
    command = Start)       # Function called when button is pressed
b.pack()                   

window.mainloop()


