"""
闭包在高阶函数的基础上实现
闭包 = 内层函数 + 外层函数变量
闭包可以访问外层函数的变量

闭包是指接受调用外层函数的返回值的那个变量，返回的其实就是内层函数
    不过访问上一级函数的变量,但是只能访问，不能修改

如果要修改需要在内层函数使用nonlocal关键字来声明变量

外层函数没有变量，访问了外层函数的参数也是闭包
"""

import time
import random

def f1(x):
    def f2(y):
        return x + y
    return f2

def f3():
    num = 10
    def f4():
        nonlocal num 
        num += 1
        return num
    return f4

temp = f3()
print(temp())

spam = f1(34)
print(spam(45))

def spacetime():
    t1 = time.time()
    def number(x):
        lst = list(range(x))
        lst = random.shuffle(lst)
        t2 = time.time()
        return t2 - t1
    return number

times = spacetime()
print(times(1000))
