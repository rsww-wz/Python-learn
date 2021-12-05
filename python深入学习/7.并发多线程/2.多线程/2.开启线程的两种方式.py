"""
开线程不需要再main下执行代码，但是还是习惯将启动命令写在main下面

"""

from threading import Thread
import time


def task(name):
    print('%s is running' % name)
    time.sleep(1)
