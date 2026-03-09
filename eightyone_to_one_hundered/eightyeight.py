"""
题目：
读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊。
"""
#自己的解法
test = 0
while test < 7:
    
    #进行提示，要求a<50
    a = int(input("请输入数值（1-50）："))

    #若进行判断
    #while a < 1 or a > 50:
    for i in range(1,a + 1):
        #存在错误，不能在一行显示
        print("*\t")

        #优化后
        print(a * "*")
    test += 1    


#标准答案
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
if __name__ == '__main__':
    n = 1
    while n <= 7:
        a = int(input('input a number:\n'))
        while a < 1 or a > 50:
            a = int(input('input a number:\n'))
        print(a * '*')
        n += 1