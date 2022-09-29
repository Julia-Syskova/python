print('Введите число')
n = int(input())
a = n%5
b = n%10
c = n%15
d = n%30
if ((a==0)and (b==0) or (c==0) and (d !=0)):
 print('Число кратно')
else:
 print('Не кратно')