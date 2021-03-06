#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tkinter as tk  # Use for Python3
#import Tkinter as tk  # Use for Python2
import CMG

window = tk.Tk()
window.title('Code Module Generator')
window.geometry('1000x500')

# Show the Title
l = tk.Label(window, 
    text='Code Module Generator!',    # Text of Label
    bg='white',                       # Background color
    font=('Arial', 24),               # Font and Size
    width=35, height=2)               # Size of Lable
l.pack()                              # center in winodw

# Show the input entries
Auth  = tk.StringVar()  
entry = tk.Entry(window, textvariable=Auth,width=35).pack()  
Auth.set('Please input your name here')

Cmpy  = tk.StringVar()  
entry = tk.Entry(window, textvariable=Cmpy,width=35).pack()  
Cmpy.set('Please input your company name here')

ModuleName = tk.StringVar()  
entry = tk.Entry(window, textvariable=ModuleName,width=35).pack()  
ModuleName.set('Please name your module')

Des   = tk.StringVar()  
entry = tk.Entry(window, textvariable=Des,width=35).pack()  
Des.set('Please describe this module') 

# Create a button to start generating code
def Start():
    A = Auth.get()
    C = Cmpy.get()
    M = ModuleName.get()
    D = Des.get()
    CMG.GenerateCode(A,C,M,D)
    
b = tk.Button(window, 
    text='Generate!',      # Text on the button
    width=15, height=2, 
    command = Start)       # Function called when button is pressed
b.pack()                   

window.mainloop()
