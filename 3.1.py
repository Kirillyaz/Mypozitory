x=float
n=int(input())
s=0
t=0
i=0
if n<=0:
    print("n<=0")
else:
    for i in range(i,n+1):
        if i%2==0:
            t=x(2*i+1)/(2*i+1)
            s=s+t
        else:
            t=x*(2*1+1)/(2*i+1)
            s=s+t
        s=s+t
        print(s)
