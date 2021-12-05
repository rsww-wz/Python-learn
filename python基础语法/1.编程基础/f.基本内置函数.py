a = 2
b = 2.3
c = 'hello'

#print函数基本用法：括号内是变量名，或者直接是要打印的内容
"""
end="" 可使输出不换行
双引号之间的内容就是结束的内容,
可以是空格,也可以是其他字符,默认为换行

sep=",",不同参数之间的分割符号，默认是空格

官方文档：
print(...)
print(value, ... sep=' ', end='\n', file=sys.stdout, flush=False)

Prints the values to a stream, or to sys.stdout by default.
Optional keyword arguments:
file:  a file-like object (stream); defaults to the current sys.stdout.
sep:   string inserted between values, default a space.
end:   string appended after the last value, default a newline.
flush: whether to forcibly flush the stream.
"""
print(a)
print(2)
print(b)
print(2.3)
print(c)
print('world')
print('\n')


#id函数，查看变量的地址
print(id(a))
print(id(b))
print(id(c))
print('\n')

#type函数：查看变量的类型
print(type(a))
print(type(b))
print(type(c))
print('\n')

#len函数：查看变量的长度
print(len(c))
print('\n')
"""
    可以查看字符串以及后面的列表，元组，字典的长度
    整型和浮点型是没有长度的，不可以查看这两个类型的长度
"""


"""
    input函数：输入的内容保存到变量中，
        变量的类型是字符串，括号内是提示要输入的内容
    spam = input('请随便输入内容')
    print(type(spam))
    print(spam)
"""

#类型转换
temper = 3
tempers = 1.2
temper1 = float(temper)
temper2 = str(temper)
tempers1 = int(tempers)

print(temper1)
print(tempers1)
print('\n')

print(type(temper2))
print(type(temper1))
print(type(tempers1))


"""
    任何类型的变量都课转化为字符串类型，包括后面的列表，元组和字典
    整数类型可以转化为浮点数类型
    字符串>浮点型>整型
    如果浮点数转浮点数，只会保留整数部分，无论小数部分是多少都会被丢弃
"""