#圆周率问题
"""
1、圆周率的近似计算公式：微积分
2、蒙特卡罗方法：
"""

#CalPiv1.py
pi = 0
N = 100
for k in range(N):
    pi += 1/pow(16,k)*( \
        4/(8*k+1) - 2/(8*k+4) - \
        1/(8*k+5) - 1/(8*k+6)
    )
print("圆周率值是：{}".format(pi))


#CalPiv2.py
#蒙特卡罗算法-撒点法
from random import random
from time import perf_counter
DARTS = 1000*1000 #确定撒点的数量（在单位面积内）
hits = 0.0 #命中圆内的点的数量
start = perf_counter()
for i in range(1,DARTS+1):
    x,y = random(),random()
    dist = pow(x**2 + y**2,0.5) #点的位置距圆心的距离
    if dist <= 1.0:             #如果在圆内，则为命中
        hits = hits +1
pi = 4 * (hits/DARTS)
print("圆周率值是：{}".format(pi))
print("运行时间是：{:.5f}s".format(perf_counter() - start))
