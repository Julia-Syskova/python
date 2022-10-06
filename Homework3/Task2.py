print('Введите число n')
n = int(input())

from random import randint
numbers = []
for i in range(n):
    numbers.append(randint(0, 10))
print(numbers)

res = []
for i in range((len(numbers)+1)//2):
    res.append(numbers[i]*numbers[len(numbers)-1-i])
print(res)