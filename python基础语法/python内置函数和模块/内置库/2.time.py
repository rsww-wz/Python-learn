"""
时间有三种
    结构化时间
        gmtime()
        localtime()
    时间戳
        time.time()
        time.mktime()
    格式化时间
        time.strftime()
        time.strptime()

    时间戳和格式化时间的转换必须通过结构化时间来转化
    时间戳 - 结构化时间 - 格式化时间
    格式化时间 - 结构化时间 - 时间戳
"""
import time,pprint

# time模块被datatime取代，用到time的功能不多，只有两个
# time.sleep():让程序暂停一段时间,单位是秒
# time.time():获取当前时间

# 时间戳：1970,1,1,0,0,00到现在的时间，单位是秒

# pprint.pprint(dir(time))

t1 = time.time()
time.sleep(1)
t2 = time.time()
print(t2 -t1)

t3 = time.gmtime()
print(type(t3))
print(t3)

t4 = time.localtime()
print(t4)


