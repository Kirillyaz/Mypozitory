import random
n=int(input('сколько строк:'))
m=int(input('сколько столбцов: '))
s=[]
a=0
b=0
for i in range(n):
    for j in range(m):
        k=random.randint(0,20)
        s.append(k)
        if k%2==1:
            a=a+1
        else:
            b=b+1
print(s)
print('нечет ',a)
print('чет ',b)
