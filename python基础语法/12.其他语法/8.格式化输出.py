"""
format()函数
    作用：函数把字符串当成一个模板，通过传入的参数进行格式化，
        并且使用大括号‘{}’作为特殊字符代替'%'
    
    使用的两种方法
        string.format()
        format(string,b)

    基本用法
        不带编号：{}
        带数字编号：{1}，{2}
        带关键字：{a}

    进阶用法
        (默认）左对齐、> 右对齐、^ 中间对齐、= （只用于数字）在小数点后进行补齐
        取位数“{:4s}”、"{:.2f}"

    可以通过字典和列表来给定参数

3、多个格式化
    'b' - 二进制。将数字以2为基数进行输出。
    'c' - 字符。在打印之前将整数转换成对应的Unicode字符串。
    'd' - 十进制整数。将数字以10为基数进行输出。
    'o' - 八进制。将数字以8为基数进行输出。
    'x' - 十六进制。将数字以16为基数进行输出，9以上的位数用小写字母。
    'e' - 幂符号。用科学计数法打印数字。用'e'表示幂。
    'g' - 一般格式。将数值以fixed-point格式输出。当数值特别大的时候，用幂形式打印。
    'n' - 数字。当值为整数时和'd'相同，值为浮点数时和'g'相同。不同的是它会根据区域设置插入数字分隔符。
    '%' - 百分数。将数值乘以100然后以fixed-point('f')格式打印，值后面会有一个百分号
"""

#不带编号
print('{} {}'.format('hello','world'))

 #带数字编号
print('{0} {1}'.format('hello','world'))
print('{1} {1} {0}'.format('hello','world'))

#带关键字编号
print('{a} {tom} {a}'.format(tom='hello',a='world'))
print('\n')

#默认左对齐
print('{} and {}'.format('hello','world'))  

#取10位左对齐，取10位右对齐
print('{:10s} and {:>10s}'.format('hello','world'))  

#取10位中间对齐
print('{:^10s} and {:^10s}'.format('hello','world')) 

#取2位小数
print('{} is {:.2f}'.format(1.123,1.123))  

#取2位小数，右对齐，取10位
print('{0} is {0:>10.2f}'.format(1.123))  
print('\n')

#关键字编号
print("网站名：{name}, 地址 {url}".format(name="百度", url="www.baidu.com"))
 
#通过字典设置参数
site = {"name": "百度", "url": "www.baidu.com"}
print("网站名：{name}, 地址 {url}".format(**site))
 
# 通过列表索引设置参数
lst = ['百度', 'www.baidu.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(lst))