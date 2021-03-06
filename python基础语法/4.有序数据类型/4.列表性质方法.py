"""
    函数：全局通用
    方法：它是类(对象)里面定义的函数，所以它属于这个对象的函数，不是通常的
    python一切皆对象，所以列表也是python的对象的
    python系统给列表这些对象定义了许多方法，增加了列表的性质

    如果调用方法：
        对象名.方法名(参数)
        对象名就是列表名
"""

"""
增:
    append()方法，将新增元素添加到列表末尾
    insert()方法:
        可以列表的任意位置插入新增元素
        两个参数，一个位置参数，一个新增元素
        位置参数：可以是负数，如果要在最后一个位置插入新增元素，用负数是不行的
            可以用len函数，计算出列表长度，作为位置参数，可以插入到最后位置
    append()和insert方法的返回值都是：None
    append()和insert方法都是对列表当场修改了，不可恢复原来的列表
    修改前后的地址是一样的，也就是修改前后他们是一个列表

    extend()方法：
        作用：在列表的后面增加列表
        两个列表并成一个列表，不会产出新的列表
        修改前后是同一个列表

    和列表加法运算的区别：
        列表加法运算也是在列表的后面加上一个列表
            但是会产生一个新的列表，原来的两个列表都能保留
        extent()方法，不会产生新的列表，原来的列表不能保留
"""

spam = [1,2,3,4,5] 
spam1 = [11,12,13]
print(id(spam))
spam.append(0)
print(spam)
spam.insert(0,9)
print(spam)
spam.insert(-1,7)
print(spam)
spam.insert(len(spam),8)
print(spam)
print(id(spam))
print('\n')

temper = spam + spam1
print(temper)
print(id(temper))

spam.extend(spam1)
print(spam)
print(id(spam))


"""
删
    del语句
        删除列表下标所处的值，被删除后面的所有值，都将向前移动一个下标
        删除的下标超出元素个数会报错
        del语句也可以用来删除变量
        删除前后是同一个列表
    remove()方法
        给remove方法传入一个值，它将从列表中删除
        试图删除不存在的值会报错
        如果一个值在列表中出现多次，只有第一次出现的值会被删除
        删除前后也是同一个列表
    总结：
        如果知道要删除值的下标，用del语句
        如果知道用删除的值，用remove方法
"""
a = [1,2,3,4,5,6,7,8]
print(id(a))
del a[len(a)-1]
print(a)
print(id(a))

a.remove(4)
print(a)
print(id(a))

"""
查
    index()方法：
        传入一个值，如果值存在，就返回该值的下标
        列表名.index(值)
        如果一个值在列表中出现多次，只会返回第一次出现的值的下标
        如果列表中没有这个值，就会报错
"""

b = [1,2,3,4,5,6,7,8,5]
print(b.index(4))
print(b.index(5))

"""
改
    知道下标
        改列表元素的值，可以直接用下标索引去改
        下标索引出来的元素，既可以做左值，也可以做右值
    知道值
        可以用index方法，索引出下标，在去修改列表的值
        列表名[列表名.index(值)] = 修改值
"""

aa = [1,2,3,4,5,6,7]
aa[0] = 0
print(aa)

aa[aa.index(7)] = 11
print(aa)