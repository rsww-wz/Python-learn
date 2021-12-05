spam = True
spam1 = False
print(spam)
print(spam1)
print(type(spam))
print(int(spam))
print(int(spam1))

"""
    布尔值：只有两个，True和False，而且首字母必须大写
    True的值是1，False的值是0

    不同类型的值的布尔值
        不为零的数字的布尔值：True
        零的数字的布尔值：False
        空字符串的布尔值：False
        其他字符串的布尔值：True
        空列表，空元组和空集合的布尔值：False

        总结：空的数据的布尔值是False，其他都是True
"""
a = 1
b = 0
c = ''
d = ' '
e = 'd'
f = []
g = {}


print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(e))
print(bool(f))
print(bool(g))