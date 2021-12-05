"""
生产者消费者模型
    生产者：生成制造东西
    消费者：消费处理东西
    该模型还需要一个媒介
        产者和消费者之间不是直接做交互的，而是借助于媒介做交互
        生产者（做包子的）+消息队列（蒸笼）+消费（吃包子的）

JoinableQueue
    JoinableQueue 每当你往该队列中存入数据的时候内部会有一个计数器+1
    每当你调用task_done的时候，计数器-1
    q.join（）当计数器为0的时候才往后运行

"""

from multiprocessing import Process, Queue, JoinableQueue
import time
import random


# 生产者
def producer(name, food, q):
    for i in range(10):
        data = '%s生产了%s%s' % (name, food, i)

        # 模拟延迟
        time.sleep(random.randint(1, 3))
        print(data)

        # 将数据放入队列中
        q.put(data)


# 消费者
def consumer(name, q):
    while True:
        food = q.get()

        # 判断是否有结束的标志
        # if food is None: break

        time.sleep(random.randint(1, 3))
        print('%s吃了%s' % (name, food))

        # 告诉队列你已经从里面取出了一个数据并且处理完毕了
        q.task_done()


if __name__ == '__main__':
    # 消息队列(中间媒介)
    # q = Queue()

    # 创建队列计数对象
    q = JoinableQueue()

    p1 = Process(target=producer, args=('大厨1', '包子', q))
    p2 = Process(target=producer, args=('大厨2', '面条', q))
    c1 = Process(target=consumer, args=('老大', q))
    c2 = Process(target=consumer, args=('老二', q))

    p1.start()
    p2.start()

    # 只要执行完毕就说明消费者已经处理完毕数据了，消费煮就没有存在的必要了
    # 此时可以设置完守护进程
    c1.daemon = True
    c2.daemon = True

    c1.start()
    c2.start()

    # 等待生产者生产完毕之后往队列中添加特定的结束符号
    p1.join()
    p2.join()

    # 有两个消费者，如果只有一个None，可能会出现两个消费者争抢一个None
    # q.put(None)
    # q.put(None)

    # 等待队列中所有数据被取完再执行以下代码
    q.join()
