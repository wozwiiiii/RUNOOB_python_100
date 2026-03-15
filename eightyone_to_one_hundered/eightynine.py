"""
题目：
某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，
加密规则如下：每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。
"""
#自己的解法含注释

#输入四位整数
b = int(input("请输入四个数字："))

#创建空列表
b_add = []

#将四位数通过取余和取整操作添加到列表中，再对于列表元素进行操作
b_add.append(b % 10)
b_add.append(b % 100 / 10)
b_add.append(b % 1000 // 100)
b_add.append(b % 10000 // 1000)

#将列表中每个数字加上5,并用和除以10的余数代替数字
for i in range(4):
    b_add[i] += 5
    b_add[i] %= 10
    
#将第一位和第四位，第二位和第三位交换
for j in range(2):
    b_add[i] , b_add[3 - i] = b_add[3 - i], b_add[i] 

#输出
for m in b_add:
    print(m)







#标准答案

 
from sys import stdout
if __name__ == '__main__':
    a = int(input('输入四个数字:\n'))
    aa = []
    aa.append(a % 10)
    aa.append(a % 100 / 10)
    aa.append(a % 1000 / 100)
    aa.append(a / 1000)
 
    for i in range(4):
        aa[i] += 5
        aa[i] %= 10
    for i in range(2):
        aa[i],aa[3 - i] = aa[3 - i],aa[i]
    for i in range(3,-1,-1):
        stdout.write(str(aa[i]))
