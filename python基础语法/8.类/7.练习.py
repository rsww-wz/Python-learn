class School:

    def __init__(self,name,area,location):
        self.name = name
        self.area = area
        self.location = location
        self.classes = []

    def add_class(self,class_name):
        self.classes.append(class_name)

    def look_classes(self):
        for class_name in self.classes:
            print(class_name)
        
class1 = School('广东交通职业技术学院',1000,'广州，花都')
class1.add_class("机电一体化")
class1.add_class("工业机器人")
class1.add_class("电气自动化")
class1.look_classes()
