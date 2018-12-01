import sys
import pygame


def check_events(ship):
    # 监视键鼠事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # 按住键盘则持续移动
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            chek_keyup_events(event, ship)


def check_keydown_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True


def chek_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, ship):
    # 每次循环都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # 让最近绘制的屏幕可见
    pygame.display.flip()
