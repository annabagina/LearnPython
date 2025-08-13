import random
import json

while True:

    try:
		with open("highscores.json", "r") as file:
		highscores = json.load(file)
	except FileNotFoundError:
		highscores = { "easy" : None, "middle" : None, "hard" : None }

	print("Выбери уровень сложности:")
	print("1 - Легкий (1-20, 10 попыток)")
	print("2 - Средний (1-50, 7 попыток)")
	print("3 - Сложный (1-100, 5 попыток)")

	levelChoice = input("Твой выбор:")

	if levelChoice == "1":
		max_num = 20
		max_attempts = 10
		level_name = "easy"
	elif levelChoice == "2":
		max_num = 50
		max_attempts = 7
		level_name = "middle"
	elif levelChoice == "3":
		max_num = 100
		max_attempts = 5
		level_name = "hard"
	else:
		print("Неверный ввод! Легкий уровень по умолчанию.")
		max_num = 20
		max_attempts = 10
		level_name = "easy"

	secret = random.randint(1, max_num) # Генерируем случайное число
	for attempt in range(1, max_attempts + 1):
		guess = int(input(f"Попытка {attempt}/{max_attempts}. Угадай число от 1 до {max_num}: "))          

		if guess < secret:
			print("Моё число больше!")
		elif guess > secret:
			print("Моё число меньше!")
		else:
			print(f"Поздравляю! Ты угадал за {attempt} попыток!")
			if highscores[level_name] is None or attempt < highscores[level_name]:
				highscores[level_name] = attempt
				with open("highscores.json", "w") as file:
					json.dump(highscores, file)
				print("Ты побил рекорд!")
			else:
				print(f"Лучший результат: {highscores}")
			break
	else:
		print(f"Ты проиграл! Моё число было {secret}")
        
	play_again = input("Сыграем ещё раз? (да/нет): ").lower()
	if play_again != "да":
		print("Спасибо за игру! До встречи 👋")
		break