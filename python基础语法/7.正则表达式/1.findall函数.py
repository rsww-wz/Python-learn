"""
要使用正则表达式，必须导入re库，使用库里面的函数
因为只有里面的函数的参数才能接受正则表达式

调用库函数
    库名.函数名()

findall()函数
    findall()是全局匹配

    第一个参数：正则表达式,都需要用引号，是把整个表达式引起来
    第二个参数：要匹配的字符串
    第三个参数：匹配模式(flag标志位)
        re.I——忽略大小写匹配（忽略你要匹配的字符和字符串中的字符的大小写关系）
        re.S——在使用英文句号时，能匹配上换行符，也就是换行符能匹配所有符号了

        同时使用多个匹配模式时，模式之间用竖线连接（|），他们之间是且的关系
    
    返回值：
        返回的匹配到的结果
        匹配到的结果是以列表的方式返回的，要用变量去接收

"""
import re

string = "But if, in your fear, you would seek only love’s peace " \
         "and love’s pleasure, then it is better for you that you cover" \
         "your nakedness and pass out of love’s threshing-floor, into the " \
         "seasonless world where you shall laugh, but not all of your laughter, " \
         "and weep, but not all of your tears. Love gives naught but it self" \
         "and takes naught but from itself. Love possesses not, nor would it" \
         " be possessed, for love is sufficient unto love"

spam = re.findall('love', string)
spam1 = re.findall('but', string, re.I)
print(spam)
print(spam1)
