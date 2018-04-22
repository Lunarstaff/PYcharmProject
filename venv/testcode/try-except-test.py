#程序的异常处理
#num = eval(input("请输入一个整数："))
#print("输入的值为：{}".format(num))

"""
报错信息如下：
请输入一个整数：>? abd
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "<string>", line 1, in <module>
NameError: name 'abd' is not defined
"""

#异常处理
"""
try :
    <语句块1>
except :
    <语句块2>

#增加异常类型标记
try :
    <语句块1>
except <异常类型>: #只有在这种异常类型出现的情况下执行语句块2
    <语句块2>
    <语句块2>
1、异常类型名称是在Python中预定义的
SyntaxError
NameError
"""

try :
    num = eval(input("请输入一个整数："))
    print(num ** 2)
except:
    print("输入的不是整数")

#异常处理的高级使用
"""
try:
    <语句块1>
except:
    <语句块2> #except 对应的语句块在发生异常时执行
else:
    <语句块3> #else 对应的语句块3 在不发生异常时执行
finally:
    <语句块4> #finally对应的语句块4 一定执行

"""