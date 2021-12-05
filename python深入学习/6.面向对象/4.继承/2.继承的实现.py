# 示范1：类与类存在冗余问题
# class Student:
#     school = 'xxx学校'
#
#     def __init__(self,name,age,sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def choose_course(self):
#         print("%s 正在选课" %self.name)
#
# class Teacher:
#     school = 'xxx学校'
#
#     def __init__(self,name,age,sex,salary,level):
#         self.name = name
#         self.age = age
#         self.sex = sex
#         self.salary = salary
#         self.level = level
#
#     def score(self):
#         print('老师%s正在给学生打分'%self.name)

# 基于继承解决冗余问题

class SchoolPeoPle:
    school = 'xxx学校'

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

class Student(SchoolPeoPle):
    # school = 'xxx学校'
    #
    # def __init__(self, name, age, sex):
    #     self.name = name
    #     self.age = age
    #     self.sex = sex

    def choose_course(self):
        print("%s 正在选课" % self.name)


stu1 = Student('lili',18,'female')
print(stu1.__dict__)
stu1.choose_course()


class Teacher(SchoolPeoPle):
    school = 'xxx学校'

    #父类没有完全覆盖子类属性
    def __init__(self, name, age, sex, salary, level):

        # 指名道姓跟父类要属性
        # 注意里面的参数一个都不能少
        # 这不是构造函数，而是一条调用函数的语句
        SchoolPeoPle.__init__(self, name, age, sex)
        self.salary = salary
        self.level = level

    def score(self):
        print('老师%s正在给学生打分' % self.name)

tea = Teacher('xm',30,'male',4000,8)
print(tea.__dict__)
tea.score()