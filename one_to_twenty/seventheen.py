"""
题目：
输入一行字符，
分别统计出其中英文字母、空格、数字和其它字符的个数。
"""

#自己的解法（统计模块参考了答案）
import string

test_str =  input("请输入您想要测试的字符串： ") #输入字符串

#定义英文字母、空格、数字和其他字符初值
en_word = 0 
sp_word = 0
num = 0
ot_word = 0


"""
isalpha()：如果字符是英文字母，则en_word加1。
isspace()：如果字符是空格，则sp_word加1。
isdigit()：如果字符是数字，则num加1。
如果字符既不是字母、空格也不是数字，则ot_word加1。
"""
for i in test_str:
    if i.isalpha():
        en_word += 1
    elif i.isspace():
        sp_word += 1
    elif i.isdigit():
        num += 1
    else:
        ot_word += 1
print(f"英文字母个数为{en_word},空格个数为{sp_word},数字个数为{num},其他字符个数为{ot_word}")

#其他方法（参考AI)
from collections import Counter

test_str = input("请输入您想要测试的字符串： ")

# 初始化计数器
en_word = 0
sp_word = 0
num = 0
ot_word = 0

# 使用Counter统计每个字符出现的次数
counter = Counter(test_str)

for char, count in counter.items():
    if char.isalpha():
        en_word += count
    elif char.isspace():
        sp_word += count
    elif char.isdigit():
        num += count
    else:
        ot_word += count

print(f"英文字母个数为{en_word},空格个数为{sp_word},数字个数为{num},其他字符个数为{ot_word}")

"""
collections.Counter是一个字典子类，用于计数可哈希对象。
它会返回一个字典，其中键是字符，值是该字符在字符串中出现的次数。
通过遍历counter.items()，我们可以根据每个字符的类型更新相应的计数器。
"""



# 使用str.count统计每种字符的数量
test_str = input("请输入您想要测试的字符串： ")

en_word = sum(c.isalpha() for c in test_str)
sp_word = sum(c.isspace() for c in test_str)
num = sum(c.isdigit() for c in test_str)
ot_word = len(test_str) - (en_word + sp_word + num)

print(f"英文字母个数为{en_word},空格个数为{sp_word},数字个数为{num},其他字符个数为{ot_word}")

"""
str.count方法可以用来统计某个特定字符在字符串中出现的次数，但在这里我们使用生成器表达式来统计每种字符的数量。
sum(c.isalpha() for c in test_str)会计算字符串中所有英文字母的数量。
sum(c.isspace() for c in test_str)会计算字符串中所有空格的数量。
sum(c.isdigit() for c in test_str)会计算字符串中所有数字的数量。
ot_word的计算通过总字符数减去英文字母、空格和数字的数量来得到。
"""



# 使用正则表达式统计每种字符的数量
import re

test_str = input("请输入您想要测试的字符串： ")


en_word = len(re.findall(r'[a-zA-Z]', test_str))
sp_word = len(re.findall(r'\s', test_str))
num = len(re.findall(r'\d', test_str))
ot_word = len(test_str) - (en_word + sp_word + num)

print(f"英文字母个数为{en_word},空格个数为{sp_word},数字个数为{num},其他字符个数为{ot_word}")

"""
re.findall(pattern, string)返回一个列表，其中包含所有匹配正则表达式pattern的子串。
r'[a-zA-Z]'匹配所有英文字母。
r'\s'匹配所有空白字符，包括空格、制表符、换行符等。
r'\d'匹配所有数字字符。
通过计算每个正则表达式匹配到的子串数量，我们可以分别统计英文字母、空格和数字的数量。
ot_word的计算同样通过总字符数减去英文字母、空格和数字的数量来得到。
"""



# 使用filter和lambda统计每种字符的数量
test_str = input("请输入您想要测试的字符串： ")

en_word = len(list(filter(lambda c: c.isalpha(), test_str)))
sp_word = len(list(filter(lambda c: c.isspace(), test_str)))
num = len(list(filter(lambda c: c.isdigit(), test_str)))
ot_word = len(test_str) - (en_word + sp_word + num)

print(f"英文字母个数为{en_word},空格个数为{sp_word},数字个数为{num},其他字符个数为{ot_word}")

"""
filter(function, iterable)会根据function返回的布尔值过滤iterable中的元素。
lambda c: c.isalpha()是一个匿名函数，用于判断字符是否为英文字母。
lambda c: c.isspace()用于判断字符是否为空格。
lambda c: c.isdigit()用于判断字符是否为数字。
filter返回的是一个迭代器，我们用list()将其转换为列表，然后计算列表的长度以得到相应的字符数量。
ot_word同样通过总字符数减去英文字母、空格和数字的数量来得到。
"""

 
"""
标准答案
程序分析：利用 while 或 for 语句,条件为输入的字符不为 '\n'。 
import string
s = input('请输入一个字符串:\n')
letters = 0
space = 0
digit = 0
others = 0
for c in s:
    if c.isalpha():
        letters += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        others += 1
print ('char = %d,space = %d,digit = %d,others = %d' % (letters,space,digit,others))
"""
