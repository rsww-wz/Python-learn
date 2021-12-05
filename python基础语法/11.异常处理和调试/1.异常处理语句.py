"""
try和except语句是python程序的一种保护机制，当程序错误的时候，跳转到相应的错误类型的语句
的处理程序，不至于让程序奔溃

try和except语句的语法

第一种模式
    try：
        语句块1
    except异常类型1        
        语句块2
    except异常类型2
        语句块3

第二种模式
    try：
        语句块1
    except异常类型N：
        语句块N+1
    except：
        语句块N+2
    else：
        语句块N+3
    finally
        语句块N+4

except语句的语法：
    如果except后面有具体的异常类型，只会捕获到这种异常的，并执行对应的语句
    如果except后面没有任何错误类型，会捕捉所有的异常
    exception是所有异常的父类，如果except后面跟的是exception也会捕捉到所有错误

如何捕捉具体的异常类型
    except exception as 变量：
    把Exception捕获到的异常赋值给as后的变量

else语句的意思：
    如果try语句中正常执行，没有抛出异常，执行else语句

finally语句的意思：
    无论try语句中有没有抛出异常，最后都要执行finally语句

"""
x = int(input('请输入一个数字'))
a = [1,2,3,4,5,6,7]
try:
    print(a[x])
except:                               #except后面没有错误类型，捕获所有错误
    print('x is not a value index')
else:
    print('nothing')
finally:
    print('anyway')

"""
常见异常类型

    SystemExit：解释器请求退出

    FloatingPointError：浮点计算错误

    OverflowError：数值运算超出最大限制

    ZeroDivisionError：除（或取模）零（所有数据类型）

    KeyboardInterrupt：用户中断执行（通常是输入^C）

    ImportError：导入模块对象失败

    IndexError：序列中没有此索引（index）

    RuntimeError：一般的运行时错误

    AttributeError：对象没有这个属性

    IOError:输入输出操作失败

    OSError:操作系统错误

    KeyError:映射中没有这个键

    TypeError:对类型无效的操作

    ValueError:传入无效的参数

"""

try:
    print('try...')
    r = 10/0
    print('result:',r)
except Exception as e:        #把Exception捕获到的错误赋值给e
    print('except:',e)
else:
    print('else...')
finally:
    print('finally...')