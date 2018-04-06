#weekNamePrint.py
weekStr = "一二三四五六七"
weekID = eval(input("请输入数字1-7：_"))
print("今天是星期"+weekStr[weekID -1])


##打印12星座符号
for i in range(12):
    print(chr(9800+i),end = '')

##字符串类型操作
#8个常用方法
str.lower() #小写

str.upper()#大写

str.split(sep=None)#str根据sep被分隔
str.split(sep=None, maxsplit=-1)

'center'.capitalize()#字符串首字符大写
'Center'

str.center(width[, fillchar]) #字符串在width宽度居中时，以fillchar字符填充
'center'.center(20,'#')
'#######center#######'

str.count(sub[, start[, end]]) #返回字符串str中以start开始，以end结束的子字符串不重复的次数
c
'center'
c.count('e')
2

str.replace(old, new[, count]) #将字符串str中old字符串，用new字符串替换
c
'center'
c.replace('t','t.123')
'cent.123er'

str.strip([chars])
>>> '   spacious   '.strip()#未指定要去除的字符，默认去除行首尾的空白字符
'spacious'
>>> 'www.example.com'.strip('cmowz.')
'example'

c
' aa123bb '
c.strip()#未指定要去除的字符，默认去除行首尾的空白字符
'aa123bb'
c
' aa123bb '
c.strip('ab')#指定字符在行首、尾没有，则不去除
' aa123bb '
c
' aa123bb '
c.strip('1 ')
'aa123bb'
c
' aa123bb '
c.strip('b ')
'aa123'


str.join(iterable) #iterable可迭代对象：列表，字符串等
#在iterable中，除最后一个元素外每个元素后增加一个 str

d = '*'
a = 'www.baidu.com'
d.join(a)
'w*w*w*.*b*a*i*d*u*.*c*o*m' #主要用于字符分隔

#字符串类型的格式化
str.format()
str.format(*args, **kwargs)

>>> "The sum of 1 + 2 is {0}".format(1+2)
'The sum of 1 + 2 is 3'

"{}:计算机{}的CPU占用率为{}%".format("2018-04-01","C",10)
'2018-04-01:计算机C的CPU占用率为10%'

#槽的引导字符：
#填充对齐宽度
#槽的说明：
{n(槽的位置序号与format方法参数表序号对应):<填充><对齐><宽度><,(数字的千分位分隔符)><.浮点数小数精度或字符串最大输出长度><类型><>}


