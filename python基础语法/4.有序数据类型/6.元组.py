"""
元组和列表的不同的两个地方
    1.元组输入是用圆括号，列表输入时用方括号
    2.元组是不可变的
        由元组是不可变带来的其他与列表不同的地方归入到第二点
        元组不可以增，删，改
        可以索引和切片,元组切片得到也是元组
"""
spam = (1,2,4,5,6,7,8)
print(type(spam))

print(spam[4])
spam1 = spam[:]
print(type(spam1))
print(spam1)

"""
空元组
    定义空元组：圆括号里面什么都不要填即可
    定义只有一个元素的元组：元组后面加一个逗号即可表示元组
    则否括号里面的是什么类型的数据，这个变量就是什么类型的数据
"""
empty = ()
empty1 = (1)
empty2 = (1,)
empty3 = ('hello world')
empty4 = ('hello world',)

print(type(empty))
print(type(empty1))
print(type(empty2))
print(type(empty3))
print(type(empty4))
 
a = (1,5,36,37,73,4,43,25)
temper = a.index(25)
print(temper)

#查
spam2 = (3,262,45,264,6,23,432,7,3452,31,724,6,8)
temp = spam2.index(45)
print(temp)