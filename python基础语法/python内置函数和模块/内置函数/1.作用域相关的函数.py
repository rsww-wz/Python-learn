# globals函数：查看全局作用域所有内容
# locals函数：查看局部作用域所有内容,返回的是字典


a = 10
def func():
    b = 20
    print(locals())

# print(globals())
func()