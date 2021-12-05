"""
sort()方法
    作用：将列表或者字符串排序
    参数：
        reverse：True，可以让sort()方法按逆序排序
    sort()方法是当场对列表排序

    不能对既有数字，又有字符串的列表排序
    如果是对字符串排序，是按ASCII排序
    大写字母排在小写字母前面
    可以加关键字参数：key = str.lower
        全部把字母当成小写字母，但是列表中的值并不会改变
"""

a = [1,2,3,4,5,6,7,8,9]
a.sort()
print(a)
a.sort(reverse = True)
print(a)

string = 'Hello World'
string = list(string)
string.sort()
print(string)
string.sort(reverse = True)
print(string)

string.sort(reverse = True,key = str.lower)
print(string)

"""
pop()方法
    作用：把指定位置的元素删除掉，然后返回出来
    参数：位置参数
    返回值：后面的元素
"""
b = [1,2,3,4,5,6,7,8,9]
spam = b.pop(5)
print(b)
print(spam)
