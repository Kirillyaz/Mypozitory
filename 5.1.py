import random
a=0
b=0 
s=[]
g=0
n=0
while a<=13:
    b=random.randint(0,10) #рандомим число от 0 до 10 вкл
    s.append(b)
    if (s[a]>0) and (s[a]%2==0):
        g=g+int(s[a])
        n=n+1
    a=a+1
print(s)
print("сумма и кол-во=",g,n)

