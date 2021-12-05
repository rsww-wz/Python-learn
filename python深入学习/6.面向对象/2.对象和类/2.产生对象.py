"""
1. 让类和对象产生关联
    因为定义了类只是把对象中公共部分的数据提取出来，并没有让这部分数据和对象产生关联

2.实例化
    让类和对象产生关联
    语法：类名()
    会创建一个对象，自动把类里面的数据给到对象，建立好联系

    返回值：创建好的对象

3. 对象里面存放的是什么
    查看对象里面存放的是什么
    创建好的对象是空的，里面什么都没有，不会有类里面的任何属性
    语法：对象名.__dict__

4. 对象添加属性
    原始语法：对象.__dict__[key] = value
    简介语法：对象.属性 = 值
    本质上也是调用了对象的dict字典

5. 添加属性问题
    即使是使用了简介语法，在给每个对象添加属性时，也会产生重复的代码
"""

class Student:
    stu_school = "xxx中学"

    def tell_stu_info():
        print('hello world')


#创建对象
stu1 = Student()
stu2 = Student()

# 查看对象数据
print(stu1.__dict__)

# 原始语法添加属性
stu1.__dict__["stu_name"] = 'rs'
stu1.__dict__["stu_age"] = 18
stu1.__dict__["stu_gender"] = 'male'

# 查看对象数据
print(stu1.__dict__)

# 简介语法添加属性
stu2.stu_name = '小红'
stu2.stu_age = '17'
stu2.stu_gender = 'famale'

# 查看对象属性
print(stu2.__dict__)
