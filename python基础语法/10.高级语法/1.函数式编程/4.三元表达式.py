"""
语法
    条件判断为真的结果 if 条件判断 else 条件判断为假返回的结果
    
    返回值，表达式运算的结果

应用场景
    一般是用在匿名函数和列表推导式中
"""

x = 50
y = 100
spam = x if x > y else y
print(spam)

spam1 = 'hello world' if x < y else 'Good morning'
print(spam1)

#匿名函数
value = lambda x,y:x if x > y else y
print(value(34,90))
print(value(100,45))

#列表推导式
spam = [x*5 if x%2 == 1 else x*3 for x in range(10)]
print(spam)