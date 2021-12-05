def findNumber():
    for i in range(0,50):
        if i % 2 == 0:
            continue
        else:
            print(i,end = ',')

findNumber()
print('\n')

sum = 0
def sum():
    firstNumber = int(input('请输入加数'))
    secondNumber = int(input('请输入被加数'))
    sum = firstNumber + secondNumber
    return sum

spam = sum()
print(spam)

temper = findNumber()
print(type(temper))
print(temper)


"""
函数的定义；
    def 函数名（参数）：
        代码块
        return 返回变量

函数的调用：
    函数必须在被调用之前定义好，否则会报错
    也就是在调用函数之前，把函数定义好，而且必须放在调用语句的前面 

return语句：
    函数应该返回的值或者表达式
    return语句如果使用列表达式，返回值是该表达式求值的结果
    注：表达式是值和操作符的组合

    函数可以返回多个值，不过需要用到列表和元组，后面在具体说明

None值：
    None表示没有值，None的类型是NoneType
    None首字母必须大写
    None不表示0或者其他，它就是什么都没有

    没有return语句的函数，python默认在末尾加上：return None
    类似的while或者for，


"""