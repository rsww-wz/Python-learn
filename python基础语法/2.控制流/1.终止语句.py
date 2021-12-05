"""
    break语句：
    用于条件语句和循环语句，遇到break跳出循环
    更多是用于while的无限循环中，
    可以设计while是无限循环语句，在代码块中用if语句和break语句结合跳出循环

"""
spam = 10
while True: 
    print(spam,end = ',')
    if spam <= 0:
        break
    else:
        spam -= 1

print('\n')

for i in range(0,10):
    print(i,end = ',')
    if i == 5:
        break
print('\n')

"""
continue语句
    作用：用于内部循环，如果程序遇到continue语句，就会马上跳回到循环开始处
    理解：结束本次循环，进入下一次循环(不会跳出循环)
"""  

for i in range(0,10):
    if i < 3 or i > 6:        #i == [0,1,2,7,8,9]
        continue
    else:                     #i == [3,4,5,6]
        print(i,end = ',')
print("\n")  

for i in range(0,50):
    if i % 2 == 0:            #如果是偶数，continue
        continue
    else:                     #打印奇数
        print(i,end = ',')

print('\n')

i = 0
while i < 50:
    i += 1
    if i % 2 == 0:
        continue
    else:
        print(i,end = ',')
