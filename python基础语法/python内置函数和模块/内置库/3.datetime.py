"""
datetime 里面包括三种类型
    date:年月日
    time：时分秒
    datetime：年月日时分秒
    
    主要掌握datatime类型即可

    注意：导入datetime模块必须是from datatime import datatime
    datetime.now():返回现在时间，格式是带下划线的
    datatime(时间):返回给定时间格式
    .total_seconds()方法：返回该时间段的秒数

格式化时间
  格式
    %y 两位数的年份表示（00-99）
    %Y 四位数的年份表示（000-9999）
    %m 月份（01-12）
    %d 月内中的一天（0-31）
    %H 24小时制小时数（0-23）
    %I 12小时制小时数（01-12）
    %M 分钟数（00-59）
    %S 秒（00-59）
    %a 本地简化星期名称
    %A 本地完整星期名称
    ‰b 本地简化的月份名称
    %B 本地完整的月份名称
    %C 本地相应的日期表示和时间表示
    %j 年内的一天（001-366）
    %p 本地AM.或PM.的等价符
    %U 一年中的星期数（00-53）星期天为星期的开始
    ‰N 星期（0-6），星期天为星期的开始
    %W 一年中的星期数（00-53）星期一为星期的开始
    %x 本地相应的日期表示

方法
    strftime()方法：把时间转换成给定字符串格式
    strptime()方法：把给定字符串格式转换成时间
"""

from datetime import datetime
from datetime import date
from datetime import time
import time
import pprint

# print(dir(datetime))
# pprint.pprint(dir(datetime))

print(datetime.now())
print(datetime(2018,3,12,11,20))
t1 = datetime(2018,6,8,0,00,00)
t2 = datetime.now()
spam = t2 - t1
print(spam)
print(spam.total_seconds())

#把时间转换成字符串
t = datetime.now()

# 编码原因会报错,因为里面包含了中文，中文没有转化为unicode编码失败的
# print(t.strftime("%Y年%m月%\d日 %H小时%M分钟%S秒"))
print(t.strftime("%Y{y}%m{m}%d{d} %H{h}%M{f}%S{s}")\
    .format(y='年',m='月',d='日',h='小时',f='分钟',s='秒'))

# 把字符串转换成时间
# time1 = input("请输入第一个时间(yyyy-mm-dd HH:MM:SS)")
# time2 = input("请输入第一个时间(yyyy-mm-dd HH:MM:SS)")

# t1 = datetime.strptime(time1,"%Y-%m-%d %H:%M:%S")
# t2 = datetime.strptime(time2,"%Y-%m-%d %H:%M:%S")
# print(t2 - t1)

#date
# pprint.pprint(dir(date))
print(date.today())

#time
# pprint.pprint(dir(time))
print(time.time())



