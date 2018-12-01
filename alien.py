import pygame
from pygame.sprite import Sprite


class Alien(Sprite):

    # 表示单个外星人的类
    def __init__(self, ai_settings, screen):
        # 初始化外星人及其起始位置
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载外星人图像，设置其rect属性
        alien_path = "./ufo.bmp"
        self.image = pygame.image.load(alien_path)
        self.rect = self.image.get_rect()

        # 每个外星人最初都在左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        # 在制定位置绘制外星人
        self.screen.blit(self.image, self.rect)
