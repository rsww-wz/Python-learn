class Dog():
    breed = ''
    size = 'middle'

    def __init__(self,color,weight,height,name):
        self.color = color                       #实例化
        self.weight = weight
        self.height = height
        self.name = name

    def getattribute(self,breed,size):
        self.breed = breed                      #实例化
        self.size = size
        attribute = [self.breed,self.size]      #访问实例变量
        return attribute

    def getcharacter(self):
        self.weight = str(self.weight)
        self.height = str(self.height)         #修改实例变量
        character = [self.color,self.weight,self.height,self.name]
        return character

    def pr_obj(self):                           #实例方法调用其他实例方法
        print(self.getcharacter())              #被调用的方法参数列表不需要self

    @classmethod                                #类方法
    def pr(cls):
        print(cls.size)                         #访问静态方法

    @staticmethod                               #静态方法
    def num(number):
        return number + 1


Teddy = Dog('gold',10.5,30,'white')              #创建对象，对象实例化
print(Teddy.getattribute('teddy','small'))       #对象调用特有实例方法
print(Teddy.getcharacter())                      #对象调用通用实例方法

Labrado = Dog('white','30.5','50.5','lala')
print(Labrado.getattribute('labrado','big'))
print(Labrado.getcharacter())

Teddy.pr_obj()                                #对象调用实例方法
print(Teddy.num(10))                          #对象调用静态方法

print(Dog.size)                               #对象访问类变量
print(Teddy.height)                           #访问实例变量,访问的是修改后的实例变量
print(type(Teddy.weight))                     

print(Dog.size)                               #类访问类变量
Dog.pr()                                      #类调用类方法
print(Dog.num(20))                            #类调用静态方法



"""
类的设计
    类最重要的是实例变量
    实例变量一定要实例化才能使用
    虽然构造函数是自动调用的，可以用构造函数来实例化对象
        但是构造函数有的形参，对象一定要传值，不然会报错
        如果有些属性只是某些对象有，放在构造函数实例化显然不合适，因为没有这个属性的
        对象也必须设定这些参数才能通过实例化

    实例变量的实例化其实放在实例方法也可以，只不过需要调用这个方法来实例化实例变量
    但是这样正好符合了我们的要求，让有特殊属性的对象调用这个方法，这样即满足对象的特殊
    属性要求，也不会让其他没有这个对象属性产生无关属性

    所以构造函数适合放一些对象共有的属性，因为构造函数的的参数列表必须和对象实例化的参数
    对应，所以一定不要把所有的实例变量都放在构造函数实例化

总结
    实例方法就是对象的方法
    实例变量就是调用对象时的参数
    
    静态方法就是普通的函数，对象和类都可以调用

    类变量和类方法有什么用，原则上对象不能访问类的属性和方法，那么怎么修改他们的值？
        类方法是操作变量的，这个问题就归结到类变量了
        类变量主要使用在类的继承上，多个类之间的变量都是通过类变量来传递的

"""