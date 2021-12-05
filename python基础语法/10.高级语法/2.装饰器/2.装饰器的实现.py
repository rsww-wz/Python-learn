"""
定义装饰器的方式都是上嵌套的函数
但是调用上比较麻烦

如果能实现和原来一样的调用方式，又能有装饰器的效果？
    在被调用的函数前面加上：@装饰器名

装饰器的最大优势就是不改变函数的调用方式


装饰器的理解
    装饰器函数里面是新增加的功能
    在调用函数前面加上装饰器
    这个函数就是有装饰器函数里面的功能

    当调用这个被装饰的函数不能改变调用方式，就能有新增加的功能
"""
import time

def decorator(func):
    def wrapper():
        print(time.time())
        func()
    return wrapper

@decorator
def f1():
    print('this is a function')

@decorator
def f2():
    print('this is a function')

f1()
f2()