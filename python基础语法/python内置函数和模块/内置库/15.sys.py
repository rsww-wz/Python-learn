"""
sys模块：主要针对python解释器

sys.exit(n):退出程序
    0:正常退出
    1.错误退出
sys.version():python版本
sys.path()
    返回模块搜索路径
    现在当前文件夹，然后找当前工作目录，最后找python解释器
    导入模块的时候，如果模块不在这个文件下面，path路径找不到，是不能导入成功的
    扩文件夹添加模块的时候，可以把要导入的模块的路径进path即可
"""

import sys
import pprint

print(sys.version)
pprint.pprint(sys.path)
sys.exit(0)
