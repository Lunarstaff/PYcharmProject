#TextProBarV3.py
#
import time as t
scale = 50  #步长
print("执行开始".center(scale//2,"-"))
start = t.perf_counter()
for i in range(scale + 1):
    a = '*' * i             #i个*
    b = '.' * (scale - i)   #scale-1 个 .
    c = (i/scale)*100
    dur = t.perf_counter() - start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end = "")
    t.sleep(0.3)
print("\n")
print("执行结束".center(scale//2,"-"))