import pygame

class Ship():

    def __init__(self, screen):
        ship_path = './spaceship.bmp'
        # 初始化飞船并设置其初始位置
        self.screen = screen

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load(ship_path)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)
