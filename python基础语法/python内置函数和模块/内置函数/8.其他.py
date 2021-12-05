# any() :or 连接所有元素
# all() :and 连接所有元素

lst = [1,0,True]
print(any(lst))
print(all(lst))


#zip函数
lst1 = [1,3,5]
lst2 = [2,4,6]

spam = zip(lst1,lst2)
print(spam)
print(type(spam))
print("__iter__" in dir(spam))
for item in spam:
    print(item)
print('\n')


#有木桶效应，以最短的那个列表为准
lst1 = [1,2,3,4]
lst2 = [6,7,8,9,5]
spam = zip(lst1,lst2)
for item in spam:
    print(item)

# 作用：可以组建成字典
lst1 = ["A","B","C","D"]
lst2= [1,2,3,4]
spam = dict(zip(lst1,lst2))
print(spam)
print('\n')

# 元组创建字典
tup1 = ("A","B","C","D")
tup2 = (1,2,3,4)
spam1 = dict(zip(tup1,tup2))
print(type(spam1))
print(spam1)

# 字符串创建字典
str1 = "hello"
str2 = "world"
spam2 = dict(zip(str1,str2))
print(type(spam2))
print(spam2)

# encode("编码格式")
# decode("编码格式")
# 不同的编码格式不能直接转化，必须通过字符串过渡两种编码格式

string = "你好"
spam= string.encode("gbk")
print(spam)
spam1 = string.encode("utf-8")
print(spam1)
code = b'\xc4\xe3\xba\xc3'
string = code.decode("gbk")
print(string)
code1 = b'\xe4\xbd\xa0\xe5\xa5\xbd'
string1 = code1.decode("utf-8")
print(string1)