class Stats():
    '''відслідує статистику'''

    def __init__(self):
        '''ініциалізує статистику'''
        self.reset_stats()
        self.run_game = True
        counter = 0
        try:
            with open('game_data/images/high_score.txt', 'r') as f:
                self.high_score = int(f.readline())
        except FileNotFoundError:
            counter += 1
            self.high_score = counter

    def reset_stats(self):
        '''статитика, яка змінюється під час гри'''
        self.guns_left = 2
        self.score = 0
