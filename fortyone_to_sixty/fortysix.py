"""
题目：
求输入数字的平方，如果平方运算后小于 50 则退出。
"""

#自己的解法
def test():
    b = True
    while b:
        num = int(input("please input a number:\t"))
        a = num ** 2
        if a < 50:
            b = False
        print("输入导出符合规范，无需再次输入")   

test()        


#标准答案

 
TRUE = 1
FALSE = 0
def SQ(x):
    return x * x
print ('如果输入的数字小于 50，程序将停止运行。')
again = 1
while again:
    num = int(input('请输入一个数字：'))
    print ('运算结果为: %d' % (SQ(num)))
    if SQ(num) >= 50:
        again = TRUE
    else:
        again = FALSE

