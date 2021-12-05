import re
import pprint
import matplotlib.pyplot as plt

lst = []
address = r"E:\0-code\Pycharm\Python应用\单词.txt"
with open(address, "r", encoding="gbk") as fp:
    for i in range(1,20200):
        spam = fp.readline()
        lst.append(spam)

string = str(lst)

# 后缀
r1 = re.findall(r"[\w]+able\\n", string)
r2 = re.findall(r"[\w]+tion\\n", string)
r3 = re.findall(r"[\w]+ly\\n", string)
r4 = re.findall(r"[\w]+ing\\n", string)
r5 = re.findall(r"[\w]+ed\\n", string)
r6 = re.findall(r"[\w]+ate\\n", string)
r7 = re.findall(r"[\w]+er\\n", string)
r8 = re.findall(r"[\w]+ous\\n", string)
r9 = re.findall(r"[\w]+ive\\n", string)
r10 = re.findall(r"[\w]+ent\\n", string)
r11 = re.findall(r"[\w]+ence\\n", string)
r12 = re.findall(r"[\w]+ment\\n", string)
r13 = re.findall(r"[\w]+ful\\n", string)
r14 = re.findall(r"[\w]+ant\\n", string)
r15 = re.findall(r"[\w]+or\\n", string)
r16 = re.findall(r"[\w]+al\\n", string)

# 前缀
p1 = re.findall(r"un[\w]+\\n", string)
p2 = re.findall(r"dis[\w]+\\n", string)
p3 = re.findall(r"mis[\w]+\\n", string)
p4 = re.findall(r"com[\w]+\\n", string)
p5 = re.findall(r"con[\w]+\\n", string)
p6 = re.findall(r"pro[\w]+\\n", string)
p7 = re.findall(r"pre[\w]+\\n", string)
p8 = re.findall(r"re[\w]+\\n", string)
p9 = re.findall(r"ex[\w]+\\n", string)
p10 = re.findall(r"de[\w]+\\n", string)
p11 = re.findall(r"under[\w]+\\n", string)
p12 = re.findall(r"inter[\w]+\\n", string)

# print(len(r1), r1)
# print(len(r2), r2)
# print(len(r3), r3)
# print(len(r4), r4)
# print(len(r5), r5)
# print(len(r6), r6)
# print(len(r7), r7)
# print(len(r8), r8)
# print(len(r9), r9)
# print(len(r10), r10)
# print(len(r11), r11)
# print(len(r12), r12)
# print(len(r13), r13)
# print(len(r14), r14)
# print(len(r15), r15)
# print(len(r16), r16)

leng = 0
post = ["able","tion","ly","ing","ed","ate","er","ous","ive","ent","ence","ment","ful","ant","or","al"]
last = []
for i in range(1,17):
    length = eval("r{}".format(i))
    length = len(length)
    last.append(length)
    leng = leng + length
# print(leng)

dic1 = dict(zip(post,last))
# print('\n')


# print(len(p1), p1)
# print(len(p2), p2)
# print(len(p3), p3)
# print(len(p4), p4)
# print(len(p5), p5)
# print(len(p6), p6)
# print(len(p7), p7)
# print(len(p8), p8)
# print(len(p9), p9)
# print(len(p10), p10)
# print(len(p11), p11)
# print(len(p12), p12)

leng = 0
fore = ["un","dis","mis","com","con","pro","pre","re","ex","de","under","inder"]
ex = []
for i in range(1,13):
    length = eval("p{}".format(i))
    length = len(length)
    ex.append(length)
    leng = leng + length
# print(leng)

dic = dict(zip(fore,ex))
print(dic1)
print(dic)


# lst1 = []
# for i in range(1,14):
#     spam = eval("r{}".format(i))
#     lst1.append(spam)
# print(len(lst1))
# print(lst1)
# pprint.pprint(lst1)


plt.style.use('seaborn-whitegrid')

plt.figure(num = "ex")
x = fore
y = ex
plt.bar(x,y,width = 0.5,alpha = 0.5,color = 'red',edgecolor = 'black',label = "前")
plt.legend()

plt.figure(num = "post")
x1 = post
y1 = last
plt.bar(x1,y1,width = 0.5,alpha = 0.5,color = 'blue',edgecolor = 'black',label = "后")
plt.legend()

plt.show()