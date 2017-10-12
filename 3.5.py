s=1
while True:
    a=int(input('введите число '))
    if a<0:
        s=s*a
    if a==0:
        break
print(s)
