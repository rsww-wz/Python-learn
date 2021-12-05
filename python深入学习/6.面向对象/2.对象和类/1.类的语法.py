"""
1. 流程
    先定义类
    在调用类产生对象

2. 定义类
    使用class关键字
    类名使用驼峰命名法

    类里面应该定义对象共有变量和功能，但是里面其实什么代码都可以放

3. 类体代码执行顺序
    类体代码在定义阶段就运行了
    即使不实例化，不调用，只是单纯的定义了类，也会执行类里面的代码
    因为类里面的属性和功能都是需要名称，必须执行才能产生名称空间
    也就是类的名称空间是在类定义的阶段就产生了

4. 查看类的名称空间
    类名.__dict__

5. 访问类的名称空间
    首先要说的是，类定义的东西也是给对象使用的
    所以理论上应该由对象访问类里面的变量和函数，但是类也是对象，也可以访问，但是不推荐

6. 访问变量属性
    原理上：类名.__dict__['key']
    python提供语法：类名.属性(变量和函数)
    这种方法本质上也是调用了__dict__加key的方法
"""


# 定义类
class Student:
    # 定义
    stu_school = "xxx中学"

    def tell_stu_info():
        print('Good morning')

    print('hello world')


# 查看类的名称空间
print(Student.__dict__)

# 访问类的名称空间
print(Student.__dict__['stu_school'])

# 访问变量属性
print(Student.stu_school)

# 访问函数属性
print(Student.tell_stu_info)

# 执行函数属性
Student.tell_stu_info()
