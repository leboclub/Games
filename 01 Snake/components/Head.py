import pygame


class Head(pygame.sprite.Sprite):
    # 1、初始化方法
    # 主要用于定义一些类的属性
    def __init__(self):
        # 调用父级的初始化方法
        super().__init__()

        # 一个精灵类需要具备两个基本的属性，1、精灵的图形；2、精灵的图形的矩形框
        self.image = pygame.Surface((24, 24))
        self.image.fill((13, 63, 108))
        pygame.draw.rect(self.image, (18, 142, 255), (4, 4, 16, 16), 0)

        # 从图形获取图像的矩形框
        self.rect = self.image.get_rect()

        # 随机出现在网格中
        self.rect.topleft = 24 * 21, 24 * 12

        # 预设蛇头移动的方向
        self.heading = 'RIGHT'

    # 2、更新方法
    def update(self):
        if self.heading == 'RIGHT':
            self.rect = self.rect.move(24, 0)
        elif self.heading == 'LEFT':
            self.rect = self.rect.move(-24, 0)
        elif self.heading == 'UP':
            self.rect = self.rect.move(0, -24)
        elif self.heading == 'DOWN':
            self.rect = self.rect.move(0, 24)
