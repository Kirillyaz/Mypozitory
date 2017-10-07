m=int(input())
n=int(input())
s=0
while m<=n:
    if m%2==1:
        s=s+m**2

    m+=1
print(s)
