"""
题目：
一球从100米高度自由落下，
每次落地后反跳回原高度的一半；
再落下，求它在第10次落地时，共经过多少米？
第10次反弹多高？
"""
#自己的解法：存在问题初始s多加了100米
def ball_jump(num): 
    #定义初始数据
    jump = 100.0
    height = 0
    s = 0

    #通过循环限制次数并计算反弹高度和总路程
    for i in range(1,num+1):
        #判断s是否需要×2
        if i == 1:
            s = jump
        else:
            s = jump * 2 #在开始回弹后，每次的距离都为jump的两倍
        """s = jump * 2 如果没有判断直接相加会导致初始s多加了100米"""
        
        #每次回弹高度减半，累计总路程
        jump  *= 0.5   
        height += s
        
    print(f"小球反弹高度：{jump},小球经过总距离：{height}")

print(ball_jump(10))





#标准答案
def calculate_distance_and_height(height, times):
    total_distance = 0
    current_height = height

    for i in range(1, times + 1):
        # 从第二次开始，落地时的距离应该是反弹高度乘以2（弹到最高点再落下）
        if i == 1:
            total_distance += current_height
        else:
            total_distance += current_height * 2  # 每次下落和反弹的距离
        current_height /= 2  # 反弹后的高度

    return total_distance, current_height

# 初始高度为100米，计算第10次落地时的总距离和反弹高度
height = 100
bounce_times = 10
total_distance, final_height = calculate_distance_and_height(height, bounce_times)

print(f"第{bounce_times}次落地时，共经过 {total_distance} 米。")
print(f"第{bounce_times}次反弹的高度为 {final_height} 米。")
