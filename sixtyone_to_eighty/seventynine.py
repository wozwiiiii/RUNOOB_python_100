"""
题目：
字符串排序。
"""

#自己的解法：使用sort()方法，将字符串转为列表形式,再使用sort()方法操作
str_1 = input("请输入第一个字符串：")
str_2 = input("请输入第二个字符串：")
str_3 = input("请输入第三个字符串：")

string = [str_1, str_2, str_3]

string.sort()
print(string)



#标准答案
 
if __name__ == '__main__':
    str1 = input('input string:\n')
    str2 = input('input string:\n')
    str3 = input('input string:\n')
    print(str1,str2,str3)
    
    if str1 > str2 : str1,str2 = str2,str1
    if str1 > str3 : str1,str3 = str3,str1
    if str2 > str3 : str2,str3 = str3,str2
 
    print('after being sorted.')
    print(str1,str2,str3)