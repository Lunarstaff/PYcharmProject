#AutoTraceDraw.py
'''
自动轨迹绘制
-需求：根据脚本来绘制图形
-不是写代码而是写数据绘制轨迹
-数据脚本是自动化最重要的第一步

基本思路：
    -步骤1：定义数据文件格式（接口）
    -步骤2：编写程序，根据文件接口解析参数绘制图形
    -步骤3：绘制数据文件
'''

import turtle as tt
tt.title("自动轨迹绘制")#设置画布标题
tt.setup(800,600,0,0)#设置画布大小和位置
tt.pencolor("red") #设置画笔颜色 还可以写成 tt.pencolor("#ff0000")
tt.pensize(5)#设置画笔粗细

#数据读取
f_txt = "C:\\E-Data-File\\腾讯课堂\\Python入门\\PYcharmProject\\venv\\testcode\\testfiles\\data-txt.txt"#数据文件路径
data_ls = []#保存文件中的数据
f = open(f_txt,"r")#打开文件，只读
for line in f:
    line = line.replace("\n","")
    data_ls.append(list(map(eval,line.split(",")))) #map(),将第一个参数的功能作用与第二个参数的每个元素
f.close()

#自动绘制
for i in range(len(data_ls)):
    tt.pencolor(data_ls[i][3],data_ls[i][4],data_ls[i][5])#数据第4、5、6位是画笔颜色，取值0~1之间的小数
    tt.fd(data_ls[i][0])#数据第1位是行进长度
    if data_ls[i][1]:#数据第2位是判断是否右转，取值为0，1
        tt.right(data_ls[i][2])#数据第3位是转向绝对角度
    else:
        tt.left(data_ls[i][2])
