import math
a=1
s=0
x=int(input('х='))
n=int(input('сколько раз? '))
while a<=n:
    s=s+((a*2+1)*x**(a*2))/math.factorial(a)
    a=a+1
print(s)
