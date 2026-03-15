'''
1. 打开文件
使用 `open` 函数打开文件。`open` 函数的基本语法如下：

file = open(file_path, mode)
```
- `file_path`：文件的路径，可以是相对路径或绝对路径。
- `mode`：文件的打开模式，常见的模式包括：
  - `'r'`：只读模式（默认模式）。
  - `'w'`：写入模式，如果文件存在则清空内容，如果文件不存在则创建新文件。
  - `'a'`：追加模式，在文件末尾追加内容，如果文件不存在则创建新文件。
  - `'b'`：二进制模式，通常与其他模式结合使用，例如 `'rb'` 或 `'wb'`。
  - `'+'`：读写模式，通常与其他模式结合使用，例如 `'r+'` 或 `'w+'`。

2. 读取文件内容
 读取全部内容

content = file.read()
```
 按行读取

# 读取一行
line = file.readline()

# 读取所有行到一个列表中
lines = file.readlines()
```

3. 写入文件内容
 写入全部内容

file.write(content)
```
 写入多行内容

file.writelines(lines)
```

4. 关闭文件
完成文件操作后，务必关闭文件以释放资源。

file.close()
```

5. 使用 `with` 语句
`with` 语句可以自动管理文件的打开和关闭，推荐使用。

with open(file_path, mode) as file:
    # 读取或写入文件的操作
    content = file.read()
```

6. 常见文件操作模式总结
- `'r'`：只读模式，文件必须存在。
- `'w'`：写入模式，如果文件存在则清空内容，如果文件不存在则创建新文件。
- `'a'`：追加模式，如果文件存在则在末尾追加内容，如果文件不存在则创建新文件。
- `'r+'`：读写模式，文件必须存在。
- `'w+'`：读写模式，如果文件存在则清空内容，如果文件不存在则创建新文件。
- `'a+'`：读写模式，如果文件存在则在末尾追加内容，如果文件不存在则创建新文件。
- `'rb'`：以二进制形式读取文件。
- `'wb'`：以二进制形式写入文件。
- `'ab'`：以二进制形式在文件末尾追加内容。
- `'r+b'` 或 `'rb+'`：以二进制形式读写文件。
- `'w+b'` 或 `'wb+'`：以二进制形式读写文件，如果文件存在则清空内容。
- `'a+b'` 或 `'ab+'`：以二进制形式读写文件，如果文件存在则在末尾追加内容。

7. 示例代码
读取文件示例

with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
```

写入文件示例

with open('example.txt', 'w') as file:
    file.write('Hello, World!\n')
    file.write('This is a new line.')
```

追加文件示例

with open('example.txt', 'a') as file:
    file.write('\nAppending this line.')
```

逐行读取示例

with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())  # strip() 用于去除行末的换行符
```

8. 文件指针定位
可以使用 `seek` 方法来定位文件指针的位置。
```python
file.seek(offset, whence)
```
- `offset`：偏移量，表示移动的字节数。
- `whence`：参考位置，可以是：
  - `0`：文件开头（默认）。
  - `1`：当前文件指针位置。
  - `2`：文件末尾。

示例

with open('example.txt', 'r') as file:
    file.seek(6)  # 移动到第7个字节
    content = file.read()
    print(content)
```

9. 文件操作中的异常处理
使用 `try` 和 `except` 来处理文件操作中的异常。

try:
    with open('example.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print('文件未找到')
except IOError:
    print('文件操作错误')
```

10. 处理二进制文件
对于二进制文件，使用 `'b'` 模式。

with open('example.bin', 'rb') as file:
    content = file.read()
    print(content)

with open('example.bin', 'wb') as file:
    file.write(b'Hello, Binary World!')

'''
