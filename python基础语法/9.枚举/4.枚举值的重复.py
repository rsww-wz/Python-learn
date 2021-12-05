"""
枚举值的重复
    枚举类中，同一个标签不能有两个值，但是一个值可以有两个标签
    相同值的第二个标签是第一个标签的别名，实际上他们是通一个枚举类型
    遍历的时候，得到是大名的那个枚举类型

    遍历的时候使用__members__方法可以得到所有枚举标签(包括小名标签)

枚举的装饰器
    作用：如果不想出现重复枚举值，可以使用装饰器，出现重复值的时候会报错
    @unique
    表示枚举的标签和枚举的值必须一一对应
    即不能有一个值对应两个标签的情况

"""

from enum import Enum


class VIP(Enum):
    YELLOW = 1  # 大名
    YELLOW_A = 1  # 小名（别名）
    GREEN = 2
    BLACK = 3
    RED = 4


print(VIP.YELLOW_A)  # 实际上是大名

for i in VIP.__members__:
    print(i)


@unique
class VIP1(Enum):
    YELLOW = 1  # 大名
    #  YELLOW_A = 1              #小名（别名）
    GREEN = 2
    BLACK = 3
    RED = 4
