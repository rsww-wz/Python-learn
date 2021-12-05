"""
单继承查找顺序
    先到自己的类中找，如果找不到，就去父类里面找，直到找到位置
    理解：自己——爸爸——爷爷——太爷爷……

"""

class Foo:
    def f1(self):
        print('from f1')

    def f2(self):
        print("from f2")
        self.f1()   #obj.f1()


class Bar(Foo):
    def f1(self):
        print('Bar.f1')


# 注意self指代的那个对象
obj = Bar()
obj.f2()
