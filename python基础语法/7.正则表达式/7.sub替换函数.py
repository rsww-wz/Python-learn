"""
字符串替换方法
replace()
    作用：替换字符串
    参数
        第一个参数：被替换掉的字符串
        第二个参数：要替换上去的字符串
    字符串是不可变的，要替换的话，要新的变量（同名）接收被替换后的变量

    简单的字符串替换用内置方法即可，如果替换的内容比较复杂，
    替换的数量也多，就要用正则表达式搜索，然后用sub函数替换

sub()函数
    参数
        第一个参数：正则表达式（查找要替换的字符）
        第二个参数：字符串（要替换上去的字符串）
        第三个参数：被替换字符串的名字
        第四个参数：替换次数，默认是0，表示匹配到的都要替换
        第五个参数：匹配模式
    返回值
        修改后的字符串
"""

string = 'hello world'
string = string.replace('world','Good')
print(string)

import re

string1 = "he is doing his homework,at the same time he is playing games"
string1 = re.sub(' is',' was',string1)
print(string1)

string2 = 'there are total 54 people,and there are 54 people have been sent to Mars'
string2 = re.sub('[\d]+','100',string2,1)
print(string2)


"""
sub()函数接受函数作为参数

    作用：能实现动态的字符串替换

    sub函数接受函数作为参数的返回值
        返回值是一个对象，这个对象有两个实例变量
            span：类型是元组，内容是匹配到的字符串在整个字符串的位置
            match：类型是字符串，内容就是匹配到的字符串
            这两个变量作为一组参数返回
        
    如何操作返回的对象
        这个对象有一个方法

        group()方法
            调用：对象+点+函数名() --- 参数+点+group()
            返回值
                返回值就是在group函数内部对字符串的操作的结果
                用一个变量去接收group方法的返回值，
                返回把这个变量作为函数的返回值给sub函数

    函数的执行过程
        1.先定义处理作为sub参数的函数
            
        2.调用sub，把处理函数传进去

        3.sub函数匹配对应的字符

        4.sub函数发现，替换字符是函数，就把匹配到的字符作为对象返回给处理函数

        5.处理函数的参数就是匹配到的对象参数(span,match)

        6.处理函数调用group方法，处理字符，结果返回给sub函数

        7.sub函数拿到字符，替换字符串

    注意
        函数的定义必须在sub函数使用之前，不然会传入一个没有被定义的函数进去
"""

string3 = 'pythonC#javaC#PHPC#'

#def convert(value):
#    print(value)


string4 = 'A9C3721D86'

def convert(value):
    matched = value.group()
    if int(matched) >= 6:
        return '9'
    else:
        return '0'

spam = re.sub('\d',convert,string4)
print(spam)


"""
删除匹配到的字符串
    写一个空函数，把函数传进sub函数作为参数即可

    或者替换的字符串用空字符即可
"""

string5 = 'ther4e a8re m2575any7 peo3ple93a3nd19 t35he6y5 a4re ea354ti3ng dinn74er'
string6 = 'ther4e a8re m2575any7 peo3ple93a3nd19 t35he6y5 a4re ea354ti3ng dinn74er'

def convert1(value):
    pass

spam1 = re.sub('[\d]*',convert1,string5)
print(spam1)

spam2 = re.sub('[\d]+','',string6)
print(spam2)