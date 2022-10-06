print('Введите число n')
num = int(input())
n = num
res = ''
while n != 0:
    res = str(n%2) + res
    n //= 2

print(f'Число {num} в двоичной системе это {res}')