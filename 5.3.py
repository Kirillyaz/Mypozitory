import random 
s=[]
a=0

while a<=11:
    b=random.randint(0,7)
    if b==0:
        n='0'
    else:
        n=''
    while b > 0: 
        y = str(b % 2)
        n = y + n
        b = int(b / 2)
    s.append(int(n))
    a=a+1
print(s)
n=11
i=0
while True:
    if s.count(s[i])>2:
        print(i,s[i])
        s.remove(s[i])
        n=n-1
    else:
        i=i+1
    if i>=n:
        break
print(s)

