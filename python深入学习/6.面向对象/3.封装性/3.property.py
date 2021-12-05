"""
装饰器
    装饰器是在不修改被装饰对象以及调用方式的情况下，为被装饰对象添加上新功能的可调用对象

可调用对象
    函数
    类

propert
    是一个装饰器，这个装饰器的名字就是property
    它是用类实现的，不需要理解如何实现的，因为比较复杂

"""

# 案例
class PeoPle:

    def __init__(self,name,weight,height):
        self.name = name
        self.weight = weight
        self.height = height

    """
    定义函数的原因
    从bmi应用是触发功能计算得到的
    bmi是随着身高，体重变化而动态变化的，不是一个固定的值

    但是，这个bmi听起来更想是一个数据，而非功能，与实际逻辑不符
    所以应该将这个功能伪装称为一个属性
    
    而property装饰器就可以实现这种伪装
    在调用的时候不需要加括号
    这也是一种封装思想的体现
    
    总结
        property的效果就是把函数伪装成变量
        在调用的时候少了一对括号
        注意：如果加了括号就会报错
    
    """

    @property
    def bmi(self):
        return self.weight / (self.height ** 2)

obj = PeoPle('rs',50,1.65)
print(obj.bmi)
obj.weight = 55
print(obj.bmi)

