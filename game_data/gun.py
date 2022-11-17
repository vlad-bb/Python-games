import pygame
from pygame.sprite import Sprite


class Gun(Sprite):
    def __init__(self, screen):
        '''ініціалізація гармати'''
        super(Gun, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('game_data/images/Gun.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.m_right = False
        self.m_left = False

    def output(self):
        '''малювання гармати'''
        self.screen.blit(self.image, self.rect)

    def update_gun(self):
        '''оновлення позиції пушки'''
        if self.m_right and self.rect.right < self.screen_rect.right:
            self.center += 4
        elif self.m_left and self.rect.left > 0:
            self.center -= 4
        self.rect.centerx = self.center

    def create_gun(self):
        '''розміщує нову гармату'''
        self.center = self.screen_rect.centerx
