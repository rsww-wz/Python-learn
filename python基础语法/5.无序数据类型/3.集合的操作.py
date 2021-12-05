a = {1,2,4}

"""
增
    add()方法
        作用：添加元素进集合里面
        当场修改集合

删
    remove()方法
        作用：删除集合中的指定元素
        也是当场修改集合
        如果删除的是集合中不存在的值会报错

"""
print(id(a))
a.add(10)
print(a)
print(id(a))

a.remove(2)
print(a)
print(id(a))
print('\n')


"""
len()函数：计算集合不重复元素个数
max()函数：找出集合最大值
min()函数：找出集合最小值
sum()函数：计算集合的和
set()函数：把其他类型转换为集合
    不同类型的列表，元组也能转化为集合
    但是，如果是嵌套的列表也是不能转化的,相同的数据类型也不行
"""

print(len(b))
print(max(b))
print(min(b))
print(sum(b))

temp = [1,2,2,3,4,6]
temp1 = (3,2,6,2,8,10)
temp2 = "hello world"
temp3 = [1,'hello']

print(set(temp))
print(set(temp1))
print(set(temp2))
print(set(temp3))

