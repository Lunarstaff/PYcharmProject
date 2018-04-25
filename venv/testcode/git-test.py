#真实和美.py
"""
文本词频统计：
需求：一篇文章，出现了哪些词？哪些词出现得最多？

英文的：
C:\E-Data-File\腾讯课堂\Python入门\PYcharmProject\venv\testcode\词频统计\London.txt

中文的:
C:\E-Data-File\腾讯课堂\Python入门\PYcharmProject\venv\testcode\词频统计\真实和美.txt

"""

def getText(file_en):
    txt = open(file_en,"r").read() #注意这里的目录表示与系统中不同
    txt = txt.lower() #将文本中的字符换成小写
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
        txt = txt.replace(ch," ") #将文本中的特殊符号换成空格
    return txt

London_file = "./词频统计/London.txt"
LondonTxt = getText(London_file)
words = LondonTxt.split() #返回文本的词序列
#词与出现的次数够成了字典
counts = {}
for word in words:
    counts[word] = counts.get(word,0) + 1

items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True) #需要查阅资料,按次数（字典的值）排序
for i in range(10):
    word,count = items[i]
    print("{0:<10}{1:>5}".format(word,count))

