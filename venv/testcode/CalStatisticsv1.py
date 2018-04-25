#CalStatisticsv1.py
"""
基本统计与计算

-总个数：len()
-求和：for...in
-平均值：求和/求个数
-方差：
-中位数：排序，然后...找到中间的1个数（奇数）或者两个数的平均值（偶数）
"""

def getNum():   #获取用户不定长度的输入
    nums = []
    iNumStr = input("请输入数字（回车退出）：")
    while iNumStr != "":
        nums.append(eval(iNumStr))
        iNumStr = input("请输入数字（回车退出）：")
    return nums

def mean(numbers): #计算平均值
    s = 0.0
    for num in numbers:
        s = s + num
    return s / len(numbers)

def dev(numbers,mean):  #计算方差
    sdev = 0.0
    for num in numbers:
        sdev = sdev + (num - mean) ** 2
    return pow(sdev / (len(numbers) - 1),0.5)

def median(numbers): #计算中位数
    sorted(numbers)     #排序
    size = len(numbers) #得到长度（数据个数）
    if size%2 == 0:     #如果是偶数
        med = (numbers[size//2-1] + numbers[size//2])/2 #就取中间两个数的平均值
    else:               #如果是奇数
        med = numbers[size//2]  #就取中间位置的值
    return med

n = getNum()
m = mean(n)
print("平均值：{:.4f}\n方差：{:.4f}\n中位数：{}".format(m,dev(n,m),median(n)))
