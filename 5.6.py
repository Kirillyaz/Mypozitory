import random
n=int(input('сколько строк:'))
m=int(input('сколько столбцов: '))
s=[]
for i in range(n):
    a=0 #для наибольшего
    b=10 #для наименьшего
    s.append([])
    for j in range(m):
        k=random.randint(0,10)
        s[i].append(k)
        if k<b:
            b=k
        if k>a:
            a=k
    print('наибольшее в строке',i+1,':',a)
    print('наименьшее в строке',i+1,':',b)
for i in range(n):
    print(s[i])
