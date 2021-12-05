"""
pickle模块的作用：
    把python中对象或者数据转化成字节存入文件中
    在网络传输中一般是以字节传输数据

    好处：能保留数据的原来的格式，加载的时候能还原原来的格式

函数主要要四个

    序列化：把对象转化成二进制
    反序列化：把二进制转化成对象

    pickle.load：把文件中的字节反序列化成对象（数据）
    pickle.loads：把字节转化成对象（数据）

    将python数据化成字节
    pickle.dump：把文件中的对象（数据）转化成字节
    pickle.dumps：把对象（数据）转化成字节

"""

import pickle

lst = ["hello","world","Good","morning"]
bs = pickle.dumps(lst)
print(bs)

bs = b'\x80\x03]q\x00(X\x05\x00\x00\x00helloq\x01X\x05\x00\x00\x00worldq\x02X\x04\x00\x00\x00Goodq\x03X\x07\x00\x00\x00morningq\x04e.'
lst = pickle.loads(bs)
print(lst)