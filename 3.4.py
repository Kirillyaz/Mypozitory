m=int(input('введите M '))
a=100
while a<=1000:
    if (a/100)%5==0:
        s=((a/100)**(a/100))/m
        print(s)
    a=a+100

