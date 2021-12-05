a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}
c = {5, 6, 7, 8, 9}

# 交集运算
spam = a & b
spam1 = b & c
spam2 = a & c
spam3 = a & b & c

print(spam)
print(spam1)
print(spam2)
print(spam3)

# 并集运算
spam4 = a | b
spam5 = b | c
spam6 = a | c
spam7 = a | b | c

print(spam4)
print(spam5)
print(spam6)
print(spam7)

# 对称运算：两个集合做并集运算，然后去掉他们的交集成分——运算符^
spam8 = a ^ b
spam9 = b ^ c
spam10 = a ^ c
spam11 = a ^ b ^ c

print(spam8)
print(spam9)
print(spam10)
print(spam11)

"""
差值运算
    运算符：-
    运算逻辑
        与运算的集合顺序有关，结果是在第一个集合中去掉两个集合的交集部分
        1.先求两个集合的交集
        2.用第一个集合减去交集部分，剩下的元素就是结果
        3.如果两个集合没有交集，结果就是第一个集合的全部元素
"""
temp = a - b
temp1 = b - a
temp2 = b - c
temp3 = c - b
temp4 = a - c
temp5 = c - a

print(temp)
print(temp1)
print(temp2)
print(temp3)
print(temp4)
print(temp5)

"""
比较运算
    比较运算返回布尔值
    ==:如果两个集合的元素相同返回True
        只有两个集合相互包含对方的全部元素即可，是否有重复元素不重要
    其他比较运算不太常用
"""

d = {1, 2, 3, 4}
e = {1, 2, 3, 4, 5}
f = {7, 8, 9}
g = {1, 1, 2, 2, 3, 4}

temp6 = d == e
temp7 = d < e
temp8 = d <= e
temp9 = f > d
temp10 = f < d
temp11 = d == g

print(temp6)
print(temp7)
print(temp8)
print(temp9)
print(temp10)
print(temp11)
