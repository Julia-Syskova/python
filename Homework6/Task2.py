#seq = input("Введите числа через пробел:\n")
#print(f"Исходный список: {seq}")
# 
# def unique(seq):
#    res = []
#    for char in seq:
#        if seq.count(char) < 2:
#            res.append(char)
#    return res
#print(unique(seq))

seq = list(map(int, input("Введите числа через пробел:\n").split()))
print(f"Исходный список: {seq}")
res = []
[res.append(i) for i in seq if seq.count(i) < 2]
print(f"Список из неповторяющихся элементов: {res}")