"""
函数内嵌套函数，并且返回内层函数
"""

import time
import random

#定义高阶函数
def f1():
    def f2():
        print("hello world")
    #返回内层函数
    return f2

#调用外层函数
spam = f1()
#调用内层函数
spam()

#内层函数带参数
def f3():
    def f4(x):
        return x ** 2
    return f4

spam1 = f3()
print(spam1(5))

#外层函数有参数
def f5(x):
    def f6(y):
        return x * y
    return f6

spam2 = f5(7)
print(spam2(9))



