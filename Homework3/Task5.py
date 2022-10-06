print('Введите число n')
n = int(input())

def fibonachi(n):
    fnums = []
    a, b = 1, 1
    for i in range(n):
        fnums.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (n+1):
        fnums.insert(0, a)
        a, b = b, a - b
    return fnums

fnums = fibonachi(n)
print(fibonachi(n))