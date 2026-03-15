"""
题目：
有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中。
"""

#标准答案
#注意：运行以上程序前，你需要在脚本执行的目录下创建 test1.txt、test2.txt 文件。
#以上程序执行成功后，打开 test3.txt 文件可以看到内容：123456

 
if __name__ == '__main__':
    import string
    fp = open('test1.txt')
    a = fp.read()
    fp.close()
 
    fp = open('test2.txt')
    b = fp.read()
    fp.close()
 
    fp = open('test3.txt','w')
    l = list(a + b)
    l.sort()
    s = ''
    s = s.join(l)
    fp.write(s)
    fp.close()
