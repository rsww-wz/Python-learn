"""
可数参数：
    在对应的装饰器内部的函数加入相应的参数即可

可变参数
    可以用可变参数：*args
    *变量名:表示可以变数量的参数
    被调用的函数无论本身有多个参数，加上装饰器后，都能实现装饰器的效果

关键字参数
    **kw
    可变参数不包括关键字参数
    如果函数有关键字参数，可以用**函数名

拓展：
    如果你想调用一个你不熟悉的函数
    可以用*args和**kw作为函数列表，可以调用任何参数
    *args和**kw可以包括参数列表的所有参数

装饰器的最终效果
    调用对任何被装饰的函数都能实现装饰器的效果

注意
    函数可以不止一个装饰器
    装饰器很灵活，可以在装饰器内部写一些判断，符合条件，装饰器才能生效
"""
import time

def decorator(func):
    def wrapper(*args,**kw):
        print(time.time())
        func(*args,**kw)
    return wrapper

@decorator
def f1(func_name):
    print('this is a function ' + func_name)

@decorator
def f2(func_name,func_line):
    print('this is a function ' + func_name + ' ' + str(func_line))

@decorator
def f3(func_name,func_line,**kw):
    print('this is a function ' + func_name + ' ' + str(func_line))
    print(kw)

f1('test func')
f2('test func',10)
f3('test func',10,a = 10,b = 20)


"""
装饰器的最终形式

def decorator():
    def function(*args,**kw):
        pass
    return function(*args,**kw)

"""