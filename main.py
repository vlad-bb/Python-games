from rsp.R_P_S import main as rsp
from orcodav.main import run
from snake_game.main import main as snake_run
from turtle_race.main import main as turtle_run


# main функція проекту
def main():
    while True:
        print(
              '1. ROCK-SCISSORS-PAPER',
              '2. Orcodav',
              '3. Snake',
              '4. Turtle Race',
              '5. Close program', sep='\n')
        user_command = input('Press menu button: >>> ')
        if user_command == '1':
            print('*' * 60, 'ROCK-SCISSORS-PAPER', '*' * 60, sep='\n')
            result = rsp()
            if result == 'Exit':
                continue

        elif user_command == '2':
            print('*' * 60, 'Orcodav Game', '*' * 60, sep='\n')
            result = run()
            if result == 'Exit':
                continue

        elif user_command == '3':
            print('*'*60, 'Snake Game', '*'*60, sep='\n')
            result = snake_run()
            if result == 'Exit':
                continue

        elif user_command == '4':
            print('*'*60, 'Turtle Race', '*'*60, sep='\n')
            result = turtle_run()
            if result == 'Exit':
                continue

        elif user_command == '5':
            print('Good bye!')
            break


if __name__ == '__main__':
    main()
