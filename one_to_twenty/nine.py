"""
题目：
暂停一秒输出。
"""
#调用sleep()函数
import time
print("下面将会1秒出现一个式子")

for i in range(1,10):
    #内层循环控制每一行内容
    for j in range(1,i+1):
        print(f"{j}*{i}={j*i}\t",end='')

    #外层循环通过print()输出一个回车符    
    print()   
    time.sleep(1)       
