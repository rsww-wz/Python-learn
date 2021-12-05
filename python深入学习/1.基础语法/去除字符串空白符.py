string = 'python'
string1 = 'python '

# 去除左右空白字符
string = string.strip()
string1 = string1.strip()

if string == string1:
    print('they are same')
else:
    print('they are different')

# 单独去除左右空白,默认去除空格
string = ' hello world '
str1 = string.strip()
str2 = string.lstrip()
str2 = str2.rstrip()

if str1 == str2:
    print('they are same')
else:
    print('they are different')

# 去除指定字符
str2 = '++hello world++'
str2 = str2.strip('+')
print(str2)

str3 = '--hello world++'
str3 = str3.lstrip('-')
str3 = str3.rstrip('+')
print(str3)
