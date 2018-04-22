#random 库-使用随机数据的Python标准库
"""
伪随机数：采用梅森旋转算法生成的食伪随机数

基本随机数函数：
seed(),random()
扩展随机数函数：
randint(),getrandbits(),uniform(),randrange(),choice(),shuffle()

随机数种子

初始化给定的随机数种子，默认为当前系统时间
import random
random.seed(10) #产生种子10对应的序列

random.random() #生成一个[0.0，1.0)之间的随机小数，与种子有关
0.5714025946899135

random.seed(10)
random.random()
0.5714025946899135
random.seed(10)
random.random()
0.5714025946899135

randint(a,b) #生成一个[a,b]之间的随机整数
randrange(m,n[,k]) #k 步长
getrandbits(k) #生成一个k比特长的随机整数
uniform(a,b) #生成一个[a,b]之间的随机小数
    random.uniform(10,100)
    53.43055070957703

choice(seq)#从序列seq中随机选择一个元素（抽奖）
shuffle(seq) #将序列seq中元素随机排列，返回打乱后的序列（洗牌）

1、能够利用随机数种子产生“确定”伪随机数
2、能够产生随机整数
3、能够对序列类型进行随机操作

"""
