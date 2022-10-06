numbers = [1.1, 1.2, 3.1, 5, 10.01]

min = 1
max = 0
for i in numbers:
    if (i - int(i)) != 0:
        if (i - int(i)) <= min:
            min = i - int(i)
        if (i - int(i)) >= max:
            max = i - int(i)  
print(round(max-min, 2))