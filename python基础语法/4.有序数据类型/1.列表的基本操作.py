#列表的定义
a = [1,2,3,4,5,6,7,8,9]
b = ['hello','world']
c = [[1,3,5],[2,4,6]]

print(a)
print(b)
print(c)

#访问列表元素
spam = a[4]
spam1 = b[0]
spam2 = c[1]
spam3 = b[0][1]
spam4 = c[1][2]
spam5 = a[-1]
spam6 = b[-1]
spam7 = c[-1]

print(spam)
print(spam1)
print(spam2)
print('\n')

print(spam3)
print(spam4)
print('\n')

print(spam5)
print(spam6)
print(spam7)
print('\n')

#列表长度
length = len(a)
length1 = len(b)
length2 = len(c)
length3 = len(b[0])

print(length)
print(length1)
print(length2)
print(length3)

#列表的遍历
for i in a:
    print(i,end = ',')
print('\n')

for i in b:
    for j in i:
        print(j,end = ',')
print('\n')

for i in c:
    for j in i:
        print(j,end = ',')  
print('\n') 

#列表遍历技巧
for i in range(len(a)):
    print(a[i],end = ',')

#列表的运算
temper = a + c
temper1 = a * 3
temper2 = a + b

print(temper)
print(temper1)
print(temper2)

"""
列表的定义：
    列表的元素可以是任何数据类型，包括可以嵌套列表自己
    列表元素之间用逗号隔开

访问列表元素
    可以用下标访问列表元素，下标可以正数也可以是负数，但是不可以是小数
    列表的下标是从零开始的，也就是第一个元素的下标是0
    负数下标表示从后面开始数，最后一个元素的下标是-1
    注意：下标不可以超过列表的元素个数，否则会报错

列表的长度
    可以用len函数计算列表的长度
    但是如果列表里面是字符串，或者其他组合，计算的是他们的个数
    如果有计算一个字符串的长度，可以用下标取出改元素再用len函数计算

遍历列表
    遍历列表一般都是用for循环
        for 循环变量 in 列表名：
    如果列表元素是组合类型的，需要用嵌套的for循环才能遍历到组合里面的元素
    嵌套了几层，就要用几个for循环

    遍历列表的另外一个思路：
        可以用列表的个数生成序列，用这些序列作为列表的下标访问列表元素
        for 循环变量 in range(len(列表名))

列表的运算
    +：表示两个列表相加组合成一个列表，无论这两个列表的元素是否相同
    *：表示一个列表复制几次，组合成一个列表
"""