"""
语法：
    定义：lambda 参数列表：表达式

    表达式
        这个位置只能是表达式，不能是语句(不能有赋值号)
        也就是不能写一些复杂的语句
        最常用的就是三元运算了

    返回值
        表达式的结果作为返回值
        用一个变量接受返回值，然后这个变量就相当于函数名
        可以实现函数的调用

应用场景
    可以实现一些比较简单的函数
    最常用的是把匿名函数作为函数参数
    比如正则表达式中的sub函数
"""

add = lambda x,y:x + y
print(add(3,6))
