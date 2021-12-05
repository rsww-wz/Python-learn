"""
元类了解即可，基本用不到，而且复杂难懂

1. 什么是元类
    都源自python的一切皆对象

    对象都是类实例化得到的
    对象 = 类()
    类也是对象，那么类这个对象是如何得到的

    调用类产生类这个对象的类称为元类
    元类 = 类()

    元类：实例化产生类的类，类的爸爸
        元类——实例化——类——实例化——对象

2. 查看元类
    type(类)
    我们用class关键词定义的所有类以及内置的类都是内置元类type帮我们实例化产生的
    即：type是内置元类，一切都都是由type实例化得到的

3. class机制分析
    类的三大特征
        类名
        类的基类
        执行类的代码拿到类的名称空间 (类体代码本身就是以堆字符串)

    class造类的步骤
        拿到类名
        拿到基类
        拿到类的名称空间
        调用元类，传以上参数
            返回值 = type(类名，名称空间，基类)

    class关键词做的就是以上四个步骤

    以上步骤只有调用元类是不可以控制的，其他都是可以直接修改类得到
    所以如果想定制化类，需要创建自己的元类实现类的实例化

4. 如何自定义元类控制类的产生
    如何继承自定义元类
        class 类名(metaclass = 自定义元类)

    自定义元类
        必须继承type，只有继承了type类才能称之为元类
        class Mymeta(type)

        调用Myeta发生的三件事
            先造一个空对象
            调用Mymeta这个类内的构造函数，完成初始化对象操作
            返回初始化好的对象

"""

# print(type(list))

class Mymeta(type):

    #           空对象，People，（object），{名称空间}
    def __init__(self,x,y,z):
        # print('run')
        # print(self)
        # print(x)  # 类名
        # print(y)  # 基类
        # print(z)  # 名称空间

        # 定制类名首字母必须大写
        if not x.istitle():
            raise NameError('类名首字母必须大写')


class People(metaclass=Mymeta):

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def say(self):
        print("%s:%s" %(self.name,self.age))

