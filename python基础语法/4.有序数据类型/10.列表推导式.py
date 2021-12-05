"""
语法格式
    [(推导式)变量 for (临时)变量 in 可迭代对象]
    如：[x for x in range(0,10)]  -- [x / for x in range(0,10)]
    可以在列表中放入任何对象，返回值是一个新的列表
    列表的最终结果就是推导式变量

包含判断和筛选的列表推导式
    [(推导式)变量 for (临时)变量 in 可迭代对象 if 判断式]

列表推导式执行顺序：
    从左到右依次递进
    语句之间是嵌套的关系
"""

# 生成普通列表
temp = []
for i in range(0, 10):
    temp.append(i)

temp1 = [i for i in range(0, 10)]

# 生成带运算的列表
temp2 = []
for i in range(0, 10):
    temp2.append(i ** 2)

temp3 = [i ** 2 for i in range(0, 10)]

# 生成带判断的列表
temp4 = []
for i in range(0, 10):
    if i % 2 == 0:
        temp4.append(i)

temp5 = [x for x in range(0, 10) if x % 2 == 0]

# 生成带判断和运算的列表
temp6 = []
for i in range(0, 10):
    if i % 2 == 0:
        temp6.append(i ** 3)

temp7 = [x ** 3 for x in range(0, 10) if x % 2 == 0]
"""
x**3 -- (定义最终元素的表达式) 
for x in range(0,10) -- (初步定义的列表) 
if x % 2 == 0 -- (对初步列表的过滤)
"""

print(temp)
print(temp1)
print(temp2)
print(temp3)
print(temp4)
print(temp5)
print(temp6)
print(temp7)

# 生成带多层嵌套判断的列表
spam = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
spam1 = []
for i in spam:
    for x in i:
        if x % 2 == 0:
            spam1.append(x)

spam2 = [x for y in spam for x in y if x % 2 == 0]

print(spam1)
print(spam2)

"""
什么时候可以用列表推导式
    生成列表
    对已有列表的过滤
    对已有列表的计算
    对已有列表的过滤和计算

如何读懂列表推导式
    开头表达式：定义最终元素的表达式，应该最后看
    中间的部分：初步定义的列表，应该看始看
    末尾部分：对初步列表的过滤，看完中间部分看

    从中间往后看，看嵌套多少个for循环，再看过滤了什么元素，把最后得到元素代入表达式
"""
