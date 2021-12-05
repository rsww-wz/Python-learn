#字符串也是不可变的数据类型

#索引
spam = "Good morning"
print(spam[8])

#切片
spam1 = "hello world"
temper = spam[2:7]
temper1 = spam[len(spam)::-2]
print(temper)
print(type(temper))
print(temper1)

#遍历
for i in spam1:
    print(i,end = ',')
print('\n')

for i in range(len(spam1)):
    print(spam1[i],end = ',')

#运算
string = 'Good'
string1 = "morning"
temp = string + string1
print(temp)
temp1 = string * 2
print(temp1)