"""
1. 菱形问题
   菱形问题是一种继承结构，这个结构的外形想一个菱形，所以称之为菱形问题，或者钻石问题
   也就是一个子类继承多个父类，最终都汇集到一个非object的类

2. MRO列表
    对于你定义的每一个类，Python都会计算出一个方法解析顺序
    继承查找属性的顺序就是根据MRO列表的顺序查找的
    每个类都会都一个MRO列表
    MRO是基于C3线性算法实现的

    准则
        子类会先于父类被检查
        多个父类会根据它们在列表中的顺序被检查
        如果对下一个类存在两个合法的选择，选择第一个父类

    注意
        mro是固定的，但是mro在python2和python3中算出来的结果是不一样的

"""

# 菱形问题
class A:
    def f1(self):
        print('from A')

class B(A):
    def f1(self):
        print('from B')

class C(A):
    def f1(self):
        print('from C')

class D(B,C):
    pass

obj = D()
print(obj.f1())
print(D.mro())


