"""
1. 魔术方法特点
    以__开头，__结尾的方法
    魔术方法有很多，需要自己学习，一般是在写框架这些才会用得到
    会在某种情况下自动调用执行
    所以魔术方法用应该是自动调用的，而不应该是手动调用的

2. 为何有用魔术方法
    为了定制化类或者对象

3. 如何使用魔术方法
    __str__：的打印对象是自动触发，然后将返回值（必须是字符类类型），当做本次打印结果输入
    __del__：在清理对象是触发，会先执行该方法，程序运行结束也会触发该方法
        常用做法：发起系统调用，告诉操作系统回收相关系统资源

"""

class People:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    # 打印对象才会触发这个魔术方法
    def __str__(self):
        return '<%s:%s>' %(self.name,self.age)

    def __del__(self):
        print('删除了')

    def say(self):
        print('<%s:%s>' %(self.name,self.age))

obj = People('rs',20)
print(obj)