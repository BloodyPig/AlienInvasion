import sys
import pygame
from bullet import Bullet
from alien import Alien


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    # 右移
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    # 左移
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    # 空格开火
    elif event.key == pygame.K_SPACE or event.key == pygame.K_KP_ENTER:
        fire_bullet(ai_settings, screen, ship, bullets)


def chek_keyup_events(event, ship):
    # 停止右移
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    # 停止左移
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    # 监视键鼠事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # 按住键盘则持续移动
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            chek_keyup_events(event, ship)


def update_bullets(bullets):
    bullets.update()
    # 删除已经消失的子弹
    # 使用 bullet.copy()报错
    # for bullet in bullets.copy():
    for bullet in bullets:
        if bullet.rect.bottom <= 0:
            # remove 函数报错
            # bullets.remove(bullet)
            bullets.remove_internal(bullet)
    # print(len(bullets)) # 设置的查看是否正确消失的标志


def get_number_aliens_x(ai_settings, alien_width):
    # 计算每行可容纳多少外星人
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_alien_x = int(available_space_x / (2 * alien_width))
    return number_alien_x


def get_number_rows(ai_settings, ship_height, alien_height):
    # 计算可容纳多少行外星人
    available_space_y = ai_settings.screen_height - \
        (3*alien_height) - ship_height
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    # 创建一个外星人并放在当前行
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add_internal(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    # 创建外星人群
    # 创建一个外星人并计算每行可容纳多少外星人
    alien = Alien(ai_settings, screen)
    number_alien_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(
        ai_settings, ship.rect.height, alien.rect.height)
    # 创建第一行外星人
    for row_number in range(number_rows):
        for alien_number in range(number_alien_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def fire_bullet(ai_settings, screen, ship, bullets):
    # 发射子弹
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        # add函数报错
        # bullets.add(new_bullet)
        bullets.add_internal(new_bullet)


def update_screen(ai_settings, screen, ship, aliens, bullets):
    # 每次循环都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    aliens.draw(screen)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # 让最近绘制的屏幕可见
    pygame.display.flip()
