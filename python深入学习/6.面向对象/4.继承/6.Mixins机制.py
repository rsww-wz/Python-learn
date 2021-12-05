"""
1. Mixmins机制解决的问题
    尽可能在多继承的背景下，提升多继承的可读性
    让多继承满足人的思维习惯"什么是什么"

2. Mixins机制
    通过在父类名后加Mixins，一般以Mixins，ible，able结尾
    这不是语法，只是一种规范，就像大家都用self,而不是其他
    表示这个类不是真正的父类，只是为了加入一个共同的功能，解决代码冗余问题的一种手段

3. Mixins机制的使用场合
    首先它必须表示某一一种功能，而不是某个物品
    其次它必须责任单一，如果有多个功能，就写多个Mixins类，一个类可以继承多个Mixins
    然后它不依赖与子类实现
    最后子类即便没有继承这个Mixins类，也照样可以工作，就是缺少某个功能

"""

# 实例1
# 交通工具
# class Vehicle:
#     pass
#
#     """
#     子类有重复的部分，但是不能把他们抽取出来，放在共同的父类，因为汽车类不会飞
#     所以会造成代码冗余问题
#     所以解决办法是在创建一个类，用多继承的方式实现继承功能的属性
#     """
#
#
# # 民航飞机
# class CiviAircraft(Vehicle):
#     def fly(self):
#         pass
#
# # 直升飞机
# class Helicopter(Vehicle):
#     def fly(self):
#         pass
#
# # 汽车
# class Car(Vehicle):
#     pass


# 实例2
# 交通工具
class Vehicle:
    pass

# 通过在类名后加上Mixins，表示这不是一个真正的父类，只是作为解决代码冗余的一个父类
class FlyableMixins():
    def fly(self):
        pass

# 民航飞机
class CiviAircraft(FlyableMixins,Vehicle):
    pass

# 直升飞机
class Helicopter(FlyableMixins,Vehicle):
    def fly(self):
        pass

# 汽车
class Car(Vehicle):
    pass