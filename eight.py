""""
题目：
输出 9*9 乘法口诀表。
"""
#存在位置不对齐的情况
for i in range(1,10):
    for j in range(1,10):
        print(f"{i}*{j}={i*j}\t",end="")
        j += 1
    i += 1


 
#标准解析：分行与列考虑，共9行9列，i控制行，j控制列。
for i in range(1, 10):
    print() 
    for j in range(1, i+1):
        print ("%d*%d=%d" % (i, j, i*j), end=" " )

#多种方法

#for循环
#外层循环控制行数
for i in range(1,10):
    #内层循环控制每一行内容
    for j in range(1,i+1):
        print(f"{j}*{i}={j*i}\t",end='')

    #外层循环通过print()输出一个回车符    
    print()        


#while循环
#定义外侧循环控制量
i = 1

while i <= 9:

    #定义内层循环控制量
    j = 1
    while j <= i:
        print(f"{j}*{i}={j*i}\t",end='')  
        j += 1
    i += 1
    print()    #输出空内容，就是输出一个换行        
