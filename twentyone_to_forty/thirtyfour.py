"""
题目：练习函数调用。
"""
#自己的解法
#一个简单的加法函数
def add(x,y):
    z = x + y
    return z
    

def price(x,y):
    price = add(x,y)
    print(price)

if __name__ == '__main__':
    price(3,4)


#标准答案，解析：使用函数，输出三次 RUNOOB 字符串。
def hello_runoob():
    print ('RUNOOB')
 
def hello_runoobs():
    for i in range(3):
        hello_runoob()
if __name__ == '__main__':
    hello_runoobs()