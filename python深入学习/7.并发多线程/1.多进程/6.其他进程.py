"""
僵尸进程
    死了，但是没有死透
    当你开设了子进程之后，该进程死后不会立刻释放占用的进程号
    因为要让父进程查看的它开设的子进程的一些基本信息，占用的pid，运行时间等
    所有的进程最终都会步入僵尸进程
        父进程不死，并且无限制的创建子进程，并且子进程也不结束
        回收子进程的pid号：父进程等待子进程运行结束，父进程调用join方法

孤儿进程
    子进程存活，父进程意外死亡
    操作系统会开设一个进程专门回收相关资源

守护进程
    理解：随着操作系统启动而启动，操作系统关闭而关闭的进程


"""

from multiprocessing import Process
import time

def run():
    print('hello')
    time.sleep(2)
    print('world')

if __name__ == '__main__':
    p = Process(target=run)

    # 将进程设置为守护进程
    # 这句话必须放在start上面才有效，否则会直接报错
    p.daemon = True

    p.start()

    print('主程序')


