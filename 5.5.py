import random
n=int(input('сколько строк:'))
m=int(input('сколько столбцов: '))
o=int(input('введите число: '))
s=[]
a=0
for i in range(n):
    s.append([])
    for j in range(m):
        k=random.randint(0,10)
        s[i].append(k)
        if o==k:
            a=a+1
for i in range(n):
    print(s[i])
print('чисес равных ',o,':',a)

