import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button


def run_game():
    # 初始化pygame、设置、屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Aline Invasion")

    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")
    # 创建一艘飞船、存储子弹数量的编组、外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)

    # 游戏主循环
    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.check_collosion(bullets, aliens)
            gf.update_bullets(bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, stats, screen, ship,
                         aliens, bullets, play_button)


run_game()
