def f1(x):
    x **= 3
    return x

spam = [f1(x) for x in range(10)] 
print(spam)