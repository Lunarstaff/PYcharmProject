#hanoi-test.py


"""
def rvs(s):
   if s == '':
      return s
   else:
      return rvs(s[1:] + s[0])
汉诺塔问题
n个圆盘从A柱移到C，大圆盘不能在小圆盘上

拆解为当前n与 n-1 之间的关系

"""

count = 0
def hanoi(n,src,dst,mid):
   global count
   if n == 1:
      print("{}:{}->{}".format(1,src,dst))
      count += 1
   else:
      hanoi(n-1,src,mid,dst)
      print("{}:{}->{}".format(n,src,dst))
      count += 1
      hanoi(n-1,mid,dst,src)

hanoi(1,'A','B','C')
print(count)
