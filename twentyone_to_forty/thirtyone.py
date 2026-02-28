"""
题目：
请输入星期几的第一个字母来判断一下是星期几，
如果第一个字母一样，则继续判断第二个字母。
"""
#自己的解法，通过不同星期英文字符的判别进行具体判断
i = 0
while i <=7:
    week = input("请输入周几的第一个字母：")
    if week == 'M':
        print("Today is Monday")
    elif week == 'F':
        print("Today is Friday")
    elif week == 'W':
        print("Today is Wensday")
    elif week == 'T' or 'S':
        week = input(f"由于第1个字母相同，请输入第2个字母进行判断：")
        if week == 'h':
            print("Today is Thursday")
        elif week == 'a':
            print("Today is Saturday")
        elif week == 'u':
            week = input("由于第2个字母相同，请输入第3个字母进行判断：")
            if week == 'e':
                print("Today is Tuesday")
            elif week == 'n':
                print("Today is Sunday")




#标准答案
#程序解析：用情况语句比较好，如果第一个字母一样，则判断用情况语句或if语句判断第二个字母。
letter = input("please input:")
#while letter  != 'Y':
if letter == 'S':
    print ('please input second letter:')
    letter = input("please input:")
    if letter == 'a':
        print ('Saturday')
    elif letter  == 'u':
        print ('Sunday')
    else:
        print ('data error')
    
elif letter == 'F':
    print ('Friday')
    
elif letter == 'M':
    print ('Monday')
    
elif letter == 'T':
    print ('please input second letter')
    letter = input("please input:")
 
    if letter  == 'u':
        print ('Tuesday')
    elif letter  == 'h':
        print ('Thursday')
    else:
        print ('data error')
        
elif letter == 'W':
    print ('Wednesday')
else:
    print ('data error')