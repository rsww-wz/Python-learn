import time
import random

def wrapper(func):
    def inner(*args):
        t1 = time.time()
        func(*args)
        t2 = time.time()
        print(t2 - t1)
    return inner

@wrapper
def f1(x):
    lst = list(range(x))
    random.shuffle(lst)

f1(10000)