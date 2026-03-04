"""
题目：
使用lambda来创建匿名函数。
"""


"""
Lambda匿名函数在Python中用于创建小型匿名函数。与def定义的函数相比，匿名函数没有名称。
Lambda函数可以接受任意数量的参数，但只能有一个表达式。它的语法形式为：`lambda 参数1, 参数2, ... : 表达式`。


Lambda函数的作用主要包括以下几点：
1. 简化代码：Lambda函数可以用来简化代码，尤其是对于那些只需要简单表达式的函数，使用lambda可以避免定义一个完整的函数。
2. 函数式编程：Lambda函数可以作为参数传递给高阶函数，如`map()`、`filter()`、`sorted()`等，这些函数接受其他函数作为参数。
3. 快速定义：Lambda函数适用于需要快速定义并使用函数的场景，不需要正式定义函数。

Lambda函数的常用用法包括：

- 使用map()函数：`map(function, iterable)`，可以使用lambda函数来对可迭代对象中的每个元素执行操作。
  
  numbers = [1, 2, 3, 4]
  squared_numbers = map(lambda x: x**2, numbers)
  print(list(squared_numbers))  # 输出: [1, 4, 9, 16]
  ```

- 使用filter()函数：`filter(function, iterable)`，可以使用lambda函数来过滤可迭代对象中的元素。
  
  numbers = [1, 2, 3, 4, 5]
  even_numbers = filter(lambda x: x % 2 == 0, numbers)
  print(list(even_numbers))  # 输出: [2, 4]
  ```

- 使用sorted()函数：`sorted(iterable, key=function)`，可以使用lambda函数来指定排序的依据。
 
  students = [('John', 8), ('Alice', 9), ('Bob', 7)]
  sorted_students = sorted(students, key=lambda student: student[1])
  print(sorted_students)  # 输出: [('Bob', 7), ('John', 8), ('Alice', 9)]
  ```

- 作为其他函数的内部函数：在需要一个简单函数作为参数时，可以直接在函数调用中定义lambda函数。

  def apply_func(func, value):
      return func(value)

  result = apply_func(lambda x: x * 3, 5)
  print(result)  # 输出: 15
  ```

需要注意的是，虽然lambda函数可以在一行中定义多个参数，但是它们只适合用于简单的操作，对于复杂的逻辑，最好还是使用def定义普通的函数。
"""

#标准答案

 

 
MAXIMUM = lambda x,y :  (x > y) * x + (x < y) * y
MINIMUM = lambda x,y :  (x > y) * y + (x < y) * x
 
if __name__ == '__main__':
    a = 10
    b = 20
    print ('The largar one is %d' % MAXIMUM(a,b))
    print ('The lower one is %d' % MINIMUM(a,b))