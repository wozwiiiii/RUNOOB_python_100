"""
题目：
有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...
求出这个数列的前20项之和。
"""
#自己的解法
a = 2.0
b = 1.0
sum = 0.0
"""
for i in range(1,21):
    sum += a / b
    a = a + b
    b = a
这里有一个逻辑错误:
更新b为a后，a的新值会变成a + b，而b的新值会变成a + b，导致数列的计算不正确。
需要像法1一样添加一个中间变量过度
"""
for n in range(1,21):
    sum += a / b
    t = a
    a = a + b
    b = t
print (sum)
    
    


#标准答案
#程序分析：请抓住分子与分母的变化规律

#法1
a = 2.0
b = 1.0
s = 0
for n in range(1,21):
    s += a / b
    t = a
    a = a + b
    b = t
print (s)


#法2
a = 2.0
b = 1.0
s = 0.0
for n in range(1,21):
    s += a / b
    b,a = a , a + b
print (s)
 
s = 0.0
for n in range(1,21):
    s += a / b
    b,a = a , a + b
print (s)


#法3
 
from functools import reduce
 
a = 2.0
b = 1.0
l = []
l.append(a / b)
for n in range(1,20):
    b,a = a,a + b
    l.append(a / b)
print (reduce(lambda x,y: x + y,l))


"""
b, a = a, a + b 这一行代码使用了Python的多重赋值特性。
这意味着Python首先会评估等号右侧的表达式，然后一次性将计算结果赋值给左侧的变量。
具体步骤如下:
 1、计算右侧的表达式：先计算 a + b 的值。
 2、之后，Python会将 a 的当前值赋给 b，将刚才计算的 a + b 的值赋给 a。
"""