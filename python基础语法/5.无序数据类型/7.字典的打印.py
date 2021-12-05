"""
需要导入pprint库
    pprint()方法
        使输出比较干净
        对于嵌套的字典特别有用
    pformat()方法
        和pprint的功能一样，不过是输出到文本，不是输出到屏幕
"""

import pprint

week = {1:'monday',2:'tuesday',3:'wednesday',
4:'truesday',5:'firday',6:'saturday',7:'sunday'}

allGuests = {'Alice':{'apples':5,'pretzels':12},
            'Bob':{'ham sandwiches':3,'apples':2},
            'Carol':{'cups':3,'apple pies':1}}


pprint.pprint(week)
pprint.pprint(allGuests)

#统计字母出现次数
message = "Whether 60 or 16, there is in every human being’s heart "\
    "the lure of wonders, the unfailing appetite for what’s next and "\
    "the joy of the game of living. In the center of your heart and my heart,"\
    " there is a wireless station; so long as it receives messages of beauty, "\
    "hope, courage and power from man and from the infinite,"\
    " so long as you are young"

count = {}
for character in message:
    count.setdefault(character,0)
    count[character] += 1
pprint.pprint(count)

