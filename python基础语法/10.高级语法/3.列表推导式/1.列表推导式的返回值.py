"""
列表推导式的作用
    用一个列表推导出一个新的序列
    这个序列不一定是列表，可以是字典，也可以是元组

列表推导式的实现
    可以用命令式编程的for和if循环实现
    也可以用函数式编程的filter，map，以及reduce函数实现

列表推导式语法
    [表达式 for 迭代变量 in 可迭代对象 [if 条件表达式] ]

列表推导式的返回值
    用什么字面量表示这个推导式，这个推导式的返回值就是它的类型
    元组类型不可以直接打印，它是一个可迭代对象，即可以用于遍历for循环
"""

lst1 = [1,2,3,4,5,6,7,8,9]

spam = [i*i for i in lst1]
spam1 = {i*i for i in lst1}
spam2 = (i*i for i in lst1)

print(spam)
print(type(spam))
print('-'*50)

print(spam1)
print(type(spam1))
print('-'*50)

print(type(spam2))
for i in spam2:
    print(i,end = ' ')