class School:

    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex


class Student(School):

    def __init__(self,name,age,sex,id):
        School.__init__(self,name,age,sex)
        self.id = id
        self.classes = []

    def choose_classes(self,classes):
        self.classes.append(classes)

    def check_classes(self):
        for class_name in self.classes:
            print(class_name)

class Teacher(School):

    def __init__(self,name,age,sex,wage):
        School.__init__(self,name,age,sex)
        self.wage = wage
        self.level = None

    def check_level(self):
        if self.wage < 3000:
            self.level = 'low'
        elif self.wage < 4000:
            self.level = 'middle'
        else:
            self.level = 'hight'
        
        return self.level


std1 = Student('rs',20,'male','18132232')
std1.choose_classes('工业机器人')
std1.choose_classes('单片机应用技术')
std1.choose_classes('电工电子技术')
std1.check_classes()

tea1 = Teacher('lly',40,'male',4500)
print(tea1.check_level())