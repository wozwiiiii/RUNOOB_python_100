"""
题目：
学习使用auto定义变量的用法。
"""

"""
在 Python 中，并没有 `auto` 这个关键字用于自动定义变量类型,因为 Python 是一种动态类型语言。
这意味着你不需要显式地声明变量的类型；Python 会根据你赋给变量的值自动推断其类型。
不过，在某些情况下，特别是在使用类型注解（Type Hints）时，Python 3.10 引入了一个新的关键字 `typing.Any`，以及 `type` 函数中的 `type()`，可以间接地实现类似“自动定义变量”的效果。

1、类型注解
类型注解是一种为变量、函数参数和返回值添加类型的提示方式。
虽然这不会改变变量的动态特性，但它可以提高代码的可读性和可维护性，并且可以被一些静态类型检查工具（如 `mypy`）使用。

from typing import Any

def example_function(x: Any) -> Any:
    return x + 1

a: int = 10
b: str = "Hello"
在这个例子中，`a` 和 `b` 被注解为 `int` 和 `str` 类型，但是这并不强制执行类型检查，Python 仍然可以动态地改变这些变量的类型。


2、`type()` 函数:可以用来查看变量的类型，但不能用于自动定义变量类型。它返回变量的类型对象。

a = 10
print(type(a))  # 输出: <class 'int'>

b = "Hello"
print(type(b))  # 输出: <class 'str'>
```


3、`typing` 模块提供了许多高级类型注解工具，比如 `List`, `Dict`, `Tuple` 等。

from typing import List

def sum_of_list(numbers: List[int]) -> int:
    return sum(numbers)

numbers = [1, 2, 3, 4, 5]
print(sum_of_list(numbers))  # 输出: 15
```
在这个例子中，`numbers` 被注解为包含 `int` 类型元素的列表。


4、`type()` 函数与动态类型
你可以使用 `type()` 函数来动态地确定变量的类型，并据此执行不同的操作，但这并不是“自动定义变量”的常用方式。

def process_variable(var):
    if isinstance(var, int):
        return var + 1
    elif isinstance(var, str):
        return var.upper()
    else:
        return var

a = 10
b = "hello"

print(process_variable(a))  # 输出: 11
print(process_variable(b))  # 输出: HELLO

在这个例子中，`process_variable` 函数根据传入变量的类型执行不同的操作。

总结
Python 不支持像 C++ 或 Rust 中的 `auto` 关键字来自动推断和定义变量类型，
因为 Python 本身就是动态类型的。你可以在代码中使用类型注解来提高代码的可读性和可维护性，但这不会改变 Python 的动态特性。
"""


#程序分析：没有auto关键字，使用变量作用域来举例。

num = 2
def autofunc():
    num = 1
    print ('internal block num = %d' % num)
    num += 1
for i in range(3):
    print ('The num = %d' % num)
    num += 1
    autofunc()