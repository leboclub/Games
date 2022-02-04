import pygame
from random import randint


class Apple(pygame.sprite.Sprite):
    # 1、初始化方法
    # 主要用于定义一些类的属性
    def __init__(self, group):
        # 调用父级的初始化方法
        super().__init__()

        # 一个精灵类需要具备两个基本的属性，1、精灵的图形；2、精灵的图形的矩形框
        self.image = pygame.Surface((24, 24))
        self.image.fill((99, 10, 11))
        pygame.draw.rect(self.image, (231, 2, 14), (4, 4, 16, 16), 0)

        # 从图形获取图像的矩形框
        self.rect = self.image.get_rect()

        # 随机出现在网格中
        self.rect.topleft = randint(0, 39) * 24, randint(0, 24) * 24
        
        # 添加到组内
        self.add(group)
