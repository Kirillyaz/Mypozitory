a = int(input())
a1=a//100
a2=a//10%10
a3=a%10
print(a1,a2,a3)
if a1==a2==a3:
    print('Все цифры одинаковы')
else:
    if(a1==a2) or (a2==a3) or (a1==a3):
        print('есть одинаковые')
    else:
        print('нет одинаковых')

