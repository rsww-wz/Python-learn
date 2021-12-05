"""
枚举类遍历
    可以用for循环遍历枚举类
    返回的是枚举类型

枚举类型的比较
    枚举类型可以做等值比较，但是不能做大小比较
    枚举类型可以和数值做等值比较，但是不会返回True
    不同枚举类可以等值比较，但是永远都是返回False

    身份比较也是可以的

枚举的类型转换
    枚举类(枚举的值)
    把变量的值对应枚举类的枚举类型
    实际上并不是真正的类型转换
    主要还是改善可读性
"""

from enum import Enum

class VIP(Enum):             

    YELLOW = 1             
    GREEN = 2
    BLACK = 3
    RED = 4

class VIP1(Enum):             

    YELLOW = 1             
    GREEN = 2
    BLACK = 3
    RED = 4

#遍历
for i in VIP:
    print(i)


#比较
spam = VIP.YELLOW == VIP.YELLOW             #等值比较
spam1 = VIP.YELLOW is VIP.YELLOW            #身份比较
spam2 = VIP.YELLOW == VIP1.YELLOW           #不同枚举类的等值比较
spam3 = VIP.YELLOW is VIP1.YELLOW           #不同枚举类的身份比较

print(spam)
print(spam1)
print(spam2)
print(spam3)

#类型转换
a = 1
b = 2
print(VIP(a))
print(id(a))                     #地址是不一样的
print(id(VIP(a)))                #不同枚举类的相同值的地址也是不一样的
print(id(VIP1(b)))
