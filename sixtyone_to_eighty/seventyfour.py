"""
题目：
列表排序及连接。
"""
#自己的解法

a = [1, 3, 8, 6, 7]
print(a)

b = [3, 6, 9, 8, 7]

#列表排序
a.sort()
print(a)

print(b)

#列表连接
for i in a:
    b.append(i)
print(b)    



#标准答案
#程序分析：排序可使用 sort() 方法，连接可以使用 + 号或 extend() 方法。

 
if __name__ == '__main__':
    a = [1,3,2]
    b = [3,4,5]
    a.sort()     # 对列表 a 进行排序
    print(a)
 
    # 连接列表 a 与 b
    print(a+b)
    
    # 连接列表 a 与 b
    a.extend(b)
    print(a)