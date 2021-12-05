"""
reduce函数的导入
    from functools import reduce

reduce语法
    参数
        第一个参数：一个函数
        第二个参数：一个序列
        第三个参数：初始值，可选参数
            如果没有初始值，同时取第一个和第二个元素做运算
            如果有初始值，就取第一个元素和初始值做运算

    返回值
        返回一个lambda的结果

reduce作用
    做连续计算，连续调用第一个参数的函数做运算
    返回的结果和下一个元素做运算

reduce应用场景
    一般也是配合lambda匿名函数使用
    涉及到连续的计算都可以使用
    在计算坐标的轨迹的时候，可以考虑使用

"""

from functools import reduce

lst = range(10)
r = reduce(lambda x,y: x + y,lst)
#((((1+2)+3)+4)+...+10)
print(r)

#第三个参数
spam = reduce(lambda x,y: x + y,lst,10)
print(spam)

lst1 = ['1','2','3','4','5','6','7','8','9']
spam1 = reduce(lambda x,y:x + y,lst1,'aaa')
print(spam1)
print(type(spam1))