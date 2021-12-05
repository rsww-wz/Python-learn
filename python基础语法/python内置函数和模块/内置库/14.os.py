"""
作用：主要针对操作系统的操作

os.makedirs()
    可以一次性创建多级目录
    如果使用相对路径：是在当前工作目录里面创建的
    上层文件夹可以不存在：如果文件夹存在就跳过当前文件夹，如果不存在就创建

os.mkdir()
    上层文件夹必须存在
    创建最后一个文件夹

os.removedirs()
    删除当前这个目录中所有空的文件夹
    不常用

os.rmdir()
    删除指定文件夹

os.listdir()
    列出该文件夹的所有内容，包括文件

os.remove()
    删除文件

os.rename()
    重命名文件

os.stat()
    获取文件/目录信息

os.system()
    运行shell命令，直接显示
    命令必须是字符串形式

os.popen("命令").read()
    在python中运行shell命令

os.getcwd()
    获取当前工作目录
    返回的是字符串形式

os.chdir()
    改变当前工作目录
    相当于shell里面的cd

os.path模块
    和文件夹路径相关的函数

    os.path.abspath():返回给定路径的绝对路径
    os.path.split():返回文件路径和文件名，返回的是元组
    os.path.dirname():返回文件的目录
    os.path.basename():返回文件的名字
    os.path.exists():判断路径是否存在
    os.path.isabs():判断路径是否是绝对路径
    os.path.isfile():判断路径是否是文件
    os.path.isdir():判断路径是否是路径
    os.path.getatime():返回路径或文件最后的访问时间
    os.path.getmtime():返回路径或者文件最后的修改时间
    os.path.getsize():返回路径的大小,返回的单位是byte
        1024byte = 1KB
        1024KB = 1MB
"""

import os
import pprint

# os.makedirs("模块/文件/os模块")
# os.system("dir")
# print(os.popen("dir").read())

spam = os.getcwd()
print(spam)
print(type(spam))

spam1 = os.stat(spam)
print(type(spam1))

# os.chdir("python算法")
# print(os.getcwd())

spam3 = os.path.abspath("sys.py")
print(spam3)

address = r"E:\0-code\visual studio code\python学习\python内置函数和模块\内置库\2.time.py"
address1 = r"F:\教程\python基础语法\- 103.05 self是谁.mp4"

lst = os.path.split(address)
lst = list(lst)
print(lst)

lst1 = os.path.dirname(address)
lst2 = os.path.basename(address)

print(lst1)
print(lst2)
print(os.path.exists(address))
print(os.path.isabs(address))
print(os.path.isfile(address))

size = os.path.getsize(address1)
size1 = size/1024/1024
size1 = round(size1,2)
print(str(size1) + "M")