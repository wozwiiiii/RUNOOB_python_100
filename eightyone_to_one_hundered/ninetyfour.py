"""
题目：
时间函数举例4,一个猜数游戏，判断一个人反应快慢。
"""

#标准答案，raw_input()在python3.12.7版本中修改为input(),并且print()中需要添加引号
"""
程序实现了一个简单的猜数字游戏，
通过导入random模块并调用其中方法实现随机数生成，
导入时间模块并使用其中对应方法来计算猜数字程序运行的时间，并进行判断是否clever
"""
 
if __name__ == '__main__':
    import time
    import random
    
    play_it = input('do you want to play it.(\'y\' or \'n\')')
    while play_it == 'y':
        c = input('input a character:\n')
        i = random.randint(0,2**32) % 100
        print('please input number you guess:\n')

        #time.clock()方法在python3.12.7版本中出现错误，修改为per_counter()方法
        start = time.perf_counter()
        a = time.time()
        guess = int(input('input your guess:\n'))
        while guess != i:
            if guess > i:
                print('please input a little smaller')
                guess = int(input('input your guess:\n'))
            else:
                print('please input a little bigger')
                guess = int(input('input your guess:\n'))
        end = time.perf_counter()
        b = time.time()
        var = (end - start) / 18.2
        print(var)
        # print 'It took you %6.3 seconds' % time.difftime(b,a))
        if var < 15:
            print('you are very clever!')
        elif var < 25:
            print('you are normal!')
        else:
            print('you are stupid!')
        print('Congradulations')
        print('The number you guess is %d' % i)
        play_it = input('do you want to play it.')

