"""
福利
    如果专业版的pycharm过期了，需要重新输入激活码，可以直接更新的最新版
    然后去这个网站：http://idea.medeming.com/jets/，里面有激活码
"""

"""
进程对象与其他方法
    一台计算机上运行着很多进程，那么计算机是如何区分并管理这些进程服务的呢？
        计算机会给每一个运行的进程分配一个PID号
        Windows电脑，进入cmd，输入tasklist即可查看
    根据PID查看具体进程
        tasklist | findstr PID
        
    查看当前进程的进程号
        current_process().pid
        os.getpid():获取进程的pid
        os.getppid(): 获取当前进程的父进程pid
        
    其他方法
        is_alive()：判断当前进程是否存活
        p.terminate()：杀死当前进程，是操作系统帮你完成，但是需要一定时间
"""

from multiprocessing import Process, current_process
import time
import os


def task():
    # 查看当前进程的PID号
    name = current_process().pid
    name1 = os.getpid()
    name2 = os.getppid()
    print('%s is running' % name1)
    print('子进程的主进程pid号：%s' % name2)
    time.sleep(2)


if __name__ == '__main__':
    p = Process(target=task)
    p.start()

    # 杀死当前进程
    p.terminate()

    # 判断当前进程是否存活
    print(p.is_alive())

    name = current_process().pid
    name1 = os.getpid()
    name2 = os.getppid()
    print('主程序', name1)
    print('主主程序', name2)  # pycharm
