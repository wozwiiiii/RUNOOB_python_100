"""
题目：
两个乒乓球队进行比赛，各出三人。
甲队为a,b,c三人，乙队为x,y,z三人。
已抽签决定比赛名单。有人向队员打听比赛的名单。
a说他不和x比，c说他不和x,z比，
请编程序找出三队赛手的名单。
"""
#自己的解法，通过某种方法获得两队的对应队员的字符串，再依据两段逻辑性描述使用if语句判断
def find_pairs():
    for a in "xyz":
        for b in "xyz":
            for c in "xyz":
                if a != b and b != c and a != c:  # 确保a, b, c各不相同
                    if a != "x" and c != "x" and c != "z":  # 根据题目条件排除不符合的情况
                        print(f"a与{a}, b与{b}, c与{c}")

find_pairs()



#标准答案
for i in range(ord('x'),ord('z') + 1):
    for j in range(ord('x'),ord('z') + 1):
        if i != j:
            for k in range(ord('x'),ord('z') + 1):
                if (i != k) and (j != k):
                    if (i != ord('x')) and (k != ord('x')) and (k != ord('z')):
                        print ('order is a -- %s\t b -- %s\tc--%s' % (chr(i),chr(j),chr(k)))