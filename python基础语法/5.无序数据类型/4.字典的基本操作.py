"""
字典的定义
    字典的元素是以键值对的形式存在的
    元素：'键'(key)：值(value)
    键值对之间用冒号隔开，元素之间用逗号隔开
    当键和值是字符串时，需要用引号
    字典用花括号定义

空字典的定义
    一对空的花括号即可

字典的性质 
    字典的键
        键可以是任何类型的数据
    字典是无序的
        所以字典不可以切片
    字典可以索引
        字典的键使得字典可以用键来索引
        索引字典不存在的键，会报错
        索引也是用中括号，中括号里面是键
    字典可以打印
        按照key-value的形式打印

"""

myCat = {'size':'fat','color':'grey','disposition':'loud'}
spam = {1:'big',2:'middle',3:'small'}
print(myCat['color'])
print(spam[3])

"""
增/改
    字典名[key] = value
        如果键不存在，添加键值对
        如果键存在，修改键值对
        添加键值对是当场修改，修改前后地址一样

删
    用del语句
        del 字典名[key]
        如果key不存在，会报错
        删除前后的地址也是一样的

查
    查key：可以用索引来查元素
    查value：可以用身份运算符is来查value是否存在
"""

print(id(myCat))
myCat['name'] = 'bigmouse'
print(myCat)
print(id(myCat))

print(id(spam))
del spam[2]
print(spam)
print(id(spam))

#遍历
for i in myCat:
    print(i)