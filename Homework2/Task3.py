n = int(input('Введите число\n'))
sum = 0

for i in range(1, n+1):
    sum = sum + ((1+1/n)**n)
print(round(sum, 4))