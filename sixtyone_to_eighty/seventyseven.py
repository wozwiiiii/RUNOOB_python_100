"""
题目：
循环输出列表
"""
num = []
a = int(input("输入列表元素最大个数："))

for i in range(a):
    m = int(input(f"请输入第{i}元素："))
    num.append(m)

for j in range(len(num)):
    print(f"第{j}个元素是{num[j]}")    
    

#标准答案

 
if __name__ == '__main__':
    s = ["man","woman","girl","boy","sister"]
    for i in range(len(s)):
        print(s[i])
