#二分支if结构的紧凑形式
# <表达式1>if<条件>else<表达式2>
#判断条件，如果thue 返回表达式1，如果为false返回表达式2
guess  = eval(input("请输入："))
print("输入值{}是{}的".format(guess,"正确" if guess == 99 else "错误"))

#多分支结构
#对不同分数分级的问题
score = eval(input("请输入分数："))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
#.
#.
#.
else:
    grade = 'E'
print("输入的分数等级为{}".format(grade))

