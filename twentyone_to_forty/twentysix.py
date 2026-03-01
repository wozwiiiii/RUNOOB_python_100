"""
题目：
利用递归方法求5!。
"""

"""
错误递归，形成无限递归
def base(scor):
    if scor == 1:
        return scor
    else:
        scor *= base(scor) 
        scor -= 1
        
print(base(5))  
"""
  
#修改之后
def base(scor):
    if scor == 0 or scor == 1:
        return 1
    else:
        return scor *base(scor-1)
    
print(base(5))


#标准答案
#程序分析：递归公式：fn=fn_1*4!
 
def fact(j):
    sum = 0
    if j == 0:
        sum = 1
    else:
        sum = j * fact(j - 1)
    return sum
 
print (fact(5))