"""
filter过滤器的语法
    参数
        第一个参数：函数或者方法
        第二个参数：序列

    返回值
        返回过滤掉的元素的列表,但是是一个对象，也是类型转换
        相等于带if语句的列表推导式
作用
    过滤列表元素

应用场景
    结合lambda匿名函数使用
    返回值必须是可以判断真假的结果，因为就是根据真假判断这个元素是否还应该保留在列表中
"""

lst = [1,0,0,1,0,1,1,0,0]
r = filter(lambda x:x,lst)
print(list(r))

lst1 = ['A','a','n','G','o','1']

#只保留大写
r = filter(lambda x:True if x.isupper() else False,lst1)
print(list(r))

#列表推导式
spam = [x for x in lst1 if x.isupper()]
print(spam)