#身份运算符
a = [0,1,2]
b = a
c = a[:]

spam = a is b
spam1 = a is c

print(spam)
print(spam1)

if a is b:
    print('same')
else:
    print('different')

if a is c:
    print('same')
else:
    print('different')

if a == c:
    print('same')
else:
    print('different')

"""
身份运算符:is ,not is
    作用：判断两个变量的地址是否一样
    返回值：
        如果地址一样，返回True
        如果地址不一样，返回False

    和==(等于)的区别
        ==：是判断两个变量的值是否一样，一样就返回True
        is：是判断两个变量的地址是否一样，一样就返回True

        is是比==更严格的判断
"""

#成员运算符
d = [1,3,5,7,9]
e = 'hello world'

temper = 1 in d
temper1 = 2 in d
temper2 = 'a' in e
temper3 = 'l' in e

print(temper)
print(temper1)
print(temper2)
print(temper3)

"""
成员运算符:in ,not in
    作用：判断一个元素是否在一个组里面（字符串，列表，元组，集合，字典等）
    返回值：
        如果在，返回True
        如果不在，返回False
"""