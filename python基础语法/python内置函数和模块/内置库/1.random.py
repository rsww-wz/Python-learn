import random

# random.random():随机一个0-1内小数，取不到0和1
# random.randint():随机范围整数,能取到边界
# random.uniform()：随机范围小数
# random.choice(lst):随机选择一个元素,不可以随机字典和集合
# random.sample(lst,number):随机固定数量元素,返回一个列表

#print(dir(random))

# print(help(random.randrange))

spam = random.random()
spam1 = random.randint(1,10)
spam2 = random.uniform(1,10)
print(spam)
print(spam1)
print(spam2)

lst = [1,25,6,3,73,532,26]
tup = (5,7,2,3,7,34,32)
str1 = "hello world"
dict1 = dict(zip(str1,lst))
set1= {1,435,6,234,2,6,714,35}

print(random.choice(lst))
print(random.choice(tup))
print(random.choice(str1))
print(random.sample(lst,2))
print(random.sample(str1,2))

# 练习：随机验证码
def randInt():
    return str(random.randint(0,10))

def randupper():
    return chr(random.randint(65,90))

def randlower():
    return chr(random.randint(97,122))

# 生成验证码方法一
def randcode(n = 4):
    lst = []
    for i in range(n):
        which = random.randint(1,3)
        if which == 1:
            s = randInt()
        elif which == 2:
            s = randupper()
        elif which == 3:
            s = randlower()
        lst.append(s)
    return "".join(lst)

# 生成验证码方法二
lst = [randInt,randlower,randupper]
def randcode1():
    lst1 = []
    for i in range(4):
        code = random.choice(lst)
        code1 = code()
        lst1.append(code1)
    return "".join(lst1)


print(randcode())
print(randcode1())

