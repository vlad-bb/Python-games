from random import choice
import colorama
import os
import time
import socket

colorama.init()

ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'

OPTIONS = [ROCK, SCISSORS, PAPER]
MAPPING = {
	ROCK: SCISSORS,
	SCISSORS: PAPER,
	PAPER: ROCK
}

counter_pl = 0
counter_ai = 0
first_switch = False
give_up = False


def get_winner(user_val, computer_val):
	global counter_ai, counter_pl
	if user_val == computer_val:
		even = ['[Ничья, просто, чтобы ты не расстраивался.]', '[Ничья, потому что мне тебя жаль.]',
		        '[Ничья. Ничья? Да ладно.]', '[Как долго ты будешь пытаться победить? Не важно. Ничья.]',
		        '[Ничья.]']
		print(choice(even))
	elif MAPPING[user_val] == computer_val:
		user_win_phrase = ["[Везение -- это миф. Просто я разрешил тебе выиграть.]", "[Только не пускайся в пляс.]",
		                   "[Я вижу эту наивную радость в твоих глазах.]",
		                   "[В этот раз дарую тебе эту маленькую победу.]", "[Всё идёт согласно МОЕМУ плану.]"]
		counter_pl += 1
		print(choice(user_win_phrase))
		time.sleep(1)
	else:
		robot_win_phrase = ["[Я вычислил этот исход ещё до твоего рождения.]", "[Ты всерьёз надеялся меня обыграть?]",
		                    "[1000001101110001000011100001101111000011010110001000000 - это ты, на моём языке.]",
		                    "[Как ничтожны твои попытки что-то предпринять.]", "[Совершенно очевидная победа.]"]
		counter_ai += 1
		print(choice(robot_win_phrase))
		time.sleep(0.5)


def get_absolute_winner(player, computer):
	global first_switch, counter_pl, counter_ai, give_up
	if counter_pl == 3:
		time.sleep(1)
		print('\n[Что ж, ты выиграл...]')
		time.sleep(1)
		print('\033[3m[..."чемпион\033[0m".]')
		time.sleep(1.5)
		print('\033[1m[Чемпион среди жуликов\033[0m.]')
		time.sleep(1.5)
		print('\033[2m[Но в следующий раз фортуна тебе уже не улыбнётся.\033[0m]')
		time.sleep(1.5)
		print("\n \n(≖_≖ )")
		time.sleep(4)
		counter_pl, counter_ai = 0, 0
		first_switch = False
	elif counter_ai == 3:
		print(f'[Победа досталась {socket.gethostname()}! Впрочем, ничего удивительного.]')
		time.sleep(0.8)
		print('Желаете...')
		time.sleep(1)
		print('\033[1m...eщё больше...\033[0m')
		time.sleep(1.2)
		print('\033[1;31m...УНИЗИТЬ СЕБЯ?\033[0m')
		time.sleep(4)
		counter_pl, counter_ai = 0, 0
		first_switch = False
		are_you = input(
			"Вы готовы вновь бросить вызов этой непобедимой машине?\nОтвет 'y' - отправит вас в цикл попыток и стенаний.\nОтвет 'n' - освободит от бремени сражения с бездушной железкой. \n")
		if are_you == 'n':
			time.sleep(1)
			print('Слабак. Нюня. Фу.')
			time.sleep(2)
			give_up = True
		else:
			print('Да будет так, храбрец.')
	else:
		print(f"Ваш счёт: {counter_pl}.")
		print(f"Счёт вашего непревзойдённого противника: {counter_ai}.")


# def validate_input(user_val):
# 	return user_val in OPTIONS


def main():
	global first_switch
	while True:
		if give_up:
			break
		if not first_switch:
			os.system('cls' if os.name == 'nt' else 'clear')
			print("-----\nДобро пожаловать в игру 'КАМЕНЬ-НОЖНИЦЫ-БУМАГА'!")
			attention = input(
				"Вашим противником станет высокоразвитый искусственный интеллект.\n\033[1;35;5mНажмите Enter\033[0m")
			os.system('cls' if os.name == 'nt' else 'clear')
			print("\033[F \033[1;31m    [0|-|0]    \033[0m    ")
			first_switch = True
		print("-----\nИгра ведётся до трёх побед.")
		user_val = input(
			f"Введите одно из значений: {', '.join(OPTIONS)} \nГде {OPTIONS[0]} - камень, {OPTIONS[1]} - ножницы, {OPTIONS[2]} - бумага.\n")
		user_val = user_val.lower()
		if user_val == 'r':
			time.sleep(0.3)
			print("Твой выбор пал на камень.")
		elif user_val == 's':
			time.sleep(0.3)
			print("Надеясь на удачу и только, ты выбираешь ножницы.")
		elif user_val == 'p':
			time.sleep(0.3)
			print("Ты выбираешь бумагу, так как отчаяние охватило тебя.")

		if user_val not in OPTIONS:
			print("Неправильное значение. Как и ожидалось. Попробуй ещё раз.\n")
			continue
		computer_val = choice(OPTIONS)
		meaning = {'r': 'камень', 's': 'ножницы', 'p': 'бумага'}
		time.sleep(1)
		print(f"Выбор превосходящего тебя во всём противника -- {meaning[computer_val]}.")
		time.sleep(2)
		get_winner(user_val, computer_val)
		get_absolute_winner(counter_pl, counter_ai)
		time.sleep(2)


if __name__ == '__main__':
	main()
