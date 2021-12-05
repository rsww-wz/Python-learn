# 进制转换
spam = 27

print(bin(spam))
print(oct(spam))
print(hex(spam))

# 运算相关

# 绝对值:abs
a = -14
print(abs(a))

# divmod(被除数，除数)
# 返回值：商，余数,元素类型

a = 21
print(divmod(a,4))

# round()：四舍五入
b = 3.1415926
r1 = round(b)
r2 = round(b,3)
print(r1)
print(r2)

# pow():
print(pow(2,5))

#sun()
#min
#max
lst = [1,2,4,5,6,7,7,8]
print(sum(lst))
print(min(lst))
print(max(lst))