#身份质量招数BMI
"""
BMI: Body Mass Index（kg/m^2）
偏瘦：<18.5
正常：18.5-25（国际），18.5-24（国内）
偏胖：25-30（国际），24-28（国内）
肥胖：>=30（国际），>=28（国内）

需求：
-输入：给定体重和身高值
-输出：BMI指标分类信息（国际和国内）

"""

#CalBMIv1.py
#输入两个值，用元组赋值

def getHeightandWeight():
    return eval(input("请输入身高（米）和体重（公斤）用逗号隔开："))#返回一个元组

def calBMI(b):
    bmi = b[1] / pow(b[0],2)
    return bmi

def calBMI_Index_Internation(b):
    if b < 18.5:
        who1 = "偏瘦"
    elif 18.5 <= b < 25:
        who1 = "正常"
    elif 25 <= b < 30:
        who1 = "偏胖"
    else:
        who1 = "肥胖"
    return who1

def calBMI_Index_CHN(b):
    if bmi < 18.5:
        who2 = "偏瘦"
    elif 18.5 <= bmi < 24:
        who2 = "正常"
    elif 24 <= bmi < 28:
        who2 = "偏胖"
    else:
        who2 = "肥胖"
    return who2

BMI_Index_CHN = ''
BMI_Index_Internation = ''
bmi = calBMI(getHeightandWeight())
BMI_Index_CHN = calBMI_Index_CHN(bmi)
BMI_Index_Internation = calBMI_Index_Internation(bmi)
print("BMI数值为：{:.2f}".format(bmi))
print("BMI指标为：国内{}".format(BMI_Index_CHN))
print("BMI指标为：国际{}".format(BMI_Index_Internation))


