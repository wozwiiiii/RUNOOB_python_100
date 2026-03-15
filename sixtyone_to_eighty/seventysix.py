"""
题目：
编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n
"""

#自己的解法，编写三个函数进行嵌套，一个总函数（或者是程序）进行判断输入n为奇数还是偶数，判别为奇数则调用函数1，判别为偶数则调用函数2

#代码没有标准答案简洁

#判别为奇数，调用函数1
def qishu(n):
    sum_1 = 0.0

    while n >= 1:
        t = 1.0 / n
        sum_1 += t
        n -= 2
    print(sum_1)

    return sum_1        


#判别为偶数，调用函数2
def oushu(n):
    
    sum_2 = 0.0
    while n > 0:
        m = 1.0 / n 
        sum_2 += m
        n -= 2
    print(sum_2)   

    return sum_2        



#总程序
n = int(input("请输入您先要测试的数字："))    
if n % 2 == 0:
    oushu(n)
else:
    qishu(n)




#标准答案

 
def peven(n):
    i = 0
    s = 0.0
    for i in range(2,n + 1,2):
        s += 1.0 / i   # Python里，整数除整数，只能得出整数，所以需要使用 浮点数 1.0
    return s
 
def podd(n):
    s = 0.0
    for i in range(1, n + 1,2):
        s += 1.0 / i    # Python里，整数除整数，只能得出整数，所以需要使用 浮点数 1.0
    return s
 
def dcall(fp,n):
    s = fp(n)
    return s
 
if __name__ == '__main__':
    n = int(input('input a number:\n'))
    if n % 2 == 0:
        sum = dcall(peven,n)
    else:
        sum = dcall(podd,n)
    print(sum)

