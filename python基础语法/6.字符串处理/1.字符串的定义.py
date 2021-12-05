"""
字符串的定义
    字符串的定义可以用:
        一对单引号
        一对双引号
        三个单引号
        三个双引号

    当字符串里面有转义字符时：
        斜杆不与其他字母组成转义字符
            斜杆不在末尾：可以直接输出,也可以用双斜杆
            斜杆在末尾，：用斜杆转义斜杆，用双斜杆
        斜杆与其他字母组成转义字符时：
            在中间：用双斜杆
            在末尾：用双斜杆

        总结：如何字符串中要输出双斜杆，一律用双斜杆

    当字符串里面有引号时：
        如果只有单引号就用双引号
        如果只有双引号就用单引号
        
        既有单引号又有双引号时,并且以引号结尾时：
            最好的方法就是用斜杆转移引号
            而且要转义同一对引号
            转义与字符串定义冲突的那对引号(转义最外面有相同一对引号组成空白字符串)

    如果字符串是地址：
        通常有很多斜杆，而且很容易与字母组成转义字符
        这时，最好在字符串前面加r，表示原始字符
        用r：会原封输出字符串的全部内容

    字符串太长：
        1.可以在要换行的地方用斜杆转义，下一行要顶格书写，但是不太美观
        2.可以让每一行都成为一个字符串，换行的地方用斜杆转移一下行的引号(引号\，结尾)
            全部如果字符串中没有引号，全部用同一种引号即可，换行不用顶格书写
            
"""
spam = 'hello'
spam1 = "world"
spam2 = '''Good'''
spam3 = """morning"""

print(spam)
print(spam1)
print(spam2)
print(spam3)

# 斜杆
temper = 'hello \world'
temper1 = 'hello \\world'
temper2 = 'hello world\\'
temper3 = 'Good mor\\ning'
temper4 = 'Good morning\\n'

# 引号
temper5 = 'he say,"he run out of his money"'
temper6 = "he say,'he run out of his money'"
temper7 = "he say,\"he run out of his 'money'\""
temper8 = "\"hello\" 'world'"
temper9 = '"hello" \'world\''

# 地址
temper10 = r"C:\Users\RONG\source\repos"

# 长字符串
string = "有时候我们放不开不是因为失去，而是心疼自己的付出。\
遗忘的好处是：也许会后悔，也许会难过，但是心却不会再疼。\
曾经看不惯，受不了的，如今不过淡然一笑。成熟，不是看破，而是看淡。"

string1 = '有时候我们放不开不是因为失去，而是心疼自己的付出。' \
          '遗忘的好处是：也许会后悔，也许会难过，但是心却不会再疼。' \
          '曾经看不惯，受不了的，如今不过淡然一笑。成熟，不是看破，而是看淡。'

print(temper)
print(temper1)
print(temper2)
print(temper3)
print(temper4)
print('\n')

print(temper5)
print(temper6)
print(temper7)
print(temper8)
print(temper9)
print(temper10)
print('\n')

print(string)
print(string1)
