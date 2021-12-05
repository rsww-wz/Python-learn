"""
异常的位置
    全局
    函数内

异常的传播
    如果异常出现在全局中，只会显示一个错误，就是第一个错误
        如果后面还有错误也不会显示了，错误不会继续传播

    如果异常出现在函数内
        不调用
            不调用这个函数不会显示异常
        调用
            如果在函数内处理了异常，不会显示异常
            如果在函数外处理类异常，也不会显示异常
            如果没有处理异常 ，至少会显示两个异常
                第一个异常是函数内的错误
                第二个异常是函数的调用处(全局作用域)

                如果没有对异常处理，会一直传播到最终调用处(全局作用域)
                如果在传播过程中处理了异常，就不会显示异常

如何判断出现异常的位置
    看TraceBack返回的最后一个异常位置

异常是如何传播的
    当程序运行过程中出现异常以后，所有的异常信息会被保存一个专门的异常对象中
    而异常传播时，实际上就是异常对象抛给了调用处
    每一个异常都有一个专门的类，这个类的名字就是异常类型，如：ZeroDivisionError
    当出现异常的时候，会创建这个异常类的实例化对象，并且传播这个对象

如何获得TraceBack的字符串
    导入traceback模块
    调用方法：traceback.format_exc()
    一般都是配合raise语句和try语句使用

"""

import traceback

try:
    raise Exception('this is an error')
except:
    spam = traceback.format_exc()
    print(type(spam))
    print(spam)

print(ZeroDivisionError)           #<class 'ZeroDivisionError'>
def fn():
    print(10/0)

def fn1():
    print('hello world')
    fn()

def fn2():
    print("hello")
    fn1()

fn2()

