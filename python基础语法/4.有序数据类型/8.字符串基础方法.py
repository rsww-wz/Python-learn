"""
字符串方法：只能用在字符串上，和列表的方法类似
字符串函数：全局通常函数
"""

"""
    lower():将字符串全部转为小写字母
    upper()：将字符串全部转为大写字母
"""

string = 'Hello World'
print(string.lower())
print(string.upper())

"""
find()方法:
    作用：查找字符串中你需要的字符（可以是单个字符，也可以成多个字符）
    参数：
        第一个参数：要查找的字符，当可以匹配到多个字符的时候，返回的第一个匹配到的字符
        第二个参数：是从字符串的第几个位置开始匹配
    返回值：
        如果能匹配到，返回匹配到第一次出现字符的位置
        如果没有匹配到，返回-1，表示没有匹配到

count()方法：
    作用：统计你要匹配的字符在字符串中出现了几次
    返回值：出现的次数，没有匹配到就返回0
"""

string1 = 'hello world,Good morning,welcome'
temper = string1.find('or',1)
temper1 = string1.find('oc',0)
print(temper)
print(temper1)

spam = string1.count("o")
spam1 = string1.count("or")
spam2 = string1.count("x")
print(spam)
print(spam1)
print(spam2)
