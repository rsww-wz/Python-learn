"""
类似枚举功能的实现
    用字典来实现枚举的缺点
        可变
        没有防止相同标签的功能
    用枚举类

概述
    枚举的意思就是给数字或其他数据起名字

    枚举也是一个类，python中的一切都是类的对象
    用类的类变量来做枚举变量，但是枚举类不能实例化


基本概念
    枚举的标签：给枚举起的名字
    枚举的值：枚举的数值
    枚举类型：枚举的标签和值

语法
    从enum导入Enum，然后继承Enum
    枚举类(Enum):
    标签 = 值
    标签要大写(python中用大写表示常量，但实际上还是变量)


访问枚举类
    访问枚举类型：枚举类.标签
    访问枚举的标签：枚举类.标签.name
    访问枚举的值：枚举类.标签.value

    可以用索引的方法访问枚举类型：类名['标签名']

"""

from enum import Enum

class VIP(Enum):             #枚举类

    YELLOW = 1              #标签 = 值
    GREEN = 2
    BLACK = 3
    RED = 4

print(VIP.YELLOW)                #枚举类型
print(type(VIP.YELLOW))

print(VIP.GREEN.value)           #枚举的值
print(type(VIP.GREEN.value))

print(VIP.BLACK.name)            #枚举的名字(标签)
print(type(VIP.BLACK.name))

print(VIP['RED'])                #索引访问