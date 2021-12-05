"""
    range()函数：
    作用：用于for循环中，产生序列用于固定次数的循环
    参数：所有参数必须是整型
        第一个参数：起始数字；
        第二个参数：表示上限，但不包含它本身；
        第三个参数（可以没有）：表示步长,默认步长是1
    返回值：
        不是列表,如果需要得到列表的结果需要转换成list类型

    官方说明：
    Return an object that produces a sequence of integers
    from start (inclusive) to stop (exclusive) by step. 
    range(i, j) produces i, i+1, i+2, ..., j-1.
    start defaults to 0, and stop is omitted! 
    range(4) produces 0, 1, 2, 3.
    These are exactly the valid indices for a list of 4 elements.
    When step is given, it specifies the increment (or decrement).

"""

spam = range(0, 10)
print(type(spam))
spam1 = list(spam)
print(spam1)

print(list(range(0, 10, 2)))

for i in range(0, 10, 2):
    print('hello', end=',')

for i in 'hello world':
    print(i, end='')

"""
    for循环格式：
        for 循环变量 in 字符串|列表|元组|字典|集合：
            pass
        else:
            pass

    else语句可以没有，而且最好也不要写
    其他语言都没有这个else语句，用了而可能会降低程序的可以阅读性

    for循环理解：
        循环次数：字符串|列表|元组|字典|集合等数据类型包含的元素个数
        循环变量：循环变量的值就等于该循环次数在以上数据类型中的值
            理解：循环变量 = 字符串|列表|元组|字典|集合[循环次数]
        for循环可以很方便的得到这些数据类型的个数和元素
        所以遍历这些数据类型通常都是用for循环
"""

i = 5
while i > 0:
    print(i, end=' ')
    i = i - 1

string = "hello world"
length = len(string)
k = 0
while k < length:
    print(string[k], end='')
    k = k + 1

"""
    while循环格式：
        while 布尔表达式：
            pass(布尔表达式为True)
        else:
            pass(布尔表达式为False)

    while循环理解
        while循环每次都会检查是否符合条件在执行程序  
        while循环多用于不知道次数的循环，
        如果while遍历list，str等没有for循环方便
        while循环中的else语句比for循环的else语句更自然
        布尔表达式很灵活，使while循环也很灵活

    注意：python没有do-while循环
"""
