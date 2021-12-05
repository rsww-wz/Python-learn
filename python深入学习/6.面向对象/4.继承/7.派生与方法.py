"""
在子类派生的新方法中如何重用父类的功能

方式1：指名道姓调用某一个类下的函数，不依赖与继承关系
方式2：super()调用父类提供给自己的方式，严格依赖于继承关系

super()
    语法
        python2：super(自己的类，self).__init__()
        python3：super().__init__(参数)



    调用super()会得到一个特殊的对象，这个对象会参照发起属性查找的那个类的mro，去当前类的父类中访问属性

注意：使用super()调用构造函数的参数列表不能有self(否则相当于前功尽废，因为self指代就是调用对象)
    但是指名道姓调用构造函数中的参数列表是一个都不能少，包括self
    super()不止可以调用构造函数，还可以调用其他任意方法，但是没有太大意义

"""

class SchoolPeoPle:
    school = 'xxx学校'

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

class Student(SchoolPeoPle):

    def choose_course(self):
        print("%s 正在选课" % self.name)

class Teacher(SchoolPeoPle):
    school = 'xxx学校'

    #父类没有完全覆盖子类属性
    def __init__(self, name, age, sex, salary, level):

        # 指名道姓跟父类要属性
        # 注意里面的参数一个都不能少
        # 这不是构造函数，而是一条调用函数的语句
        # SchoolPeoPle.__init__(self, name, age, sex)

        # 调用的是方法，传入的是对象
        super().__init__(name, age, sex)
        self.salary = salary
        self.level = level

    def score(self):
        print('老师%s正在给学生打分' % self.name)

tea = Teacher('xm',30,'male',4000,8)
print(tea.__dict__)
tea.score()