# def data(str_t):
#     num = 0
#     for i in str_t:
#         num = (eval(i) ** 2) + num
#     return str(num)
#
#
# def main():
#     num_in_str = input("")
#     while eval(num_in_str) != 1:
#         num_in_str = data(num_in_str)
#     if num_in_str == '1':
#         print("True")
#     else:
#         print("False")
# main()


# num_in = input("")
# try:
#     num = eval(num_in)
#     if num == 0:
#         print("输入有误，请输入正整数")
#     elif num_in.isdigit():
#         result_num = 0
#         for i in range(eval(num_in)):
#             i_n = 1
#             i = i + 1
#             for j in range(i):
#                 i_n = i_n * (j + 1)
#             result_num = result_num + i_n
#         print(result_num)
#     else:
#         print("输入有误，请输入正整数")
# except:
#     print("输入有误，请输入正整数")




#
# fenshu_in = input("")
# try:
#     fenshu = eval(fenshu_in)
#     if fenshu_in.isdigit():
#         if fenshu > 100:
#             print("输入数据有误！")
#         elif fenshu >= 91:
#             print("输入成绩属于A级别。")
#             print("祝贺你通过考试！")
#         elif fenshu >= 81:
#             print("输入成绩属于B级别。")
#             print("祝贺你通过考试！")
#         elif fenshu >= 71:
#             print("输入成绩属于C级别。")
#             print("祝贺你通过考试！")
#         elif fenshu >= 60:
#             print("输入成绩属于D级别。")
#             print("祝贺你通过考试！")
#         elif fenshu <= 59:
#             print("输入成绩属于E级别。")
#     print("好好学习，天天向上！")
# except:
#     print("输入数据有误！")
#


# # 斐波那契数列计算 B
# def fb(num_in):
#     if num_in == 0:
#         fb_result = 0
#     elif num_in == 1:
#         fb_result = 1
#     else:
#         fb_result = fb(num_in - 1) + fb(num_in - 2)
#     return fb_result
#
# num_input = input("")
# num_input_int = eval(num_input)
# fb_list = []
# sum_list = 0
# for i in range(num_input_int+1):
#     fb_i = fb(i)
#     if (fb_i <= num_input_int):
#         sum_list = sum_list + fb_i
#         fb_list.append(str(fb_i))
#     else:
#         break
# avr = int(sum_list/len(fb_list))
# fb_list.append(str(sum_list))
# fb_list.append(str(avr))
# print(", ".join(fb_list))


# # 2======================
# def jebona(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return jebona(n - 1) + jebona(n - 2)
#
# n = eval(input())
# len = 0
# ret = 0
# ls = []
# for i in range(0, n + 1):
#     ret = ret + jebona(i)
#     len += 1
#     ls.append(str(jebona(i)))
# ls.append(str(ret))
# ls.append(str(ret // len))
# print(", ".join(ls))


# # 站队顺序输出
# """
# mem = input("")
# print(mem, type(mem), eval(mem), type(eval(mem)))
#
# list.count(obj)
# 统计某个元素在列表中出现的次数
# list.index(obj)
# 从列表中找出某个值第一个匹配项的索引位置
# """
# from operator import itemgetter
# queue = eval(input())
#
# queue.sort(key = itemgetter(1))
# queue.sort(key = itemgetter(0), reverse = True)
#
# output = []
# for item in queue:
#     output.insert(item[1], item)
# print(output)
#

# # 合法括号组合的生成
# def foo(output, open, close, pairs):
#     if open == pairs and close == pairs:
#         ls.append(output)
#     else:
#         if open < pairs:
#             foo(output + "(", open + 1, close, pairs)
#         if close < open:
#             foo(output + ")", open, close + 1, pairs)
#
#
# n = eval(input())
# ls = []
# foo('', 0, 0, n)
# print(ls)

# # 用户登录（三次机会）
# #name_passwd.py
# i=0
# ret=1
# for i in range(0,3):
#      name=input()
#      passwd=input()
#      if name == "Kate" and passwd == "666666":
#           ret = 0;
#           break;
# if ret == 0:
#      print("登录成功！")
# else:
#      print("3次用户名或者密码均有误！退出程序。")




# # 凯撒密码：
# alphabet_s = 'abcdefghijklmnopqrstuvwxyz'
# alphabet_S = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# mingwen = input("")
# miwen = ""
# for i in mingwen:
#     if i in alphabet_s:
#         x = (alphabet_s.find(i) + 3) % 26
#         miwen = miwen + alphabet_s[x]
#     elif i in alphabet_S:
#         x = (alphabet_S.find(i) + 3) % 26
#         miwen = miwen + alphabet_S[x]
#     else:
#         miwen = miwen + i
# print(miwen)

# # 水仙花数
# # 列出三位数：
# l = []
# for i in range(1, 10):  # 1-9
#     for j in range(10):
#         for k in range(10):
#             num = i*100 + j*10 + k
#             if (i**3 + j**3 + k**3) == num:
#                 l.append(str(num))
# l_str = ",".join(l)
# print(l_str)


# # -*- coding:utf-8 -*-
# name = input("")
# msg_sent = input("")
# print("({})，我想对你说，({})".format(name, msg_sent))

# # -*- coding:utf-8 -*-
# msg_input = input("")
# for i in msg_input:
#     print(i)


# # -*- coding:utf-8 -*-
# import jieba
# # exclues = {"一首", "可以", "没有", "许多", "由于"}#多次尝试建立排除词的集合
# hamlet = "./hamlet.txt"
# with open(hamlet, "r", encoding="utf-8") as fo:
#   txt = fo.read()
# words = jieba.lcut(txt) #分词
# counts = {}
# for word in words:
#     # if len(word) == 1:
#     #     continue
#     # else:
#     counts[word] = counts.get(word, 0) + 1
# # #在这里删除排除词库里的词
# # for word in exclues:
# #     del counts[word]
# items = list(counts.items())
# items.sort(key=lambda x: x[1], reverse=True)
# #输出
# for i in range(10):
#     word, count = items[i]
#     print("{0:<10}, {1:>5}".format(word, count))


def getText():
    txt = open("hamlet.txt", "r").read()
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        txt = txt.replace(ch, " ")  # 将文本中特殊字符替换为空格
    return txt


hamletTxt = getText()
words = hamletTxt.split()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))