"""
题目：对10个数进行排序
"""

#自己的解法，通过插入排序算法进行排序

#添加元素进入列表
test_list = []
while (len(test_list) <= 5):
    a = int(input("输入排列元素："))
    test_list.append(a)

#排序
for i in range(len(test_list)):
    temp = test_list[i]
    j = i

    while j > 0 and test_list[j - 1] > temp:
        test_list[j] = test_list[j - 1]
        j -= 1 
    test_list[j] = temp

print(test_list)          



#标准答案
#程序分析：可以利用选择法，即从后9个比较过程中，选择一个最小的与第一个元素交换，下次类推，即用第二个元素与后8个进行比较，并进行交换。
 
if __name__ == "__main__":
    N = 10
    # input data
    print ('请输入10个数字:\n')
    l = []
    for i in range(N):
        l.append(int(input('输入一个数字:\n')))
    print
    for i in range(N):
        print (l[i])
    print
 
    # 排列10个数字
    for i in range(N - 1):
        min = i
        for j in range(i + 1,N):
            if l[min] > l[j]:min = j
        l[i],l[min] = l[min],l[i]
    print ('排列之后：')
    for i in range(N):
        print (l[i])
