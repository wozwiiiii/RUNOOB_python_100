"""
题目：求一个3*3矩阵主对角线元素之和。
"""
#自己的解，设置3*3矩阵通过遍历循环实现主对角线元素相加
m = 0
test = [[1, 0, 0], [0, 4, 0], [0, 0, 7]]
for i in range(3):
    for j in range(3):
        if i == j:
            m += test[i][j]
print(m)        



#标准答案
#程序分析：利用双重for循环控制输入二维数组，再将a[i][i]累加后输出。
if __name__ == '__main__':
    a = []
    sum = 0.0
    for i in range(3):
        a.append([])
        for j in range(3):
            a[i].append(float(input("input num:\n")))
    for i in range(3):
        sum += a[i][i]
    print (sum)