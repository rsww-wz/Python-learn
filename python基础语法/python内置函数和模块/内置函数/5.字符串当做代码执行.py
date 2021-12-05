# eval():可以把字符串当做代码来执行,有返回值
# exec()：也是吧字符串当做代码量执行，但是没有返回值


# 尽量别使用这些函数，因为不安全，不知道字符串里面的可以是什么，他们可以是任何东西

spam = "1 + 1"
a = eval(spam)
print(a)

spam1 = "['张无忌','张翠山','张三丰']"
print(type(spam1))
r = eval(spam1)
print(r,type(r))