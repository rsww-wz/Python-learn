"""
数量词
    符号：花括号
    匹配规则
        组和字符集等，一个表达式只能匹配一个字符
        使用数量词可以匹配指定次数，相当于把组和字符集的表达式复制了几次
        是对花括号前面的那个表达式复制几次，不是对整个表达式复制几次
        所以前面一般是组，表示把组匹配多少次(重复分组多少次)

    数量词的范围
        如果匹配的内容长度不确定，数量词也是可以用范围表示的，数之间用逗号隔开
        一个数最小匹配次数和另外一个最大匹配次数
        也可以不写第一个或者第二个数字，即不限定最小值或者最大值

贪婪与非贪婪
    符号：问号，？
    匹配规则：当符合匹配规则的时候，会尽可能多的匹配字符

    当数量词范围是不确定的时候，默认是贪婪模式

    非贪婪模式：满足匹配要求就会不继续匹配下去
"""
import re
 
string = r"34h6ld3k5d956 \j9f5h9a \dss02fhing2kd \w3h46"

spam = re.findall('\d{1,4}',string)
spam1 = re.findall('\d[a-z]\d',string)

spam2 = re.findall('\d[a-z]{2,4}',string)      
     #\d[a-z][a-z]或\d[a-z][a-z][a-z]或\d[a-z][a-z][a-z][a-z]
spam3 = re.findall('(\d[a-z]){2,4}',string)    
     #(\d[a-z])或(\d[a-z])(\d[a-z])或(\d[a-z])(\d[a-z])(\d[a-z])

spam4 = re.findall('([0-9][a-z][0-9][a-z])',string)   
spam5 = re.findall('([0-9][a-z][0-9][a-z][0-9][a-z])',string)   

print(spam)
print(spam1)
print(spam2)
print(spam3)
print(spam4)
print(spam5)

string1 =  "your nakedness and pass out of love’s threshing-floor, into the"

temp = re.findall('[a-z]{3,9}',string1)           #贪婪模式
temp1 = re.findall('[a-z]{3,9}?',string1)         #非贪婪模式

print(temp)
print(temp1)

"""
其他数量词
    * (星号):表示匹配0次或者无限多次（"字符串*"）
    + (加号):表示匹配1次或者无限多次
    ？(问号):表示匹配0次或者1次（去重复操作）

    . (英文句号)-不是数量词：匹配1次除了换行符之外的所有符号

    注意
        数量词都默认是贪婪模式
        数量词问号和贪婪模式的问号
        如果看见有两个问号在一起时，第一个问号表示数量词，第二个问号表示非贪婪模式
        所以??--表示不使用数量词

    这些数量词都表示匹配次数，就算是用了非贪婪模式匹配0次
        也只是相当于没有了数量词，原本的表达式还是可以匹配字符的
"""

string2 = 'hello world'

temp2 = re.findall('\w*',string2)
temp3 = re.findall('\w*?',string2)       #不使用数量词

temp4 = re.findall('\w+',string2)
temp5 = re.findall('\w+?',string2)       #使用数量词一次

temp6 = re.findall('\w?',string2)
temp7 = re.findall('\w??',string2)       #不使用数量词

temp8 = re.findall('\w.',string2)        #匹配两个字符
temp9 = re.findall('\w.?',string2)       #匹配两个字符的非贪婪模式

print(temp2)
print(temp3)
print(temp4)
print(temp5)
print(temp6)
print(temp7)
print(temp8)
print(temp9)

