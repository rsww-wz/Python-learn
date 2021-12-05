"""
1. 查找顺序
    对象查询顺序
        先从对象自身开始找
        找不到就在类里面找

2. 类变量
    类中的属性也称为类变量
    类的数据和功能是共享给所有对象用的，大家访问的地址都一样
    如果一个对象修改了类变量，其他对象访问到的类变量也会跟着改变

    所以尽量不用用对象修改类变量
    而应该在类的内部用一个专门的方法来修改类变量

    类和对象都可以访问类变量，但是最好是只能类本身访问类变量

3. 实例变量
    对象添加的变量（构造函数中的变量）称为实例变量
    实例变量只能是对象访问
    类不能访问实例变量

4. 实例方法
    类中的函数分为类方法和实例方法
    操作类变量的函数称为类方法
    操作实例变量的函数称为实例方法

    实例方法是绑定给对象使用的

    类和对象也都是可以调用方法的
    对象调用方法只需要传实际参数就可以了
    类调用方法，方法的参数列表有多少个参数，就需要传多少个参数

    实例方法的特殊之处
        谁来调用实例方法就会将它当做实例方法的第一个参数自动传入
        因此，那个对象调用这个方法操作的就是这个对象
        所以如果类来调用实例方法需要传入操作的对象
        所以类中实例方法都要有一个参数，不管这个参数的名字是什么
        即使不是self,对象调用的时候，也不需要把自己手动传进去了

    记住：类最好不要调用实例方法

5. 理解
    在python中，str,list,dict等都是一个类
    创建对象后，都是用对象调用具体的方法，如果用类调用的话，就需要手动传入对象

6. self理解
    在类中，无论地方，需要用到具体的对象的，都要加self
    因为有了self,才可以绑定到调用对象上的身上
"""


class Student:
    stu_school = "xxx高中"
    count = 0

    # 构造函数
    def __init__(self, name, age, sex):
        self.stu_name = name
        self.stu_age = age
        self.stu_sex = sex
        Student.count += 1

    def tell_stu_info(self):
        print('hello world')


stu1 = Student('rs', 20, 'male')
print(Student.count)
stu2 = Student('xh', 18, 'female')
print(Student.count)

# 查找类变量属性
print(id(stu1.stu_school))
print(id(stu2.stu_school))

# 查看类变量
print(stu1.stu_school)

# 修改类变量
stu1.stu_school = 'xxx中学'

# 查看修改后的类变量
print(stu1.stu_school)
print(stu1.stu_school)

# 对象访问实例变量
print(stu1.stu_age)

# 类调用方法
Student.tell_stu_info(stu1)

# 对象调用方法
stu1.tell_stu_info()

# python中的例子
lst = [1, 2, 3]

# 用对象操作
lst.append(4)
print(lst)

# 用类操作
list.append(lst, 5)
print(lst)
