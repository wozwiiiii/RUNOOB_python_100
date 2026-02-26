"""
题目：
斐波那契数列。
（斐波那契数列是一个由0和1开始的数列，
后续每一项都是前两项之和，
其数列为：0、1、1、2、3、5、8、13、21、34……）
"""

"""
分析：
F0 = 0     (n=0)
F1 = 1    (n=1)
Fn = F[n-1]+ F[n-2](n=>2)
"""


"""
直接使用循环会导致下标与元素两者相互混乱，导致代码写到一半混乱
li_number = int(input("请输入最大限制："))
list_1 = 1
total = 0
if li_number >= 2:
    for i in range(0,li_number+1):
        total += 
"""


#法一：定义函数进行递归操作
def fin(n):
    if n == 1 or n == 2:
        return 1
    return fin(n-1) + fin(n-2)   
print(fin(3))     


