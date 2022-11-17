import os
import time

import pygame
import sys

from game_data.bullet import Bullet
from game_data.ork import Ork


def events(screen, gun, bullets):
    '''обробка події'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # праворуч
            if event.key == pygame.K_RIGHT:
                gun.m_right = True
            # ліворуч
            elif event.key == pygame.K_LEFT:
                gun.m_left = True
            elif event.key == pygame.K_UP:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            # праворуч
            if event.key == pygame.K_RIGHT:
                gun.m_right = False
            # ліворуч
            elif event.key == pygame.K_LEFT:
                gun.m_left = False


def update(bg_color, screen, stats, sc, gun, orks, bullets):
    '''оновлює екран'''
    screen.fill(bg_color)
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    orks.draw(screen)
    pygame.display.flip()


def update_bullets(screen, stats, sc, orks, bullets):
    '''оновлює позиції куль'''
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, orks, True, True)
    if collisions:
        for orks in collisions.values():
            stats.score += 1 * len(orks)
        stats.score += 1
        sc.image_score()
        check_high_score(stats, sc)
        sc.image_guns()
    if len(orks) == 0:
        bullets.empty()
        create_army(screen, orks)


def gun_kill(stats, screen, sc, gun, orks, bullets):
    '''зіткнення гармати і орків'''
    if stats.guns_left > 0:
        stats.guns_left -= 1
        sc.image_guns()
        orks.empty()
        bullets.empty()
        create_army(screen, orks)
        gun.create_gun()
        time.sleep(1)
    else:
        stats.run_game = False
        sys.exit()


def update_orks(stats, screen, sc, gun, orks, bullets):
    '''оновлює позиції орків'''
    orks.update()
    if pygame.sprite.spritecollideany(gun, orks):
        gun_kill(stats, screen, sc, gun, orks, bullets)
    orks_check(stats, screen, sc, gun, orks, bullets)


def orks_check(stats, screen, sc, gun, orks, bullets):
    '''перевірка, чи дісталися орки до края еркана'''
    screen_rect = screen.get_rect()
    for ork in orks.sprites():
        if ork.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, sc, gun, orks, bullets)
            break


def create_army(screen, orks):
    '''create army of orcs'''
    ork = Ork(screen)
    ork_width = ork.rect.width
    number_ork_x = int((800 - 2 * ork_width) / ork_width)
    ork_height = ork.rect.height
    number_ork_y = int((790 - 350 - ork_height) / ork_height)

    for row_number in range(number_ork_y):
        for ork_number in range(number_ork_x):
            ork = Ork(screen)
            ork.x = ork_width + (ork_width * ork_number)
            ork.y = ork_height + (ork_height * row_number)
            ork.rect.x = ork.x
            ork.rect.y = ork.rect.height + (ork.rect.height * row_number)
            orks.add(ork)


def check_high_score(stats, sc):
    '''перевірка нових рекордів'''
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()
        try:
            with open('game_data/images/high_score.txt', 'w') as f:
                f.write(str(stats.high_score))
        except FileNotFoundError:
            pass

