n = input('Введите число\n')
sum = 0

for i in n:
    if i != '.':
        sum = sum + int(i)
print(sum)