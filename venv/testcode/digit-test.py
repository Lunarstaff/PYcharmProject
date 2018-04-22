#digit-test.py
#七段数码管
"""
需求：
用程序绘制七段数码管

turtle绘图体系 --> 七段数码管
显示日期：2018年04月22日

1、绘制单个数字对应的数码管
2、获得一串数字，绘制对应的数码管
3、获取当前系统日期时间
"""

#绘制单个数码管
import turtle as t
import time
def drawGap(): #绘制间隔
   t.penup()
   t.fd(5)

def drawLine(draw): #绘制单段数码管
   drawGap()
   t.pendown() if draw else t.penup() #if的紧凑形式
   t.fd(40)
   drawGap()
   t.right(90)

def drawDigit(digit):#根据数字digit绘制七段数码管
   drawLine(True) if digit in [2, 3, 4, 5, 6, 8, 9] else drawLine(False)
   drawLine(True) if digit in [0, 1, 3, 4, 5, 6, 7,8,9] else drawLine(False)
   drawLine(True) if digit in [0, 2, 3, 5, 6, 8, 9] else drawLine(False)
   drawLine(True) if digit in [0, 2, 6, 8] else drawLine(False)
   t.left(90)
   drawLine(True) if digit in [0, 4, 5, 6, 8, 9] else drawLine(False)
   drawLine(True) if digit in [0, 2, 3, 5, 6, 7, 8, 9] else drawLine(False)
   drawLine(True) if digit in [0, 1, 2, 3, 4, 7, 8, 9] else drawLine(False)
   t.left(180)
   t.penup() #为绘制后续数字确定位置
   t.fd(20)  #为绘制后续数字确定位置,可设置数码管间隔

def drawDate(date): #data为日期，格式定为 ‘%Y-%m=%d+’
   t.pencolor("#FF0000")
   for i in date:
      if i == '-':
         t.write('年',font = ("Arial",18,"normal"))#字符串中如果是指定字符就绘制对应内容
         t.pencolor("green")
         t.fd(40)
      elif i == '=':
         t.write('月', font=("Arial", 18, "normal"))
         t.pencolor("blue")
         t.fd(40)
      elif i == '+':
         t.write('日', font=("Arial", 18, "normal"))
      else:
         drawDigit(eval(i)) #字符串中如果不是指定字符就直接绘制

def main():
   t.setup(800,350,200,200)
   t.penup()
   t.fd(-300)
   t.pensize(5)
   drawDate(time.strftime('%Y-%m=%d+',time.gmtime())) #获取当前系统日期并格式化
   t.hideturtle()
   t.done()

main()
