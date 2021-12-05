import time

#while循环
def isprime(x):
    prime = []
    for number in range(2,x + 1):
        i = 2
        while i < number ** 0.5:
            if number % i == 0:
                break
            i += 1
        else:
            prime.append(number)
    return prime

#for循环
def isprime1(x):
    prime = []
    for number in range(2,x + 1):
        for x in range(2,int(number ** 0.5) + 1):
            if number % x == 0:
                break
        else:
            prime.append(number)
    return prime

#for循环-优化
def isprime2(x):
    prime = [2]
    for number in range(3,x + 1,2):
        for x in range(2,int(number ** 0.5) + 1):
            if number % x == 0:
                break
        else:
            prime.append(number)
    return prime

t1 = time.time()
temp = isprime2(1000000)
#print(temp)
t2 = time.time()
spacetime = t2 - t1
print(spacetime)
