"""
题目：
输入3个数a,b,c，按大小顺序输出。
"""
#自己的解法，通过两个循环实现，一个循环实现三个数字的输入，一个循环实现排列（将输入数字转换为列表，再对于列表进行排序）

#定义初始值
temp = 0
num = []

#实现数字输入，并转换为列表
for i in range(3):
    m = int(input(f"请输入第{i}个数：\n"))
    num.append(m)

#实现排列
for i in range(3):
    for j in range(i + 1, len(num)):
        if num[i] < num[j]:
            temp = num[i]
            num[i] = num[j]
            num[j] = temp

            #更加简洁的表达式：num[i],num[j] = num[j],num[i]

#循环打印输出            
for n in range(3):
    print(num[n])



#标准答案
#经过修改符合python3.12.7版本
 
if __name__ == '__main__':
    n1 = int(input('n1 = :\n'))
    n2 = int(input('n2 = :\n'))
    n3 = int(input('n3 = :\n'))
 
    def swap(p1,p2):
        return p2,p1
 
    if n1 > n2 : n1,n2 = swap(n1,n2)
    if n1 > n3 : n1,n3 = swap(n1,n3)
    if n2 > n3 : n2,n3 = swap(n2,n3)
 
    print(n1,n2,n3)









