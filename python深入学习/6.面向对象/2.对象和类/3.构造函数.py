"""
1. 添加属性问题
    即使是使用了简介语法，在给每个对象添加属性时，也会产生重复的代码

2. 解决方法1
    在对象外使用函数
    可以实现给任意对象添加任意属性值的函数

    这样的方法可以解决代码冗余问题，但是有存在新的问题
    就是这个函数没有与类和对象产生关联，它没有被整合进去，还是一个独立的函数

3. 解决方法2
    在方法1的基础上把函数整合进类里面，就是直接把函数放进类里面
    但是实例化的时候，不会触发构造函数
    因此python提供了一种语法，可以实例化的时候自动执行构造函数

4. 构造函数的语法
    名字必须是：__init__()
    对象默认使用self,其实可以是任意单词
    没有返回值，或者返回值必须是None

5. 有构造函数的实例化语法
    调用类的过程也称为实例化对象
    实例化的时候自动调用构造函数
    会自动把对象传进构造函数里面
    需要在实例化的时候传添加属性的参数
    返回初始化好的对象

6. 构造函数的使用
    想要调用类的时候就立刻执行的代码都可以放在构造函数中

6. 注意
    传参数的时候必须一一对应，顺序不能乱
    不能少参数，也不能多参数，否则会报错

"""


class Student:
    stu_school = "xxx中学"

    def tell_stu_info():
        print('hello world')


stu1 = Student()
stu2 = Student()


# 给对象添加属性函数
def addAttribute(obj, name, age, sex):
    obj.stu_name = name
    obj.stu_age = age
    obj.stu_sex = sex


# 给对象添加属性
addAttribute(stu1, 'rs', 18, 'male')
addAttribute(stu2, 'xh', 16, 'female')

# 查看对象属性
print(stu1.__dict__)
print(stu2.__dict__)


class Student1:
    stu_school = "xxx高中"

    # 构造函数
    def __init__(obj, name, age, sex):
        obj.stu_name = name
        obj.stu_age = age
        obj.stu_sex = sex

    def tell_stu_info():
        print('hello world')


std = Student1('xm', 20, 'boy')
print(std.__dict__)
