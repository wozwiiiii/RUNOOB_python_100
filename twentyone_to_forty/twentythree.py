"""
题目：
打印出如下图案（菱形）:
   *
  ***
 *****
*******
 *****
  ***
   *
"""


#标准答案
#程序分析：先把图形分成两部分来看待，前四行一个规律，后三行一个规律，
#利用双重for循环，第一层控制行，第二层控制列。
def print_diamond(rows):
    # 上半部分
    for i in range(1, rows, 2):
        spaces = " " * ((rows - i) // 2)
        stars = "*" * i
        print(spaces + stars)

    # 下半部分
    for i in range(rows, 0, -2):
        spaces = " " * ((rows - i) // 2)
        stars = "*" * i
        print(spaces + stars)

# 设置行数，可以根据需要调整
rows = 7
print_diamond(rows)