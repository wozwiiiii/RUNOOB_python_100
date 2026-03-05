"""
题目：
数字比较。
"""
def bijiao():
    a = int(input("input first number:"))
    b = int(input("input second number:"))
    if a == b:
        print("输入两个数字大小一样")
    elif a > b:
        print(f"较大的数字为{a},较小的数字为{b}")
    else:
        print(f"较大数字为{b},较小数字为{a}")

bijiao()    


#标准答案
 
if __name__ == '__main__':
    i = 10
    j = 20
    if i > j:
        print ('%d 大于 %d' % (i,j))
    elif i == j:
        print ('%d 等于 %d' % (i,j))
    elif i < j:
        print ('%d 小于 %d' % (i,j))
    else:
        print ('未知')