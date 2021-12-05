# range()函数
# iter()函数 : 生成器
# next()函数 ：迭代访问下一个元素，如果没有元素会报错

lst = [11,22,33]

spam = lst.__iter__()
print(spam.__next__())
print(spam.__next__())
print(spam.__next__())
print('\n')

spam = iter(lst)
print(next(spam))
print(next(spam))
print(next(spam))