"""
题目：
一个数如果恰好等于它的因子之和，
这个数就称为"完数"。
例如6=1＋2＋3.编程找出1000以内的所有完数。
"""

#自己的解法（存在问题:只能进行判断且有重复）
from functools import reduce


def testNum(n):
    reduceNum(n)

    for i in range(1,1000):
       if lit == n:
          print(lit)
       else:
          print(f"{n}该数字不是完数")

def reduceNum(n):
    list_1 = []
    
    #isinstance 是 Python 内置的一个函数，用于判断一个对象是否是指定的类型或其子类型。
    if not isinstance(n, int) or n <= 0 :
        print ('请输入一个正确的数字 !')
        exit(0)
    elif n in [1] :
        print ('{}'.format(n))
    while n not in [1] : # 循环保证递归
        for index in range(2, n + 1) :
            if n % index == 0:
                 n //= index # n 等于 n//index
                 if n == 1: 
                    print (index )
                 else : # index 一定是素数
                    print ('{} *'.format(index), end=" ")
                 list_1.append(index) 
                 global lit
                 lit = reduce(lambda x,y : x + y,list_1)
                 break            
    return lit

testNum(90)


#标准答案
"""
解析:参考例题14"""
#sys 模块提供了与Python解释器密切相关的函数和变量。stdout是一个文件对象，代表标准输出流，默认情况下是控制台。 
from sys import stdout
for j in range(2,1001):
    k = []
    n = -1
    s = j
    for i in range(1,j):
            if j % i == 0:
                n += 1
                s -= i
                k.append(i)
    
    if s == 0:
        print (j)
        for i in range(n):
            stdout.write(str(k[i]))
            stdout.write(' ')
        print (k[n])








