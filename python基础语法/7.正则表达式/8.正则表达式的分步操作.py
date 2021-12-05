"""
导入re库：regular expression -- regex

创建正则表达式
    complie()方法：
        作用：返回一个regex对象
        参数：正则表达式

        理解：这个是根据正则创建出来的对象，专门处理符合该正则的字符串

search()方法：
    search方法是regex对象的方法
    作用：查找符合正则的字符串
    返回值
        如果找到：返回一个Match对象
        如果没有找到：返回None

    Match对象
        Match对象有一个group方法
        group()方法：
            返回匹配到的第一个字符串
            没有匹配到的对象调用group方法会报错

findall()方法：
    search是返回第一次匹配到的字符
    findall是返回所有匹配到的字符

    返回值
        如果调用在没有分组的正则表达式上，返回匹配到的列表
        如果调用在有分组的正则上，返回一个字符串的元组的列表
            字符串方法元组里面，元组是列表的元素

sub()方法：
    sub()也是regex的对象的方法
    第一个参数：字符串
    第二个参数：替换的字符串
"""

import re

string = 'hello world'
string1 = '984023750137'

wordRegex = re.compile(r'[a-z]+')  # 创建正则对象
temp = wordRegex.search(string)  # 返回March对象
temp1 = wordRegex.search(string1)
print(temp)  # 匹配到了返回span，match
print(temp1)  # 没有匹配到返回None

spam = temp.group()  # March对象调用group方法，返回字符

print(spam)

temp2 = wordRegex.findall(string)
print(temp2)

string2 = "34h6ld3k5d956j9f5h9adss2fhing2kdw3h46"

NumberRegex = re.compile(r'(\d[a-z]){2,4}')  # 分步操作多了一个中间对象
spam1 = NumberRegex.findall(string2)  # 如果这个正则要处理很多字符串
print(spam1)  # 可以为这个正则创建一个对象

spam2 = re.findall('(\d[a-z]){2,4}', string2)
print(spam2)
