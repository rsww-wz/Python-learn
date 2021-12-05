"""
进程间通信

IPC机制
    理解：把要通信的数据放进队列中，然后主进程和子进程都可以访队列数据，实现通信

思路
    主进程跟子进程借助队列通信
    子进程跟子进程借助队列通信
"""

from multiprocessing import Queue,Process

def producer(q):

    # 把数据放进队列
    q.put('Good morning')
    print('hello world')

def consumer(q):
    print(q.get())


if __name__ == '__main__':

    # 创对队列
    q = Queue()

    # 创建进程
    p = Process(target=producer,args = (q,))
    p1 = Process(target=consumer,args = (q,))

    # 启动进程
    p.start()
    p1.start()

    # 主进程通过队列访问子进程数据
    print(q.get())