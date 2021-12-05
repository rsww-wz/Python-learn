# 列表的切片
animals = ['cat', 'dog', 'pig', 'bat', 'rat', 'elephant']
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
temper = animals

spam = animals[0:3]
spam1 = animals[2:-1]
spam2 = animals[-2:-1]
spam3 = animals[0:]
spam4 = animals[:]
spam5 = number[1:-1:2]
spam6 = number[::2]
spam7 = number[len(number)::-2]
spam8 = number[::-2]

print(spam)
print(spam1)
print(spam2)
print(spam3)
print(spam4)
print(spam5)
print(spam6)
print(spam7)
print(spam8)
print('\n')

print(id(animals))
print(id(spam3))
print(id(spam4))

if animals is temper:
    print('they are same')
else:
    print('they are different')

if spam3 is spam4:
    print('they are same')
else:
    print('they are different')

"""
列表的切片
    切片的符号：来个下标之间用冒号隔开
    切片：都是在数的前面切
    如：
        0：就在下标是0的元素的前面切
        -1：-1是最后一个元素，就在最后一个元素的前面切(所以不包含最后一个元素)
    如何切整个列表：
        第一个下标写0，最后一个下标空白即可
        或者两个下标都空白也是可以的

    列表切片的第三个参数:
        第三个参数表示步长
        表示在前两个参数得到的列表，每个多少个取出一个元素
        步长可以是负数，表示从后面往前提取元素
        但是此时，前面的两个参数下标必须从大到小

列表的复制
    如果直接把一个列表赋值给另外一个变量，那么这个变量就会得到列表的值
        但是这不是复制列表，他们的地址是一样的，也就是说他们是一个东西
        只是有两个名字而已，如果修改其中一个，另外一个也会改变的

    如果要复制列表，可以用切片的方法
        用切片的方法得到的列表和原列表是两个列表，他们之间没有任何关系
        他们的地址是不一样的，修改其中的任何一个，另外一个也不会改变
        如果对一个列表切两次相同的元素，他们之间也是相互独立
"""
