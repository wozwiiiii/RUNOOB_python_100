"""
题目：
利用条件运算符的嵌套来完成此题：
学习成绩>=90分的同学用A表示，
60-89分之间的用B表示，
60分以下的用C表示。
"""
#自己的解法(基于答案进行了一定优化)
while True:
    score = int(input("请输入对应学生具体成绩："))
    if score >= 90:
        grade = 'A'
        print(f"该同学评分为{grade}")
    elif 60 <= score <= 89:
        grade = 'B'
        print(f"该同学评分为{grade}")
    else:
        grade = 'C'
        print(f"该同学评分为{grade}")
    print(f"该同学成绩为：{score}，对应评分为{grade}")        


#标准答案，程序分析：(a>b) ? a:b 这是条件运算符的基本例子。
score_2 = int(input('输入分数:\n'))
if score_2 >= 90:
    grade = 'A'
elif score_2 >= 60:
    grade = 'B'
else:
    grade = 'C'
 
print ('%d 属于 %s' % (score,grade))

