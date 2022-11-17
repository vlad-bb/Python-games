import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gun):
        '''створиємо кулю в позиції пушки'''
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 15, 15)
        self.colour = (63, 73, 204)
        self.speed = 4.5
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        '''переміщення кулі до гори'''
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        '''малюємо кулю на екрані'''
        pygame.draw.rect(self.screen, self.colour, self.rect)
