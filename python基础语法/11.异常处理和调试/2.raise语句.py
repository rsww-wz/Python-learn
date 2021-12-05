"""
程序异常和程序错误
    程序发生异常和程序执行错误，它们完全是两码事
    程序由于错误导致的运行异常，是需要程序员想办法解决的
    但还有一些异常，是程序正常运行的结果，比如用raise手动引发的异常
        程序是正常的，但是内容如果不符合要求的换可以人为抛出异常

raise语句的理解：
    raise是用来人为的触发异常,在程序的指定位置手动抛出一个异常
    触发异常之后也会跳转到except语句，执行对应异常的代码
    每次执行 raise 语句，都只能引发一次执行的异常
    一旦执行了raise语句,raise之后的语句不在执行    

raise的语法：
    raise [Exception/exceptionName('reason')]
    raise Exception/具体的异常类型('异常说明的内容')
        Exception/exceptionName是可选参数
        reason也是可选参数
    
    Exception是一个(异常)类，如果直接打印不会有任何信息
    所以Exception后面可以加上可选参数，来说明异常的信息

    如果可选参数全部省略，则raise会把当前错误原样抛出
    如果仅省略(reason)，则在抛出异常时，将不附带任何的异常描述信息

    注：Exception是所有异常的父类，如果except后面跟的是Exception也会捕捉到所有错误
        
        
raise语句有如下三种常用的用法：
    1.raise：该语句引发当前上下文中捕获的异常（比如在 except 块中）
        或默认引发RuntimeError异常
    2.raise[exceptionName]：表示引发执行类型的异常
    3.raise[exceptionName[(reason)]]：在引发指定类型的异常的同时，附带异常的描述信息
    
raise语句可以配合try语句使用，raise语句引发的异常也是可以跳转到except语句中的

自定义异常类
    需要自己创建一个类，但是这个类什么都不用写，写个pass即可
    但是需要继承Exception类


"""

#不用try语句
def sum(a,b):
    if a <0 or b < 0:
        #raise                                   #打印原样错误
        #raise Exception                         #只会显示Exception
        raise Exception("你的输入有负数")         #显示异常内容

    r = a + b
    return r

#用try语句
print(sum(1,7))


try:
    s = None
    if s is None:
        print('s是空对象')
        raise NameError          #手动引发一个NameError的异常
    print(len(s))                #引发异常后，raise后面的语句不执行

except Exception:              #配合try语句使用，raise引发的异常可以跳转到except语句
    print('空对象没有长度')

#自定义异常类

class MyError(Exception):
    pass

print('正常执行')
raise MyError('这是个自定义的异常类')