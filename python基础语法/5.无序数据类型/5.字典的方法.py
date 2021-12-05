"""
遍历
    keys()方法：返回字典的key
    values()方法：返回字典的value
    items()方法：返回字典的key-value

    直接用字典遍历，得到的是字典的key

这些方法返回的不是列表，不能被修改，不能用append方法
但是可以类型转换，可以转换成list
"""

spam = {'XL':175,'L':170,'M':165,'S':160}
for i in spam.keys():
    print(i)

for i in spam.values():
    print(i)

for i in spam.items():
    print(i)

for i,k in spam.items():
    print('key: ' + str(i) + ' value: ' + str(k))
print('\n')

print(list(spam.keys()))
print(list(spam.values()))
print(list(spam.items()))

"""
查
检查键或值
    检查key：可以用下标索引
    检查value：可以用is

    还可以用上面的keys()方法和value()方法配合身份运算符使用
    但是这些方法都有一个缺点，就是如果key或者value不存在，就会报错

    get()方法：
        作用：返回要访问的值
        参数
            第一个参数：要取得值的键
            第二个参数：如果键不存在时的备用值
        返回值  
            如果键存在，返回对应的值
            如果键不存在，返回备用值，但是该键值对并没有被添加进字典
"""

temp = 'L' in spam
temp1 = 'M' in spam.keys()
temp2 = 165 in spam.values()
print(temp)
print(temp1)
print(temp2)

temp3 = spam.get('M')
temp4 = spam.get('XXL',180)
temp5 = spam.get('XL',178)
print(temp3)
print(temp4)
print(temp5)
print(spam)

"""
增
setdefault()方法：
    作用：为字典的键设置一个默认值，当键不存在时，使用默认值，确保一个键的存在
    参数：
        第一个参数：要检查的键
        第二个参数：如果键不存在时要设置的值
    返回值：
        如果键存在，则忽略掉这个参数，并且返回原来键的值
        如果键不存在，这两个参数就是字典的键值对（添加键值对）
    形式：
        temp = setdefault(key,备用value)
"""

week = {1:'monday',2:'tuesday',3:'wednesday',
4:'truesday',5:'firday',6:'saturday'}

temp6 = week.setdefault(6,'sunday')       #key存在，返回原来的value
temp7 = week.setdefault(7,'sunday')       #key不存在，添加备用value进字典
print(temp6)
print(temp7)
print(week)

#其他函数
print(len(week))     #字典元素个数
print(max(week))     #字典最大key
print(min(week))     #字典最小key