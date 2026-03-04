"""
题目：
两个变量值互换。
"""




#法一：通过中间变量来进行互相转换
def excchange_1():
    a = int(input("please input a number: "))
    b = int(input("please input another number: "))

    temp = a
    a = b
    b = temp

    #法二：直接赋值
    """
    a,b = b,a
    """

    print(f"转换之后{a},{b}")
    return a , b

excchange_1()





#标准答案
 
def exchange(a,b):
    a,b = b,a
    return (a,b)
 
if __name__ == '__main__':
    x = 10
    y = 20
    print ('x = %d,y = %d' % (x,y))
    x,y = exchange(x,y)
    print ('x = %d,y = %d' % (x,y))
