#daydayup.py
# 天天向上的力量
#1.001^365
dayup = pow(1.001,365)
#0.999^365
daydown = pow(0.999,365)
print("天天向上：{:.2f}，天天向下：{:.2f}".format(dayup,daydown))


#daydayup3.py
dayup = 1.0#标准值
dayfactor = 0.01#每日增加或减少值
for i in range(365):
    if i%7 in[6,0]:#对7取模
        dayup = dayup * (1 - dayfactor)
        print("减少了：{:.2f}".format(dayfactor))
    else:
        dayup = dayup * (1 + dayfactor)
        print("增加了：{:.2f}".format(dayfactor))
print("工作日的力量：{:.2f}".format(dayup))

#工作日的力量：4.63


#daydayup4.py
def dayUP(df):#根据df参数计算工作日模式的力量值
    dayup = 1#力量初始值为1
    for i in range(365):
        if i%7 in[6,0]:
            dayup = dayup * (1 - 0.01)#周末减少0.01
        else:
            dayup = dayup * (1 + df)#工作日增加df
    return dayup

dayfactor = 0.01 #dayfactor = 0.01 开始试错
while dayUP(dayfactor) < 37.8:
    dayfactor += 0.001
print("工作日模式的努力参数是：{:.3f}".format(dayfactor))

#工作日模式的努力参数是：0.019

