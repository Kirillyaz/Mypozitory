import random
s=[]
s2=[]
a=0
while a<=8:
    b=random.randint(10,99)
    x=b//10
    y=b%10
    s.append(b)
    s2.append(x+y)
    a=a+1
print(s)
print(s2)

