"""
函数工具
主要用的是装饰器的工具

wraps函数
    给装饰器的inner该名字

reduce函数
    reduce函数的作用：连续计算，类似递归

partial函数
    作用：给函数的参数添加默认参数
    固定函数参数中某些参数的值
    被固定的参数不能修改了
    partial：第一个参数是原来的函数

"""

from functools import wraps
from functools import reduce
from functools import partial

def wrapper(func):
    @wraps(func)           #把inner的内置伪装成func
    def inner(*args,**kw):
        print("前")
        func(*args,**kw)
        print("后")

    return inner

@wrapper
def fun():
    print("hello world")

#改变了函数名字
print(fun.__name__)

def f1(name1,name2):
    print(name1,name2)

f2 = partial(f1,name2 = "小明")

f2(1)
f2(2)
f2(3)