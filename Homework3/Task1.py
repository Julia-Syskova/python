print('Введите число n')
n = int(input())

from random import randint
numbers = []
for i in range(n):
    numbers.append(randint(0, 10))
print(numbers)

def sum(list):
    s = 0
    for i in range(len(list)):
        if i % 2 != 0:
            s += list[i]
    print(f"Сумма равна: {s}")
sum(numbers)
