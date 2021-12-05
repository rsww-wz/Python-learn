a = 3
b = 3
spam = a is b
print('a is b? ' + str(spam))

string1 = 'hello'
string2 = 'hello'
spam1 = string1 is string2
print("string1 is string2? " + str(spam1) )

c = [1,2,3]
d = [1,2,3]
spam2 = c is d
print("c is d? " + str(spam2))

temp = (1,2,3)
temp1 = (1,2,3)
spam3 = temp is temp1
print('temp is temp1? ' + str(spam2))

"""
    相同值的不同变量
        int类型和str类型是同一个元素，地址是一样的
        list和tuple的地址是不一样的，不是同一个元素

    对象的三个特征
        值，身份（地址），类型
        其中身份和类型是不会变的，对象的值有些是可以变的

    int，str，list，tuple，set，dict这些数据类型都是类
    他们创建出来的对象的身份和类型是不会变的
    list，set，dict这些对象的值是可以变的
"""
