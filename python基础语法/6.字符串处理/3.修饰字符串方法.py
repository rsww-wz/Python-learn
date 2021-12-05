"""
字符串列表连接与分割
    join()方法
        适用范围：一个列表的全部元素都是字符串
        作用：成为一个单独的字符串
        参数：字符串列表
        返回值：连成串的字符串
        注意：join()方法必须在字符串上调用

    split()方法
        作用：把一个字符串分割成一个列表
        参数：分割的字符串，可以是任意的字符串，通常是转移字符居多,默认是空格
        返回值：列表
        注意：是针对字符串调用的，也就是必须是字符串调用这个方法
"""

string = ''
spam = ['Monday', 'Tuesday', 'Wednesday', 'Truesday', 'Firday', 'Saturday', 'Sunday']
string = string.join(spam)
print(string)

string1 = 'Monday,Tuesday,Wednesday,Truesday,Firday,Saturday,Sunday'
spam1 = string1.split(',')
print(spam1)

"""
文本对齐方法
    rjust(),ljust():
        这两个方法分别是右对齐和左对齐
        参数：
            第一个参数：整数长度
            第二个参数：指定一个填充字符 
    center():
        作用：让文本居中

删除空白符
    strip():删除字符串两边的空白符
    rstrip():删除字符串右边的空白符
    lstrip():删除字符串左边的空白符

    strip()方法有一个可选参数：
        作用：指定两边的那些字符应该删除
        参数：两边要删除的字符
        字符的顺序不重要，可以随便排，只要是参数字符的组合即可
"""
string2 = 'hello'
string3 = 'world'
string4 = 'Good morning'

temp = string2.rjust(20, '*')  # 右对齐
temp1 = string3.ljust(20, '*')  # 默认是左对齐
temp2 = string4.center(20, '=')  # 必须超过字符串本身的长度，剩下的长度才能用来居中

print(temp)
print(temp1)
print(temp2)

string5 = '   hello world'
string6 = 'Good morning     '
string7 = '       你好      '
string8 = 'ishello worldsi'

temp3 = string5.lstrip()
temp4 = string6.rstrip()
temp5 = string7.strip()
temp6 = string8.strip('is')  # 指定两边要删除的字符

print(temp3)
print(temp4)
print(temp5)
print(temp6)
