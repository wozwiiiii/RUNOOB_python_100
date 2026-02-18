"""
题目：
输入三个整数x,y,z，请把这三个数由小到大输出。
"""

"""解析：我们想办法把最小的数放到x上，
先将x与y进行比较，如果x>y则将x与y的值进行交换，
然后再用x与z进行比较，如果x>z则将x与z的值进行交换，
这样能使x最小。
"""
#通过循环达到连续输入的效果，再利用列表中sort()方法进行升序排列
l = []
for i in range(3):
    x = int(input('integer:\n'))
    l.append(x)
l.sort()
print(l)    

h = []
for i in range(3):
    x = int(input('integer:\n'))
    h.append(x)
h.sort(reverse=True) #降序排列
print(h)    
