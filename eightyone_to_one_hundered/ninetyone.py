"""
题目：
时间函数举例1。
"""
#标准答案,代码解析见注释


if __name__ == '__main__':
    import time
    print(time.ctime(time.time()))
    """
    time.time()：这个函数返回自1970年1月1日午夜（UTC）以来的秒数，以浮点数形式表示（即Unix时间戳）。
    time.ctime(seconds)：这个函数将时间戳转换为本地时间的字符串表示。
    因此，time.ctime(time.time())会打印当前的本地时间，格式类似于“Wed Oct 7 23:34:23 2020”。
    """


    print(time.asctime(time.localtime(time.time())))
    """
    time.localtime(seconds)：这个函数将时间戳转换为本地时间的struct_time对象。
    time.asctime(time_tuple)：这个函数将struct_time对象转换为字符串表示。
    因此，time.asctime(time.localtime(time.time()))也会打印当前的本地时间，格式与time.ctime()相同。
    """



    print(time.asctime(time.gmtime(time.time())))
    """
    time.gmtime(seconds)：这个函数将时间戳转换为UTC时间的struct_time对象。
    time.asctime(time_tuple)：这个函数同样将struct_time对象转换为字符串表示。
    因此，time.asctime(time.gmtime(time.time()
    """
