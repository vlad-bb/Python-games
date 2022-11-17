import pygame.font
from game_data.gun import Gun
from pygame.sprite import Group


class Scores():
    '''виведення ціфрової інофрмації'''

    def __init__(self, screen, stats):
        '''ініціалізація підрахунку очків'''
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.colour = (63, 73, 204)
        self.font = pygame.font.SysFont(None, 36)
        self.image_score()
        self.image_high_score()
        self.image_guns()

    def image_score(self):
        '''графіка рахунку'''
        self.score_img = self.font.render(str(self.stats.score), True, self.colour, (0, 0, 0))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def image_high_score(self):
        '''перетворює рекорд в графічне зображення'''
        self.high_score_image = self.font.render(str(self.stats.high_score), True, self.colour, (0, 0, 0))
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top + 20
        self.image = pygame.image.load('game_data/images/pixil-frame-0.png')
        self.rect = self.image.get_rect()
        self.rect.x = 600
        self.rect.y = 20

    def image_guns(self):
        '''каялькість життів'''
        self.guns = Group()
        for gun_number in range(self.stats.guns_left):
            gun = Gun(self.screen)
            gun.rect.x = 15 + gun_number * gun.rect.width
            gun.rect.y = 20
            self.guns.add(gun)

    def show_score(self):
        '''виведення рахунку на екран'''
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.guns.draw(self.screen)
