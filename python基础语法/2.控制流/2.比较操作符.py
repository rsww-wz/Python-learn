"""
    比较操作符：比较两个值，返回值是一个布尔值
    比较操作符一共有6个操作符，其中只有等于和不等于适用于任何数据类型的值，
    其他的都是只用于整型和浮点型的值
    ==:等于
    !=:不等于
    比较操作符会自动返回一个布尔值，真返回True，假返回False  
"""

a = 42 == 42
b = 43 ==29
c = 2 != 3
d = 3 > 3
e = 3 >= 3

aa = 3
bb = 3.0
cc = aa == bb

print(a)
print(b)
print(c)
print(d)
print(e)

print(id(aa))
print(id(bb))
print(cc)

string = 'hello'
string1 = 'Hello'
value = string == string1
print(value)

spam = 'A'
spam1 = 65
value1 = spam == spam1
print(value1)

"""
    ==和!=
        比较数值类型：不是根据地址是否一样判断的，就是根据他们的值是否相等判断的
            只有他们的值是一样的，即使是整型和浮点型也是相等的
        比较字符串类型：字符串就是必须一模一样才能相等，
            底层的实现原理是把字符串转换成ASCII比较的，
            但是如果用一个字符和它对应的ASCII值比较也是不相等的

"""