import sys
import pygame


def run_game():
    # 初始化游戏 创建屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Aline Invasion")

    # 设置背景色
    bg_color = (230, 230, 230)

    # 游戏主循环
    while True:

        # 监视键鼠事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # 每次循环都绘制背景色
        screen.fill(bg_color)

        # 让最近绘制的屏幕可见
        pygame.display.flip()


run_game()
