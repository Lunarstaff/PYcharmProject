#真实和美.py
"""
文本词频统计：
需求：一篇文章，出现了哪些词？哪些词出现得最多？

英文的：
C:\E-Data-File\腾讯课堂\Python入门\PYcharmProject\venv\testcode\词频统计\London.txt

中文的:
C:\E-Data-File\腾讯课堂\Python入门\PYcharmProject\venv\testcode\词频统计\真实和美.txt

"""

import jieba

exclues = {"一首","可以","没有","许多","由于"}#多次尝试建立排除词的集合

file_zhenshi = "./词频统计/真实和美.txt"
txt = open(file_zhenshi,"r",encoding="utf-8").read()
words = jieba.lcut(txt)#分词
counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word,0) + 1
#在这里删除排除词库里的词
for word in exclues:
    del counts[word]

items = list(counts.items())
items.sort(key=lambda x:x[1] , reverse=True)
#输出
for i in range(15):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word,count))

