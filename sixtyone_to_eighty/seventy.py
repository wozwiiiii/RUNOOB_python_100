"""
题目：
写一个函数，求一个字符串的长度，在main函数中输入字符串，并输出其长度。
"""
#自己的解法
def length(str):
    #str = input("please input string:")
    a = len(str)
    print(f"输入字符串长度为{a}")

    return a

if __name__ == '__main__':
    length('THe')


#标准答案(修改后满足python3.12.7版本)

if __name__ == '__main__':
    s = input('please input a string:\n')
    print("the string has %d characters." % len(s))
    