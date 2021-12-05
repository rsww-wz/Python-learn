# 方法1：使用%
# 格式：字符串里面使用格式化字符串符号，字符串外面使用%+变量，如果有多个变量需要用括号
name = input('please enter your name:')
hello = 'hello,%s' % name
hello1 = 'hello,%s,you are %d years old!' % (name, 20)

print(hello)
print(hello1)

# 使用format函数
# 格式1：直接花括号
# 格式2:花括号里面加数字，注意只能从0开始
# 格式3：花括号里面指定标识符，参数使用这个标识符指定参数
string = 'hello,{},you are {} years old'.format(name, 21)
string1 = 'hello,{0},you are {1} years old'.format(name, 18)
string2 = 'hello,{n},Good {m}'.format(n=name, m='morning')
print(string)
print(string1)
print(string2)

# 使用最新语法
# 格式：f关键字，字符串里面的花括号直接填变量
string3 = f'hello,{name},Good {"morning"}'
print(string3)
