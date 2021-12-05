import time
import numpy as np

#for循环
def f1(x):
    for i in range(0,x,2):
        pass

#while循环
def f2(x):
    i = 0
    while i < x:
        i += 2

#numpy数组-for
def f3(x):
    for i in np.arange(0,x,2):
        pass

t1 = time.time()
f1(1000000)
t2 = time.time()
print(t2 - t1)


t3 = time.time()
f2(1000000)
t4 = time.time()
print(t4 - t3)

t5 = time.time()
f3(1000000)
t6 = time.time()
print(t6 - t5)

