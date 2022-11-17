from game_data import controls
import pygame
from pygame.sprite import Group

from game_data.gun import Gun
from game_data.scores import Scores
from game_data.statistic import Stats


def run():
    pygame.init()
    screen = pygame.display.set_mode((800, 790))
    pygame.display.set_caption('Armed Forces of Ukraine against russian orcs')
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    orks = Group()
    controls.create_army(screen, orks)
    stats = Stats()
    sc = Scores(screen, stats)

    while True:
        controls.events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun()
            controls.update(bg_color, screen, stats, sc, gun, orks, bullets)
            controls.update_bullets(screen, stats, sc, orks, bullets)
            controls.update_orks(stats, screen, sc, gun, orks, bullets)


if __name__ == '__main__':
    run()
