"""
题目：
时间函数举例2。
"""

#标准答案,记录起始时间来计算程序运行时长
 
if __name__ == '__main__':
    import time
    start = time.time()
    for i in range(3000):
        print(i)
    end = time.time()
 
    print(end - start)