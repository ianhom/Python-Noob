#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：编写input()和output()函数输入，输出5个学生的数据记录。
'''
N = 3
#stu
# num : string
# name : string
# score[4]: list
student = []
for i in range(5):
    student.append(['','',[]])
 
def input_stu(stu):
    for i in range(N):
        stu[i][0] = raw_input('input student num:\n')
        stu[i][1] = raw_input('input student name:\n')
        for j in range(3):
            stu[i][2].append(int(raw_input('score:\n')))
 
def output_stu(stu):
    for i in range(N):
        print '%-6s%-10s' % ( stu[i][0],stu[i][1] )
        for j in range(3):
            print '%-8d' % stu[i][2][j]
 
if __name__ == '__main__':
    input_stu(student)
    print student
    output_stu(student)

# Result
'''
input student num:
1
input student name:
Tom
score:
100
score:
100
score:
100
input student num:
2
input student name:
Jerry
score:
99
score:
88
score:
77
input student num:
3
input student name:
Henry
score:
90
score:
60
score:
80
[['1', 'Tom', [100, 100, 100]], ['2', 'Jerry', [99, 88, 77]], ['3', 'Henry', [90, 60, 80]], ['', '', []], ['', '', []]]
1     Tom       
100     
100     
100     
2     Jerry     
99      
88      
77      
3     Henry     
90      
60      
'''
