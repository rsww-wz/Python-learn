"""
列表推导式的条件的理解
    是对每个原始元素做判断，是否符合条件
    如果符合条件就可以加入列表
    如果不符合就不能放人列表

语法
    [表达式 for 迭代变量 in 迭代对象 if 条件]
"""


lst = [34,-23,90,-1,-54,45,87,-25]

#列表推导式实现
spam = [x for x in lst if x > 0]
print(spam)
print('-'*50)

#for循环实现
spam = []
for i in lst:
    if i > 0:
        spam.append(i)
print(spam)  

#综合,用列表推导式实现
spam1 = [x if x%2==0 else x**2 for x in lst if x > 0]
print(spam1)
print('-'*50)

#用for循环实现
spam2 = []
for i in lst:
    if i > 0:
        if i % 2 == 0:
            spam2.append(i)
        else:
            spam2.append(i ** 2)
print(spam2)
