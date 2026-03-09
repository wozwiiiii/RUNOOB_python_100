"""
题目：
两个字符串连接程序。
"""
#自己的想法：简单构建一个相加函数，直接进行调用
def add(str_1, str_2):
    str_3 = str_1 + str_2

    print(str_3)

    return str_3

add("I ","Love You")


#标准答案
 
if __name__ == '__main__':
    a = "acegikm"
    b = "bdfhjlnpq"
 
    # 连接字符串
    c = a + b
    print(c)