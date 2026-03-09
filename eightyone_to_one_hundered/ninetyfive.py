"""
题目：
字符串日期转换为易读的日期格式。
"""
#标准答案
"""
dateutil 库中与时间解析相关的主要模块和用法包括： 

parser 模块：这个模块提供了 parse 函数，可以解析几乎任何格式的日期时间字符串。

  parse(date_string, **kwargs)：date_string 是要解析的日期时间字符串，
  kwargs 是可选的关键字参数，用于控制解析的行为。
  例如：
     fuzzy：允许解析不完整的日期时间字符串。
  
     dayfirst 或 yearfirst：指定日期格式中的日和年是否在月之前。
  
     ignoretz：忽略时区信息。
  
     default：设置默认的 datetime 对象作为解析的基础。

  
relativedelta 模块：用于计算两个日期之间的差异，或者在日期上进行相对的加减操作。

  relativedelta(dt1, dt2)：计算两个 datetime 对象之间的差异。

  relativedelta(years=1, months=1)：用于创建一个相对的时间差对象，可以用于在日期上进行加减操作。


tz 模块：提供了时区信息的支持，可以用于处理不同时区的日期时间。 
  tz.gettz(tzname)：通过时区名称获取 tzinfo 对象，例如 tz.gettz('Asia/Shanghai') 可以获取上海的时区信息。
"""

from dateutil import parser
dt = parser.parse("Aug 28 2015 12:00AM")
print(dt)
