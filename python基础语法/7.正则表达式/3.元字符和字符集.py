"""
元字符
    \d：匹配0-9
    \D：匹配除了0-9的字符
    \w：匹配26大小写个字母和0-9和下划线
    \W：除了w能匹配到的东西都可以匹配（包括不可见的字符，比如空号，回车等）
    \s：专门匹配那些不可见的字符
    \S：匹配可见字符

    一个元字符只能匹配一个字符

字符集
    符号：中括号
    匹配规则：中括号里面的内容是或关系
        中括号内表示的是范围，在这个范围内有你需要匹配到的内容
    
    理解：
        中括号里面的正则表达式是一个范围
        字符串有内容这个范围就可以匹配上
        所以字符集里面是或的关系

    中括号里面一般是元字符

总结
    概括字符集是对常用的字符集的一种简化表达，实际上都可是用字符集完成
    原则上，字符集和概括字符集都是只能匹配一个字符的
    关键是看引号，如果引号内只有一个字符集，那只能匹配一个字符

"""
import re

string = "34hd3k5d95\j 9f59ad ss02f     h2kdw3h46"

spam = re.findall('\d',string)         #匹配数字
spam1 = re.findall('\D',string)        #匹配非数字
spam2 = re.findall('\w',string)        #匹配字母和数字(下划线也是字母)
spam3 = re.findall('\W',string)        #匹配除了字母和数字之外的字符
spam4 = re.findall('\s',string)        #匹配不可见字符
spam5 = re.findall('\S',string)        #匹配可见字符

spam6 = re.findall('\d\D',string)
spam7 = re.findall('\s\S',string)
spam8 = re.findall('\w\W',string)

print(spam)
print(spam1)
print(spam2)
print(spam3)
print(spam4)
print(spam5)
print('\n')

print(spam6)
print(spam7)
print(spam8)

temp = re.findall('[a-z]',string)
temp1 = re.findall('[A-Z]',string)
temp2 = re.findall('[0-9]',string)
temp3 = re.findall('[0-9][a-z]',string)
temp3 = re.findall('[0-9][0-9]',string)

print(temp)
print(temp1)
print(temp2)
print(temp3)

string1 = "java C C++ python php JavaScript C#"

temp4 = re.findall('[A-Z][\W]',string1)
temp5 = re.findall('[\w][h]',string1)

print(temp4)
print(temp5)
