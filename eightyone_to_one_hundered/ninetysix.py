"""
题目：
计算字符串中子串出现的次数。
"""

#自己的解法
str3 = input("please input str3:")
str4 = input("please input str4:")
num = str3.count(str4)
print(num)


#标准答案

if __name__ == '__main__':
    str1 = input('请输入一个字符串:\n')
    str2 = input('请输入一个子字符串:\n')
    ncount = str1.count(str2)
    print(ncount)


#其他解法

#循环遍历匹配
def count_substring(main_str, sub_str):
    count = 0
    sub_len = len(sub_str)
    for i in range(len(main_str) - sub_len + 1):
        if main_str[i:i + sub_len] == sub_str:
            count += 1
    return count

str1 = input('请输入一个字符串:\n')
str2 = input('请输入一个子字符串:\n')

ncount = count_substring(str1, str2)

print(ncount)
  