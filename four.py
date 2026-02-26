"""
题目：
输入某年某月某日，判断这一天是这一年的第几天？
"""

"""
自己的想法（较为复杂）：
通过三个函数进行取余计算来判别具体的年、月、日,再通过乘以对应月份的天数相加
def year_1():
    y = int(input("请输入现在是几年："))
    if (y % 4 == 0) and (y % 100 != 0) and (y % 400 == 0):
        print("今年是闰年")
    else:
        print("今年不是闰年")

def month_1():
    m = int(input("请输入现在的月份："))
"""

    


#标准解析（答案）：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天

 
year = int(input('year:\n'))
month = int(input('month:\n'))
day = int(input('day:\n'))
 
months = (0,31,59,90,120,151,181,212,243,273,304,334)
if 0 < month <= 12:
    sum = months[month - 1]
else:
    print ('data error')
sum += day
leap = 0
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    leap = 1
if (leap == 1) and (month > 2):
    sum += 1
print ('it is the %dth day.' % sum)