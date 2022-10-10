num = int(input("Введите число: "))
i = 2 
mul = []
while i <= num:
    if num % i == 0:
        mul.append(i)
        num //= i 
    else:
        i += 1
print(f"Простые множители числа: {mul}")