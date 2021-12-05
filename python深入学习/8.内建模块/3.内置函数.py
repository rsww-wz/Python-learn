"""
1. abs()
    浮点数和整数都可以
    返回绝对值

2. all()
    将可迭代对象都做布尔运算，全为True返回True，如果有一个是False就返回False
    即：如果可迭代对象中，有一个是空值，就返回False；如果都都不是空值就返回True
    如果可迭代对象是空(Null)也返回True

3. any()
    如果可迭代对象中，有任意一个空值就返回True，如果都不是空值就返回False
    如果可迭代对象是空(Null)也返回False

4. callable()
    判断某个对象是否可调用，能加括号的都是可以调用的
    可调用对象：函数，方法，类，对象

5. chr()
    查看数字对应的ASCII
    拓展：ord():查看ASCII对应的数字

6. dir()
    查看对象有哪些属性

7. divmod()
    返回除法的商和余数

8. enumerate()
    一般用在for循环中，以元组的方式返回索引和值

9. eval
    运行字符串中的表达式

10. frozenset()
    可不变集合

11. hash(可不变类型)
    得到一个hash值,但是每次程序运行的得到值都是不一样的

12. help()
    查看文档

13. isinstance(对象，类)
    判断一个对象是否是一个类的实例
    可以做类型判断(可以取代type函数)

14. zip()
    返回的是一个迭代器
    一一对应

15. __import__()
    导入类名为字符串的类
    import 后面不能接字符串类型
"""

# abs
x = -1.1
print(abs(x))

# all
lst1 = []
lst2 = ['hello']
lst3 = ['', 'world']
print(all(lst1))
print(all(lst2))
print(all(lst3))

# any
print(any(lst1))
print(any(lst2))
print(any(lst3))

# chr
print(chr(65))
print(ord('a'))

# enumerate
lst = ['a', 'b', 'c', 'd']
for i in enumerate(lst):
    print(i)

# eval
string = '{"a":1,"b":5}'
dic = eval(string)
print(dic)

# frozenset
set1 = {44, 267, 167, 1}
set2 = frozenset({44, 267, 167, 1})
print(set1)
print(set2)

# hash
print(hash(46))
print(hash('hello'))

print(help(hash))


# isinstance
class Foo:
    pass


obj = Foo()
print(isinstance(obj, Foo))

# isinstance可以类型判断
span = 'hello'
print(isinstance(span, list))

# __import__
t = __import__('time')
print(t.time())
