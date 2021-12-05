# enumerate()

lst = ["你","好","我","是","rs"]

for i in range(len(lst)):
    print(i,lst[i])
print('\n')

for i,j in enumerate(lst):
    print(i,j)
print('\n')

for i,j in enumerate(lst,10):
    print(i,j)