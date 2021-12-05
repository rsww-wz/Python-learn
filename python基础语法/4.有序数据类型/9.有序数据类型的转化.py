spam = [1,2,3,4,5]
spam1 =(1,2,3,4,5)
spam2 = "1,2,3,4,5"

print(type(spam))
print(type(spam1))
print(type(spam2))

temper = list(spam1)
temper1 = list(spam2)

temper2 = str(spam)
temper3 = str(spam1)

temper4 = tuple(spam1)
temper5 = tuple(spam2)

print(temper)
print(temper1)
print(temper2)
print(temper3)
print(temper4)
print(temper5)

spam3 = [1,'hello',2,'world']
spam4 = [[1,'h3'],['ok',3],'love']
temper6 = tuple(spam3)
temper7 = str(spam3)
temper8 = str(spam4)

print(temper6)
print(temper7)
print(temper8)

"""
有序数据类型包括：
    列表
    元组
    字符串

    其中不可变的数据类型有：元组，字符串

转化：
    列表，元组和字符串之间都是可以无条件转换

有序数据类型的通用操作：
    +：连接两个相同的容器
    *：复制容器几次
    is:身份运算符，判断一个元素是否在里面
    下标索引
    切片
    遍历
"""