"""
题目：
求s=a+aa+aaa+aaaa+aa...a的值，
其中a是一个数字。
例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
"""


"""
第一次错误示例：
错误理解题意，将限制次数及初始数字混淆
x = int(input("请输入限制数量级："))
i = 0
s = 0
while i < x:
    s += i* (10^(x))
    i += 1
    x -= 1

print(s)
"""


#自己的重新解法

#定义次数和初始数字
x = int(input("请输入次数："))
y = int(input("请输入初始数："))

#定义每次的数字和
sum_1 = 0
num = 0

#存储每次的数字和
sn_1 = []

#通过两个循环实现输出每个数字及相加
for i in range(x):
    sum_1 += y
    y = y * 10
    sn_1.append(sum_1)
    print(sn_1)

for j in range(x):
    num += sn_1[j]
    print(num)



#标准答案，解析；关键是计算出每一项的值

#使用了functools模块中的reduce 函数。reduce函数的作用是对序列中的元素进行累积操作
from functools import reduce
 
Tn = 0
Sn = []
n = int(input('n = '))
a = int(input('a = '))
for count in range(n):
    Tn = Tn + a
    a = a * 10
    Sn.append(Tn)
    print (Tn)

"""
从列表 Sn 中取出前两个元素，将它们相加，然后将结果与下一个元素相加，
如此反复，直到列表中的所有元素都被累加到一起，最终得到一个总的和 
"""
Sn = reduce(lambda x,y : x + y,Sn)
print ("计算和为：",Sn)



