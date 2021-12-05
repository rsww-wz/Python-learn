"""
字符串是不可以修改的，所以所有的字符串方法都是返回一个新的字符串
如果要改字符串，可以用修改后的字符串覆盖原来的字符串，可以达到修改字符串的效果
大小写方法
    upper()：全部大写，非字母不变
    lower()：全部小写，非字母不变
    isupper()：至少有一个字母，并且所有字母都是大写，返回True
    islower()：至少有一个字母，并且所有字母都是小写，返回True
"""

spam = 'hello'
spam1 = 'WORLD'
spam = spam.upper()
spam1 = spam.lower()
print(spam)
print(spam1)

temp = spam.isupper()
temp1 = spam1.islower()
print(temp)
print(temp1)

#连续调用方法
spam = spam.lower().islower()
spam1 = spam1.upper().isupper()
print(spam)
print(spam1)
print('\n')

"""
以is开头的字符串方法(isX)都是返回布尔值的
    isalpha():只包含字母，返回True
    isalnum():只包含数字和字母，返回True
    isdecimal():只包含数字，返回True
    isspace():只包含空格，制表符，换行符等不可见字符，返回True
    istitle():值包含大写字母开头，后面都是小写字母的单词，返回True

    验证用户输入时，isX字符串方法是有用的

startwith()和endwith()方法
    starwith():调用这个方法的字符串与该方法的参数字符串开始，返回True
    endwith():调用这个方法的字符串与该方法的参数字符串结束，返回True
"""

string = 'hello'
string1 = 'my tellphone number is 15113657172'  #有空格
string2 = '15113657172'
string3 = '   '
string4 = 'Monday,Tuesday,Wednesday,Truesday,Firday,Saturday,Sunday'

temper = string.isalpha()
temper1 = string1.isalnum()
temper2 = string2.isdecimal()
temper3 = string3.isspace()
temper4 = string4.istitle()

temper5 = string1.startswith('my')
temper6 = string4.endswith('Sunday')

print(temper)
print(temper1)
print(temper2)
print(temper3)
print(temper4)
print('\n')

print(temper5)
print(temper6)
