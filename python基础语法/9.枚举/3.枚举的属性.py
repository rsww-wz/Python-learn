"""
枚举是不可变的，不可修改的

枚举的继承
    如果枚举继承的是Enum，枚举的值可以是数值，也可以是字符串
    但是如果枚举继承的是IntEnum，枚举的值必须是数值
        from enum import IntEnum
        类名(IntEnum):

"""
from enum import Enum

from enum import IntEnum


class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4


# 枚举不可修改
# VIP.YELLOW = 5

# 枚举的继承
class VIP1(IntEnum):
    #    YELLOW = 'a'           #IntEnum枚举的值只能是数值，不能是字符串
    GREEN = 2
    BLACK = 3
    RED = 4
