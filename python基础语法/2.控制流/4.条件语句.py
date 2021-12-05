"""
if-else语句
    if语句格式：
    if 布尔值表达式：
        pass(表达式是True执行的语句)
    else:
        pass(表达式是False执行的语句)

    格式：if和else的最后面都有冒号
         else语句可以没有
         else语句不可以单独存在
         if和else后面的语句必须缩进，缩进是python的语法

    if语句的逻辑：
        布尔值表达式必得到True或者False
        if或者else语句同时存在时，必有一个语句被执行

"""
if 3 >= 3:
    print('This is True')
else:
    print("This is False")

"""
elif语句
    elif语句是else语句嵌套if-else语句的缩写
    elif语句后面需要接条件，而且后面要有逗号

elif语句的逻辑
    elif语句的(条件)次序很重要，因为遇到True的判断条件就会跳过后面的判断
    条件的顺序原则：大范围到小范围(从一大堆中，不断缩小筛选范围，最后选一个情况出来)
    elif语句的适用情况: 有多种情况，每一种情况都需要对应的语句
    简而言之：类似switch-case语句，刚好python没有switch-case语句

    elif语句最多只能有一个语句被执行
    如果条件都不符合，会执行最后的else语句(else语句可以没有)
"""


