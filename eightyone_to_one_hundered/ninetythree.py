"""
题目：
时间函数举例3。
"""
#标准答案



if __name__ == '__main__':
    import time
    #start = time.clock(),time.clock()方法在python3.3后被弃用，使用time.perf_counter()计时
    start = time.perf_counter()

    for i in range(10000):
        print(i)
    #end = time.clock()
    end = time.perf_counter()

    print('different is %6.3f' % (end - start))
