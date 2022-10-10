seq = list(map(int, input("Введите числа через пробел:\n").split()))
print(f"Исходная последовательность: {seq}")
new_seq = []
for i in seq:
    if i not in new_seq:
        new_seq.append(i)
        
print(f"Список из неповторяющихся элементов: {new_seq}")