#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tkinter as tk

window = tk.Tk()
window.title('Babies Love Python')
window.geometry('1000x500')

l = tk.Label(window, 
    text='Babies Love Python!',    # 标签的文字
    bg='white',     # 背景颜色
    font=('Arial', 24),     # 字体和字体大小
    width=15, height=2  # 标签长宽
    )
l.pack()    # 固定窗口位置


def Start():
 print("Hello")
    
b = tk.Button(window, 
    text='Start!',      # 显示在按钮上的文字
    width=15, height=2, 
    command = Start)     # 点击按钮式执行的命令
b.pack()    # 按钮位置


# 这里是窗口的内容

window.mainloop()
