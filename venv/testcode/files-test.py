#files-test.py
"""

文件和数据格式化
-文件的使用
-自动轨迹绘制
-一维数据的格式化和处理
-二维
-模块6：wordcloud库
-实例：政府工作报告词云

文本文件vs二进制文件
    -文本文件和二进制文件只是文件的展示方式
    -本质上，所有文件都是二进制形式存储
    -形式上，所有文件采用两种方式展示
-文本文件：
    由单一特定编码组成的文件，比如utf-8编码
    由于存在编码，也被看成是存储着的长字符串
    适用于列如：.txt文件、.py文件
-二进制文件
    直接由比特0和1组成，没有统一字符编码
    一般存在二进制0和1的组织结构，即文件格式
    适用于例如：.png文件、.avi文件等


文件的处理步骤：
    打开-操作-关闭
    文件的存储状态 -> a=open(,) -> 文件的占用状态
    读文件、写文件
    文件的占用状态 -> a.close() -> 文件的存储状态


文件的使用：
变量名 = open(<文件名>,<打开模式>)

文件名：
    Windows下的文件路径：“PYcharmProject\venv\testcode\testfiles\txt.txt”
    py文件中路径写为：“PYcharmProject/venv/testcode/testfiles/txt.txt”
        或“PYcharmProject\\venv\\testcode\\testfiles\\txt.txt”
    也可写为相对路径：当前执行路径为：C:\E-Data-File\腾讯课堂\Python入门\PYcharmProject
    所以，可写为“./venv/testcode/testfiles/txt.txt”
C:\E-Data-File\腾讯课堂\Python入门\PYcharmProject\venv\testcode\testfiles
C:/E-Data-File/腾讯课堂/Python入门/PYcharmProject/venv/testcode/testfiles


打开模式：(一定要用双引号)
    'r' 只读模式，默认值，如果文件不存在，返回FileNotFoundError
    'w' 覆盖写模式，如果文件不存在则创建，如果存在则完全覆盖
    'x' 创建写模式，如果文件不存在则创建，如果存在则返回FileExistsError
    'a' 追加写模式，如果文件不存在则创建，如果存在则在文件最后追加内容。
    'b' 二进制文件模式
    't' 文本文件模式，默认值
    '+' 与r/w/x/a 一同使用，在原功能基础上增加同时读写功能
        比如： ft = open("./even/testcode/testfiles/txt.txt","w+")
例：
ft = open("./venv/testcode/testfiles/txt.txt")          #文本形式、只读模式、默认值
ft = open("./venv/testcode/testfiles/txt.txt","rt")     #文本形式、只读模式、同默认值
ft = open("./venv/testcode/testfiles/txt.txt","w")      #文本形式、覆盖写模式
ft = open("./venv/testcode/testfiles/txt.txt","a+")     #文本形式、追加写模式+读文件
ft = open("./venv/testcode/testfiles/txt.txt","x")      #文本形式、创建写模式
ft = open("./venv/testcode/testfiles/txt.txt","b")      #二进制形式、只读模式
ft = open("./venv/testcode/testfiles/txt.txt","wx")     #二进制形式、覆盖写模式

文件关闭：
    <变量名>.close()

txt_file = "./venv/testcode/testfiles/txt.txt"
ft = open(txt_file,"rt")
fb = open(txt_file,"rb")
ft
<_io.TextIOWrapper name='./venv/testcode/testfiles/txt.txt' mode='rt' encoding='cp936'>
ft.readline()
'这里有一个文本文件。Lunar12'
fb.readline()
b'\xd5\xe2\xc0\xef\xd3\xd0\xd2\xbb\xb8\xf6\xce\xc4\xb1\xbe\xce\xc4\xbc\xfe\xa1\xa3Lunar12'

文件读取：
<f>.read(size = -1) 读入全部内容，如果给出参数，读入前size长度

>>> txt = "C:/E-Data-File/腾讯课堂/Python入门/PYcharmProject/venv/testcode/
testfiles/txt.txt"
>>> ft = open(txt,"rt")
>>> ft.read(2) #如果给出参数，读入前size长度
'这里'
>>> ft.read(2) #

<f>.readline(size = -1) 读入一行内容，如果给出参数，读入该行前size长度
>>> ft = open(txt,"r")
>>> ft.readline()
'1-这里是一个文本文件。\n'
>>> ft.readline(2)
'2-'

<f>.readlines(hint = 1) 读入文件所以行，以每行元素形成列表，如果给出参数，读入前hint行
>>> ft = open(txt,"r")
>>> s = ft.readlines()
>>> s
['1-这里是一个文本文件。\n', '2-第二行']

>>> ft = open(txt,"r")
>>> t = ft.readlines(1)
>>> t
['1-这里是一个文本文件。\n']


文件的全文本操作：
    遍历全文本：方法一
fname = input("请输入要打开的文件名称：")
fo = open(fname,"r")
txt = fo.read() #一次读入，统一处理（不适用于文本文件大时读入）
#对全文txt进行处理
fo.close()

    方法二：按数量读入，逐步处理
fname = input("请输入要打开的文件名称：")
fo = open(fname,"r")
txt = fo.read(2)
while txt != "":
    #对txt进行处理
    txt = fo.read(2)
fo.close()

按行存储的文件遍历方法一：
    fname = input("请输入要打开的文件名称：")
    fo = open(fname,"r")
    for line in fo.readlines():#一次读入，分行处理
        peint(line)
    fo.close()

    方法二：
    fname = input("请输入要打开的文件名称：")
    fo = open(fname,"r")
    for line in fo:#分行读入，逐行处理
        print(line)
    fo.close()



数据的文件写入
<f>.write(s) #向文件写入一个字符串或字节流
<f>.writelines(lines) #将一个元素全为字符串的列表写入文件
<f>.seek(offset) #改变当前文件操作指针的位置，offset含义如下：、
                    0-文件开头
                    1-当前位置
                    2-文件结尾



-有一个字符串数组，将其写入到文件a
-并将文件中的内容输出
其中：
    文件a
    路径：C:\E-Data-File\腾讯课堂\Python入门\PYcharmProject\venv\testcode\testfiles
        C:/E-Data-File/腾讯课堂/Python入门/PYcharmProject/venv/testcode/testfiles/files-test.txt
    需要写入文件a的内容为：
    new_text = ["i miss my blue blue sky\n",
                "but aftet i left my home\n",
                "blue blue sky is far away from me\n",
                "and there is no star\n",
                "i miss my blue blue sky\n",
                "i miss my little little home\n"]

"""

blueSky_f = "C:/E-Data-File/腾讯课堂/Python入门/PYcharmProject/venv/testcode/testfiles/files-test.txt"
new_text = ["i miss my blue blue sky\n",
            "but aftet i left my home\n",
            "blue blue sky is far away from me\n",
            "and there is no star\n",
            "i miss my blue blue sky\n",
            "i miss my little little home\n"]
blueSky_fo = open(blueSky_f,"w+")   #写+读模式打开文件
blueSky_fo.writelines(new_text)     #写入文本
blueSky_fo.seek(0)                  #操作指针归零
blueSky_text = blueSky_fo.readlines()#读取文本文本，返回按行的字符串列表
for line in blueSky_text:           #遍历
    print(line)
blueSky_fo.close()

