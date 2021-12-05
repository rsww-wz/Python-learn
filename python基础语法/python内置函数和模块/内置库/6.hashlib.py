"""
hashlib：加密模块
主要用的md5加密算法

MD5：是一种不可逆的加密算法，是不可以被破解的
每个数据都有唯一的md5，虽然不可以破解，但是可以通过不断生成不同数据的md5
所以可以通过一些手段查询到md5的值
所以需要对原来的数据做一些伪装

在处理密码等比较重要的数据，应该采用加密存储

使用
    hashlib.md5:创建一个md5对象
    obj.update(string.encode("utf-8")):update要求必须是字节
    obj.hexdigest():拿到密文

    伪装
        生成md5对象的时候，可以用伪装
        伪装必须是字节类型
        伪装可以是动态的，提高安全性

文件加密
    文件也可以加密
    作用：通过判断md5的值，可以判断两个文件是不是同一个文件（文件一致性）
    网盘上传技术
    下载文件的时候是否被篡改，下载的文件与原文件的md5值比较
"""

import hashlib

# 创建md5对象
obj = hashlib.md5()
# md5密文
obj.update("666".encode("utf-8"))
# 得到md5密文
mi = obj.hexdigest()
print(mi)

# 伪装
obj = hashlib.md5(b'jdksfos')
obj.update("666".encode("utf-8"))
mi = obj.hexdigest()
print(mi)
