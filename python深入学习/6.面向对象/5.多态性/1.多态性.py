"""
1. 什么是多态
    多态指定的是同一种事物多种形态

2. 如何在程序表达多态
    其实在程序中表达多态就是继承
    是继承背景下引申出来的概念
    例如动物类有：人类，狗类，猪类，这些都是动物的多种形态

3. 为何要有多态(多态会带来怎样的特性)
    多态性是指定在不考虑对象具体类型的情况下而直接使用对象

    好处
        方便了使用者，使用者只需要知道父类有什么方法就可以使用
        相当于用父类整合了子类的功能，进行了封装

    父类的作用：统一所有子类的方法

4. 理解
    例子1
        如果子类是各种汽车的品牌，父类是驾驶汽车的技术，使用者只需要学习驾驶技术即可
        各种汽车根据父类定制的驾驶技术只是大同小异，使用者不需要单独学习每种汽车的驾驶技术

    例子2(python中的len函数)
        len函数可以算出各种类型对象的长度，而底层的实现方法就是使用了多态性
        为每个类型都定值一个算出长度的len函数，然后用父类统一把这些len函数集中在一起
        最后把父类封装成一个函数供使用者调用

"""

class Animal:
    def say(self):
        print('动物基本的发声频率   ',end='')

class People(Animal):
    def say(self):
        super().say()
        print('啊啊啊')

class Dog(Animal):
    def say(self):
        super().say()
        print('汪汪汪')

class Pig(Animal):
    def say(self):
        super().say()
        print('哼哼哼')


obj1 =People()
obj2 = Dog()
obj3 = Pig()

obj1.say()
obj2.say()
obj3.say()


# # 定义统一的接口，接收传入的对象
# def animal_say(Animal):
#     animal.say()


# 每种数据类型下面都有自己的方法算出长度
print('hello'.__len__())
print([1,2,3].__len__())
print({"a":1,"b":2,"c":4}.__len__())

# 统一接口
def my_len(val):
    return val.__len__()

print(my_len('hello'))
print(my_len([1,2,3]))
print(my_len({"a":1,"b":2,"c":4}))
