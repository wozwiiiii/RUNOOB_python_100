"""
题目：
将一个列表的数据复制到另一个列表中。
"""
#通过for循环遍历目标列表元素，再使用append()方法将元素添加到空白列表中
fir_list = [1, 2, 3, 4, 5]
sec_list = []
for i in fir_list:
    sec_list.append(i)
   
    print(sec_list)


 
#标准分析（答案）：使用列表[:]。
a = [1, 2, 3]
b = a[:]
print (b)