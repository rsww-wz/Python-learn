"""
队列Queue模块
    队列：先进先出
    堆栈：先进后出

存数据
    存是为了更好的取
    原则：千方百计的存，简单快捷的取

"""

# from multiprocessing import Process,queues
import queue

# 创建一个队列
# 括号内可以穿数字，表示生成的队列最大可以同时存放的数据量
# 默认值为0,最大值是32767
# 当队列数据存放满了之后，如果还有数据要存放，程序和阻塞，直到有位置让出来，不会报错
q = queue.Queue(5)

# 往队列中存放数据
q.put(111)
q.put(222)
q.put(333)
q.put(444)
q.put(555)

# 判断当前队列是否满了
print(q.full())

# 取队列中取数据
# 队列中如果没有数据了，get方法会原地阻塞
v1 = q.get()
v2 = q.get()
v3 = q.get()
v4 = q.get()
v5 = q.get()

# 判断当前队列是否空了
print(q.empty())

# 没有数据直接报错,queue.Empty错误
# v6 = q.get_nowait()

# 没有数据之后原地等待三秒，再报错
v6 = q.get(timeout = 3)

print(v1, v2, v3, v4, v5)

"""
总结
    put():存放数据
    get()：取出数据
    get(timeout = num):如果超过设定秒数还是没有数据，就会报错
    get_nowait()：如果没数据，不等待，直接报错
    full()：判断队列是否满了
    empty()：判断队列是否空了
    
注意
    get()
    put()
    get_nowait()
    
    在多进程的情况下，这三个方法是不能使用的，因为它是不精确的
"""