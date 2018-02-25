#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tkinter as tk
import CMG

window = tk.Tk()
window.title('Code Module Generator')
window.geometry('1000x500')

l = tk.Label(window, 
    text='Code Module Generator!',    # 标签的文字
    bg='white',     # 背景颜色
    font=('Arial', 24),     # 字体和字体大小
    width=35, height=2  # 标签长宽
    )
l.pack()    # 固定窗口位置

#'''
Auth = tk.StringVar()  
entry = tk.Entry(window, textvariable=Auth,width=35).pack()  
Auth.set('Please input your name here')

ModuleName = tk.StringVar()  
entry = tk.Entry(window, textvariable=ModuleName,width=35).pack()  
ModuleName.set('Please name your module')

Des = tk.StringVar()  
entry = tk.Entry(window, textvariable=Des,width=35).pack()  
Des.set('Please describe this module') 


def Start():
    A = Auth.get()
    M = ModuleName.get()
    D = Des.get()
    CMG.GenerateCode(A,M,D)
#'''

    
b = tk.Button(window, 
    text='Start!',      # 显示在按钮上的文字
    width=15, height=2, 
    command = Start)     # 点击按钮式执行的命令
b.pack()    # 按钮位置


# 这里是窗口的内容

window.mainloop()
