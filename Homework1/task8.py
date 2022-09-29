from cmath import sqrt


print('Введите координаты точки А')
x1 = float(input())
y1 = float(input())
print('Введите координаты точки B')
x2 = float(input())
y2 = float(input())

res = round(((((x2-x1)**2)+((y2-y1)**2))**0.5), 2)
print(res)