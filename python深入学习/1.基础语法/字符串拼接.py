# 字符串拼接
string1 = 'Good morning,sir,'
string2 = 'this is your breakfast'
total_string = string1 + string2
print(total_string)

string1 = input('please enter your name：')
string2 = input('please enter your age：')
total_string = 'hello，' + string1 + ',your age is ' + str(string2)
print(total_string)

# 字符串大小写
# upper:大小全部字母
# lower：小写全部字母
# title：大写首字母
string = "hello"
string1 = 'HELLO'
string2 = 'monday'
string = string.upper()
string1 = string1.lower()
string2 = string2.title()
print(string)
print(string1)
print(string2)
