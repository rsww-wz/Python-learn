"""
    布尔操作符：and，or，not
    布尔操作符是对布尔值再次进行布尔运算，所以返回值也是一个布尔值
    and：两个布尔值都是True，返回值才是True(有错就错)
    or：两个布尔值有一个True，返回值就是True；两个都是False，才返回False（有对就对）
    not：真变假；假变真
"""

a = True and True
b = True and False
c = False and True 
d = False and False

e = True or True
f = True or False
g = False or True 
h = False or False

i = not True
j = not False

print(a)
print(b)
print(c)
print(d)
print('\n')

print(e)
print(f)
print(g)
print(h)
print('\n')

print(i)
print(j)

"""
    布尔操作符的优先级
        not>and>or
    布尔复合运算
        可以把and和or两边的True或者False怎么的来的表达式带入到表达式中运算
        布尔复合运算的优先级很重要，也很容易发生错误，尽量使用括号，避免歧义
    如何看复合运算的优先级
        先找到优先级最高的
        再看是否有同级运算，如果有同级运算从左往右运算
        把优先级高的运算完再算优先级低的
"""

spam = 4 > 5 and 2 < 5                #(4 > 5) and (2 < 5)
spam1 = 3 == 2 and 3 < 9 or 4 > 2     #(3 == 2 and 3 < 9 )or (4 > 2)
spam2 = 3 != 3 or 34 > 25 and 9 < 3 and 3 >= 3   
    # (3 != 3) or ((34 > 25 and 9 < 3) and 3 >= 3)
           
print(spam)
print(spam1)
print(spam2)
