"""
语法：
    [最终迭代变量 for 第一层迭代变量 in 第一个迭代对象 …… for 最终迭代变量 in 上一层迭代对象]

如果带条件是先把所有的元素遍历出来，然后再做判断，最后做运算
"""
#列表推导式实现，遍历列表
lst = [[1,2,3],['hello','world'],[7,8,9]]
spam = [i for x in lst for i in x]
print(spam)
print('-'*50)

#for循环实现
spam1 = []
for i in lst:
    for k in i:
        spam1.append(k)
print(spam1)
print('-'*50)

#带判断的多层推导式
spam2 = [i*i for x in lst for i in x if type(i) == int]
print(spam2)
print('-'*50)

#for循环实现
spam3 = []
for i in lst:
    for k in i:
        if type(k) == int:
            spam3.append(k*k) 
print(spam3)            