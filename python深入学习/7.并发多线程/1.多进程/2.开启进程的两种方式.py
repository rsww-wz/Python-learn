"""
代码开启进程和线程的方式，代码书写基本是一样的，学会了开启进行就会开启线程

windows操作系统下，创建进程一定要在main内创建
因为Windows下创建进程类似于模块导入的方式，会从上往下一次执行

linux下是将代码完整拷贝一份

"""

# 方式1
# from multiprocessing import Process
# import time
#
# def task(name):
#     print('%s is running' %name)
#     time.sleep(3)
#     print('%s is over' %name)
#
# if __name__ == '__main__':
#
#     # target是函数名，args是函数的参数，类型是元组
#     # 容器类型无论里面有几个元素，哪怕只有一个元素，特别是元组，建议用逗号隔开
#
#     # 实例化一个对象
#     p = Process(target=task,args = ('进程',))
#
#     # 开启进程
#     # 告诉操作系统帮你创建一个进程  异步
#     p.start()
#
#     # 目前有两个进程，一个是task，一个是在main里面的创建进程
#     print("测试")


# 方式2 类的继承方式
from multiprocessing import Process
import time


class MyProcess(Process):
    def run(self):
        print('hello world')
        time.sleep(2)
        print("Good morning")


if __name__ == '__main__':
    p = MyProcess()
    p.start()
    print('主进程')

"""
总结
    创建进程就是在内存中申请一块内存空间将需要运行的代码丢进去
    一个进程对应在内存中就是一块独立的内存空间
    多个进程对应在内存中就是多块独立的内存空间
    进程与进程之间数据默认情况下是无法直接交互，如果想交互可以借助于第三方工具，模块
"""