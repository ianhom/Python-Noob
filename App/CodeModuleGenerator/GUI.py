#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tkinter as tk
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
Auth = tk.StringVar()  
entry = tk.Entry(window, textvariable=Auth,width=35).pack()  
Auth.set('Please input your name here')

ModuleName = tk.StringVar()  
entry = tk.Entry(window, textvariable=ModuleName,width=35).pack()  
ModuleName.set('Please name your module')

Des = tk.StringVar()  
entry = tk.Entry(window, textvariable=Des,width=35).pack()  
Des.set('Please describe this module') 

# Create a button to start generating code
def Start():
    A = Auth.get()
    M = ModuleName.get()
    D = Des.get()
    CMG.GenerateCode(A,M,D)
    
b = tk.Button(window, 
    text='Generate!',      # Text on the button
    width=15, height=2, 
    command = Start)       # Function called when button is pressed
b.pack()                   

window.mainloop()
