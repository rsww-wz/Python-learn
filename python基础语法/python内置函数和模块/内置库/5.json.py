"""
什么是json
    json是一种数据格式
    json的概念来源于前端
    前端把数据传输给后端，传输数据的格式就是json格式
    json就是一种数据传输的格式
    目前前后端传输数据基本用的都是json格式

json格式
    数据传输都是用字符串格式的，但是字符串里面的数据是json格式
    他是字符串格式，字符串里面的格式类似字典，但是里面用的是双引号
    python中这种格式叫字典

json和python中字典的区别
    主要是数据类型的写法不一样
    json  python
    true  True
    false False
    null  None

需求
    把python中的字典或者列表转化成json字符串
    把json字符串转换成python的字典或者列表

主要函数
    json.load(json,open()):文件中的json转化成对象
    json.loads:把json转化成对象
    json.dump(dict,open()):把文件中的对象转化为json
    json.dumps:把对象转化成json
    
"""

import json
import pprint

# pprint.pprint(dir(json))

# json默认采用的是ascii对中文的编码
# 处理中文，要使用ensure_ascii = False关键字参数

# 字典变字符串
dic = {"id":0,"name":"小明","age":19}
s = json.dumps(dic)
print(s,type(s))

print(ascii("小明"))
s = json.dumps(dic,ensure_ascii = False)
print(s)

# 字符串变字典
# 因为json里面用的是双引号，所以python字典要用单引号
s = '{"id":0,"name":"小明","age":19}'
d = json.loads(s)
print(d,type(d))

# 列表转化成json
lst = [True,False,None,"小明"]
print(json.dumps(lst,ensure_ascii=False))
spam = '[true, false, null, "小明"]'
print(json.loads(spam))
