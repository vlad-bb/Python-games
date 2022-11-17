import pygame


class Ork(pygame.sprite.Sprite):
    '''клас одного орка'''
    def __init__(self, screen):
        '''ініціалізіруєм та задаємо начальну позицію'''
        super(Ork, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('game_data/images/pixil-frame-0.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        '''bring out the ork in the screen'''
        self.screen.blit(self.image, self.rect)

    def update(self):
        '''переміщує орків'''
        self.y += 0.5
        self.rect.y = self.y
