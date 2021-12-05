"""
time.time
    时间戳：从1970年1月1日0时0分0秒，到现在的总秒数
"""

import time

#任务：给每个函数都加入time.time这条语句该如何实现？

"""
方法1:
    给每个函数都加入一条语句

    效果：非常不好
    
    因为编程的基本思想是：对修改是封闭的，对扩展是开放的
    当需求发生改变的时候，不应该改变函数本身
    而应该想办法用新的函数实现的新的功能

"""
def f1():
    print('this is a function')

def f2():
    print('this is a function')

f1()

"""
方法二：
    用函数式编程
    给这个新的要求新增加一个函数实现这个功能

    缺点：
        新增加的这个要求不是函数本身的，而是强行加入进去的
        没有体现函数本身的特性
        而且改变了调用函数的形式
"""
def print_current_time(func):
    print(time.time())
    func()

print_current_time(f1)
print_current_time(f2)
print('-'*50)

"""
方法三
    用装饰器

    缺点
        改变函数的调用方式，变的复杂
        一个函数的定义可以复杂，但是调用绝对不能复杂
"""

def decorator(func):
    def wrapper():
        print(time.time())
        func()
    return wrapper

f = decorator(f1)
f()
