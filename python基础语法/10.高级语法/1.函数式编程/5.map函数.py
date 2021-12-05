"""
map函数
    参数
        第一个参数：函数
        第二个参数：一个集合（有序列表）

    返回值
        是一个map对象
        可以用list类型转换成列表

作用
    相对于列表推导式

应用场景
    配合lambda匿名函数使用
    lambda有多个参数，map就需要多个列表
    这两个列表的大小可以不一样，但是会以短的那个列表为基准
"""

lst = range(10)

def square(x):
    return x * x

#map函数实现
spam = map(square,lst)
print(list(spam))

#配合匿名函数实现
spam1 = map(lambda x: x * x,lst)
print(list(spam1))

#用列表推导式实现
spam2 = [x*x for x in lst]
print(spam2)


#匿名函数有多个参数
lst1 = range(20,30)
spam3 = map(lambda x,y:x + y,lst,lst1)
print(list(spam3))

#列表元素不相等
lst2 = range(20,30,2)
spam4 = map(lambda x,y:x + y,lst,lst2)
print(list(spam4))