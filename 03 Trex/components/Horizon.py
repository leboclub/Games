import pygame
from random import choice

class Horizon(pygame.sprite.Sprite):
    def __init__(self, sprite, **config):
        super().__init__()

        self.images = []

        for col in range(2):
            self.images.append(sprite.subsurface(
                (4 + 1200 * col, 108), (1200, 28)))

        # 初始化图片
        self.image_0 = choice(self.images)
        self.image_1 = choice(self.images)

        # 初始化矩形框
        self.rect_0 = self.image_0.get_rect()
        self.rect_0 = self.image_0.get_rect()
        self.rect_0.bottomleft = 0, 280
        
        self.rect_1 = self.image_1.get_rect()
        self.rect_1 = self.image_1.get_rect()
        self.rect_1.bottomleft = 1200, 280

        self.speed = -10

    def update(self):
        self.rect_0 = self.rect_0.move([self.speed, 0])
        self.rect_1 = self.rect_1.move([self.speed, 0])

        if self.rect_0.right <= 0:
            self.rect_0.left = 1200
            self.image_0 = choice(self.images)

        if self.rect_1.right <= 0:
            self.rect_1.left = 1200
            self.image_1 = choice(self.images)

    def draw(self, surface):
        surface.blit(self.image_0, self.rect_0)
        surface.blit(self.image_1, self.rect_1)
