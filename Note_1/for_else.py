#!/usr/bin/python
# -*- coding: UTF-8 -*-

# for else的用法，当for能正常完成循环时，执行else语句，如果再循环中出现了break，就不执行else分支
'''
for i in range(10,20):
    if i<5:
        print i,"haha"
        break
else:
    print i,"555"
    
for i in range(10,20):
    if i<5:
        print i,"haha"
        break
    print i,"555"    
'''
 
for num in range(10,20):  # 迭代 10 到 20 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         print '%d 等于 %d * %d' % (num,i,j)
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print num, '是一个质数'
      
 '''
 10 等于 2 * 5
11 是一个质数
12 等于 2 * 6
13 是一个质数
14 等于 2 * 7
15 等于 3 * 5
16 等于 2 * 8
17 是一个质数
18 等于 2 * 9
19 是一个质数
'''
