"""
property和隐藏属性

    为了确保程序的安全必须设置隐藏属性，可以通过开放接口实现

    但是通过开放接口会把所有的操作都变成调用方法，有些只是查看变量。
    与人的逻辑不符合，所以就需要用property装饰器把方法伪装成原来的变量属性

    但是如果有很多接口，每个接口需要设置property装饰器，也会很麻烦
    所以property提供了一种快速设置的语法

    语法
        名字 = property(要设置property的方法名，他们之间用逗号隔开)
    调用
        直接对象调用设置好的名字即可
        调用的时候会根据操作方式，参数，自动选择方法
    理解
        可以将多个相关的方法同时封装并伪装成同一个变量
        把多个方法封装到一个变量中

"""


class People:

    def __init__(self,name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self,val):
        if type(val) is not str:
            print('必须传入字符串类型')
            return
        self.__name = val

    def del_name(self):
        print('不能删除')
        # del self.__name

    # 伪装成同一个变量
    name = property(get_name, set_name, del_name)

obj = People('rs')
print(obj.name)
obj.name = 'xm'
print(obj.name)
del obj.name

"""
property扩展

class People:   
    
    def __init__(self,name):
        self.__name = name

    @property                         obj.name
    def get_name(self):
        return self.__name
        
        
    @name.setter                      obj.name = 'str'
    def name(self,val):
        if type(val) is not str:
            print('必须传入字符串类型')
            return
        self.__name = val

    @name deleter                      del obj.name
    def name(self):
        print('不能删除')
        # del self.__name 
        

语法
    把要装饰成变量的方法名全部改成要伪装成变量的名称
    根据不同执行方式设置不同的装饰器
    @property      直接查看方法
    @name.setter   调用方法赋值
    @name deleter  删除属性的方法
    
    调用的时候还是和上面的一样

"""