#time库
import time
dir(time)
['_STRUCT_TM_ITEMS', '__doc__', '__loader__', '__name__',
 '__package__', '__spec__',
 'altzone', 'asctime', 'clock',  'ctime', 'daylight',
 'get_clock_info', 'gmtime', 'localtime', 'mktime',
 'monotonic', 'perf_counter', 'process_time', 'sleep',
 'strftime', 'strptime', 'struct_time', 'time',
 'timezone', 'tzname']



1、时间获取
time() #获取当前时间戳，即计算机内部时间值，浮点数
time.time()
1522557277.0803845
#从1970年1月1日0时开始的

ctime() #获取当前时间并以易读方式表示，返回字符串
time.ctime()
'Sun Apr  1 12:35:33 2018'

gmtime() #获取当前时间，表示为计算机可处理的时间格式
time.gmtime()
time.struct_time(tm_year=2018, tm_mon=4, tm_mday=1, tm_hour=4, tm_min=36, tm_sec=31, tm_wday=6, tm_yday=91, tm_isdst=0)


2、时间格式化
#类似字符串格式化，需要有展示模板
strftime(tpl,ts)
'''
tpl是格式化模板字符串，用来定义输出效果
ts是计算机内部时间类型变量
'''
#例：
t = time.gmtime()
t
time.struct_time(tm_year=2018, tm_mon=4, tm_mday=1, tm_hour=4, tm_min=40, tm_sec=2, tm_wday=6, tm_yday=91, tm_isdst=0)
time.strftime("%Y-%m-%d %H:%M:%S",t)
'2018-04-01 04:40:02'


strptime(str,tpl)
'''
str是字符串形式的时间值
tpl是格式化模板字符串，用来字义输入效果
'''
#例：
timestr = '2018-04-01 04:40:02'
time.strptime(timestr,"%Y-%m-%d %H:%M:%S")
time.struct_time(tm_year=2018, tm_mon=4, tm_mday=1, tm_hour=4, tm_min=40, tm_sec=2, tm_wday=6, tm_yday=91, tm_isdst=-1)


#3、程序计时
#测量程序起止动作所经历时间的过程
#测量时间：
perf_cunter()
'''
#获取CPU时钟计数，返回一个CPU级别的精确时间计数值，
单位为秒，由于这个计数值起点不定，连续调用差值才有意义
'''
#例：
start = time.perf_counter()
start
5.140568855349533e-07
end = time.perf_counter()
end
11.923241539908807
end - start
11.92324102585192

sleep(s)
'''
s拟休眠的时间，单位是秒，可以是浮点数
'''


