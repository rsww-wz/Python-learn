"""
组
    正则表达式符号：小括号
    匹配规则：把要匹配的字符串用小括号括起来即可
    小括号里面是且的关系
    组里面的才是匹配到的内容，组外面的不会被匹配

    组的使用一般要配合其他正则表达式一起使用

    总结：就是要匹配的内容必须跟小括号里面的字符串一样，才能匹配上

    组的常用做法就是把表达式作为一个整体，然后用数量词重复
"""
import re

string = 'hello,my name is js,i like learning,because it can make me spirit'

spam = re.findall('(is)',string)
print(spam)