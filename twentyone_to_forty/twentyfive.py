"""
题目：
求1+2!+3!+...+20!的和。
"""

#自己的解法,没有展示每个具体的元素

def base(len):
    num = 1
    sum = 0
    for i in range(1,len + 1):
        num *= i 
        sum += num
    print(sum)
    return sum
base(20) 


#标准答案
#程序分析：此程序只是把累加变成了累乘。
 
s = 0
l = range(1,21)
def op(x):
    r = 1
    for i in range(1,x + 1):
        r *= i
    return r

#使用map方法来处理序列 l。map(op, l)的作用是将 op 函数应用到 l 中的每个元素上，生成一个新的迭代器。
#这个迭代器包含每个元素的阶乘值
s = sum(map(op,l))
print ('1! + 2! + 3! + ... + 20! = %d' % s)
    