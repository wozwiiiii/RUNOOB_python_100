"""
题目：
连接字符串。
"""
#自己的解法，直接简单进行相加
str_1 = input("please input string_one:")
str_2 = input("please input string_two:")

str_3 = str_1 + str_2

print(str_3)


#标准答案
"""
join()方法是字符串对象的一个方法，
用于将一个可迭代（如列表、元组等）对象中的所有元素连接成一个字符串，
并在每个元素之间插入指定的分隔符。
"""
 
delimiter = ','
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))