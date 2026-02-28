"""
题目：将一个数组逆序输出。
"""
#自己的解法，通过操作的列表方法实现倒序输出
num_list = []
test = True
while test:
    i = int(input("请输入数组的元素:"))
    num_list.append(i)
    if len(num_list) >= 3:
        test = False

print(num_list[::-1])
print(list(reversed(num_list)))



#标准答案，解析：用第一个与最后一个交换。 
if __name__ == '__main__':
    a = [9,6,5,4,1]
    N = len(a) 
    print (a) 
    for i in range(len(a) // 2):
        a[i],a[N - i - 1] = a[N - i - 1],a[i]
    print (a)


