"""
推导表达式
    对每个元素做相同的运算
    这个表达式的结果就是最终的元素的结果
    这是个表达式，不能有赋值号，否则就是语句了

    这个表达式还可以是三元运算符
    [表达式1 if 条件 else 表达式2 for 迭代变量 in 迭代对象]
"""

lst = [1,2,3,4,5,6,6,7,8,9]

#用列表推导式实现
spam = [i**2 for i in lst]
print(spam)
print('-'*50)

#用for循环实现
spam1 = []
for i in lst:
    spam1.append(i**2)
print(spam1)

#三元运算符
spam2 = [i if i%2==0 else i**2 for i in lst]
print(spam2)
print('-'*50)   

#for循环实现
spam3 = []
for i in lst:
    if i % 2 == 0:
        spam3.append(i)
    else:
        spam3.append(i**2)

print(spam3)