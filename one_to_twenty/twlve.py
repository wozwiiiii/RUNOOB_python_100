"""
题目：
判断101-200之间有多少个素数，并输出所有素数。
"""
#自己的解法：定义一个存储单位，遍历101-200之间的所有数字，
#并依据素数除了自己及1之外没有其他因数的特性再次构成一个循环并判断，再将元素加入存储单位并计数

list_1 = []
for i in range(101,201):
    test = True
    for j in range(2,i):
        #判断i能否被j整除，如果能则i不是素数
        if i % j == 0:
            test = False
            break
    if test:
        list_1.append(i)

        
    """
    存在问题：由于循环出现大量重复元素
        if i % j == 0: 
            break
        else:
            list_1.append(i) 
    """    

        
print(f"{list_1},总数为{len(list_1)}")    



#标准答案 
#程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。
h = 0
leap = 1
from math import sqrt
from sys import stdout
for m in range(101,201):
    k = int(sqrt(m + 1))
    for i in range(2,k + 1):
        if m % i == 0:
            leap = 0
            break
    if leap == 1:
        print ('%-4d' % m)
        h += 1
        if h % 10 == 0:
            print ('')
    leap = 1
print ('The total is %d' % h)