import random
list = [18.03, 'осень', 307, 'питон']
print(list)

n = len(list)
for i in range(n):
    j = random.randint(0, n-1)
    list[i], list[j] = list[j], list[i]
print(list)