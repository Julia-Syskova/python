from random import randint

def take(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def answer(name, s, counter, candies):
    print(f"Ходил {name}, он взял {s}, теперь у него {counter}. Осталось на столе {candies} конфет.")

player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
candies = int(input("Введите количество конфет на столе: "))
flag = randint(0,2) # очередность
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0 
counter2 = 0

while candies > 28:
    if flag:
        s = take(player1)
        counter1 += s
        candies -= s
        flag = False
        answer(player1, s, counter1, candies)
    else:
        s = take(player2)
        counter2 += s
        candies -= s
        flag = True
        answer(player2, s, counter2, candies)

if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")