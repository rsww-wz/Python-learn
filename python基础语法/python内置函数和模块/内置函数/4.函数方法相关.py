# callable()
#   查看方法或者函数是否能被调用，返回一个布尔值
#   判断一个方法或者函数是否能被调用，看后面是否能加括号
#   作用：判断能否被调用

# help()
#     查看方法或者函数的使用
#     还可以查看库的使用
#     命令行命令里面用的多

import re

def func():
    pass

print(callable(func))

print(help(int))
print(help(re)) 