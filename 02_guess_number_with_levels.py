# Info:

# Компьютер загадывает число.

# Игрок вводит числа через input().

# Программа подсказывает, больше или меньше число.

# Игрок выбирает уровень сложности — от лёгкого до сложного.

# Есть ограничение по количеству попыток.

# Диапазон чисел меняется в зависимости от уровня.

import random

print("Выберите уровень сложности:")
print("1 — Легко (1-20, 10 попыток)")
print("2 — Средне (1-50, 7 попыток)")
print("3 — Сложно (1-100, 5 попыток)")

level = input("Введите 1, 2 или 3: ")

if level == "1":
    max_number = 20
    max_attempts = 10
elif level == "2":
    max_number = 50
    max_attempts = 7
elif level == "3":
    max_number = 100
    max_attempts = 5
else:
    print("Неверный ввод, выбран уровень Легко по умолчанию.")
    max_number = 20
    max_attempts = 10

secret = random.randint(1, max_number)
attempts = 0
guess = None

while guess != secret and attempts < max_attempts:
    guess = int(input(f"Угадайте число от 1 до {max_number}: "))
    attempts += 1

    if guess < secret:
        print("Моё число больше!")
    elif guess > secret:
        print("Моё число меньше!")
    else:
        print(f"Поздравляем! Вы угадали за {attempts} попыток!")

if guess != secret:
    print(f"Вы проиграли. Моё число было {secret}.")
