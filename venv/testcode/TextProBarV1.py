#TextProBarV1.py
#
import time as t
scale = 10  #步长
print("----------执行开始----------")
for i in range(scale + 1):
    a = '*' * i             #i个*
    b = '.' * (scale - i)   #scale-1 个 .
    c = (i/scale)*100
    print("{:^3.0f}%[{}->{}]".format(c,a,b))
    t.sleep(0.6)
print("----------执行结束----------")


#TextProbarV2.py
import time as t
for i in range(101):
    print("\r{:3}%".format(i),end = "")#光标回退到行首，不换行
    t.sleep(0.6)


