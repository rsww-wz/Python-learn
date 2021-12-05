"""
常用
re.findall():全局查找
re.search():查找第一个结果，用group方法获得匹配到的结果
re.finditer():返回一个迭代器，用for循环加group方法得到匹配到的所有结果 
re.match():从头开始匹配，如果字符串的第一个位置不符合正则，就不匹配了
    也是需要用group方法获得匹配到的结果

其他    
    re.split():切分字符串，返回列表
    re.sub()：替换字符串
    re.subn():替换字符串，会返回替换了多少次
    re.complie()：先加载正则，后面可以直接用这个正则，相当于给正则创建了一个对象
        可以条用上面的所有函数

爬虫
    一个正则里面，如果不是所有东西都是我们想要的，我们可以给想要的东西加括号
    其实就是分组，同时还可以给这个组起名字
    概括：从匹配到结果拿到指定数据
    起名字：(?<name>正则表达式)
    r"今天吃了(?<面>2)碗面，喝了(?<水>4)杯水"

应用
    匹配手机号：match()
    搜索字符串：search()
    爬虫：finditer()
    万能：findall(),如果返回的东西多，消耗内存严重
"""

import re

string = "今天吃了2碗面，喝了4杯水"

r = re.findall("\d",string)
r1 = re.search('\d',string)
r2 = re.match('\d',string)
r3 = re.finditer('\d',string)

print(r)
print(r1.group())
print(r2)

for i in r3:
    print(i.group())

res = re.split('\d',string)
print(res)

res1 = re.findall('今天吃了(?P<面>\d)碗面，喝了(?P<水>\d)杯水',string)
res2 = re.finditer('今天吃了(?P<面>\d)碗面，喝了(?P<水>\d)杯水',string)
print(dict(res1))

for item in res2:
    # print(item.group("面"))
    # print(item.group("水"))
    print(item.groupdict())
    