"""
题目：
编写input()和output()函数输入，输出5个学生的数据记录。
"""
#自己的解法，首先考虑两个函数输入参数的设置（均为学生名字），分别设置两个函数功能：input()函数进行存储学生名字及成绩，output()函数进行学生数据输出








#标准答案

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
        stu[i][0] = input('input student num:\n')
        stu[i][1] = input('input student name:\n')
        for j in range(3):
            stu[i][2].append(int(input('score:\n')))
 
def output_stu(stu):
    for i in range(N):
        print('%-6s%-10s' % ( stu[i][0],stu[i][1] ))
        for j in range(3):
            print('%-8d' % stu[i][2][j])
 
if __name__ == '__main__':
    input_stu(student)
    print(student)
    output_stu(student)