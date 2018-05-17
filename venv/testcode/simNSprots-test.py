'''
自顶向下
    解决复杂问题的有效方法
        -将一个问题表达为若干个小问题组成的形式
        -使用同样方法进一步分解小问题
        -直至，小问题可以用计算机简单明了的解决

自底向上（执行）
    逐步组建复杂系统的有效测试方法
        -分单元测试，逐步组装
        -按照自顶向下相反的路径操作
        -直至，系统各部分以组装的思路都经过测试和验证

比赛规则：
    -双人击球比赛：A&B，回合制，5局3胜
    -开始时一方先发球，直至判分，接下来胜者发球
    -球员只能在发球局得分，15分胜一局


程序总体框架及步骤
    -1：打印程序的介绍性信息               -printInfo()
    -2：获得程序远行参数：proA,ProB,n      -getInputs()
    -3：利用球员A和B的能力值，模拟n局比赛    -simNGames()
    -4：输出球员A和B获胜比赛的场次及概率     -printSummary()


'''
import random

def main():
    printInfo()
    probA,probB,n = getInputs()
    winsA,winsB = simNGames(n, probA, probB)
    printSummary(winsA,winsB)

def printInfo():
    print("这个程序模拟两个选择A和B的某种竞技比赛")
    print("程序运行需要A和B的能力值（以0到1之间的小数表示）")

def getInputs():
    a = eval(input("请输入选手A的能力值（0-1）："))
    b = eval(input("请输入选手B的能力值（0-1）："))
    n = eval(input("模拟比赛的场次："))
    return a,b,n

def printSummary(winsA,winsB):
    n = winsA + winsB
    print("竞技分析开始，共模拟{}场比赛".format(n))
    print("选手A获胜{}场比赛，占比{:0.1%}".format(winsA,winsA/n))
    print("选手B获胜{}场比赛，占比{:0.1%}".format(winsB, winsB/n))

def simNGames(n,probA,probB):
    winsA,winsB = 0,0
    for i in range(n):
        scoreA,scoreB = simOneGame(probA,probB)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA,winsB

def simOneGame(probA,probB):
    scoreA,scoreB = 0,0
    serving = "A"#发球人为A
    while not gameOver(scoreA,scoreB):
        if serving == "A":
            if random.random() < probA:#A发球时，如果随机数小于A的能力值，A得分
                scoreA += 1
            else:
                serving = "B"#A发球时，如果随机数不小于A的能力值，A不得分，换B为发球人
        else:
            if random.random() < probB:
                scoreB += 1
            else:
                serving = "A"
    return scoreA,scoreB

def gameOver(a,b):
    return a == 15 or b == 15

main()