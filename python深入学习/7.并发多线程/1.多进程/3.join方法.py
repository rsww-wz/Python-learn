"""
join是让主程序等待子进程代码运行结束之后，在继续运行，不影响其他子进程的执行

创建多个进程，多个进程之间的执行顺序是随机的

用Process创建的是一个对象，这个对象就是进程，但是它是子进程
主进程是main函数下面的代码

默认情况下，进程数据是相互隔离的
"""

from multiprocessing import Process
import time

def task(name,n):
    print('%s子进程开始' %name)
    time.sleep(n)
    print('%s子进程结束' %name)

if __name__ == '__main__':
    # 创建三个进程
    # 这三个进程是独立的个体，互不干扰
    # p1 = Process(target=task, args=('p1',1))
    # p2 = Process(target=task, args=('p2',2))
    # p3 = Process(target=task, args=('p3',3))
    #
    # start_time = time.time()
    #
    # p1.start()
    # p2.start()
    # p3.start()
    #
    # # 主进程等待子进程结束之后再执行
    # # p.join()
    #
    # # 必须要进程全开了才能实现并发
    # p1.join()
    # p2.join()
    # p3.join()
    #
    # print('主进程',time.time() - start_time)

    # 改进写法
    start_time = time.time()
    list_p = []
    # 先创建进程
    for i in range(1,4):
        p = Process(target=task, args=('p%s'%i,i))
        p.start()
        list_p.append(p)

    for p in list_p:
        p.join()

    print('主进程', time.time() - start_time)