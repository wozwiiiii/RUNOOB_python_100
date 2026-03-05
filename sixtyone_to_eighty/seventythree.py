"""
题目：
反向输出一个链表。
"""
#标准答案

if __name__ == '__main__':
    ptr = []
    for i in range(3):
        num = int(input('please input a number:\n'))
        ptr.append(num)
    print(ptr)
    
    ptr.reverse()
    print(ptr)
