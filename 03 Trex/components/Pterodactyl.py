import pygame
from random import *

class Pterodactyl(pygame.sprite.Sprite):
    def __init__(self, sprite, **config):
        super().__init__()

        self.images = []
        for col in range(2):
            self.images.append(sprite.subsurface(
                (268 + 92 * col, 4), (92, 80)))

        # 初始化图片
        self.image_idx = 0
        self.image = self.images[self.image_idx]
        # self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = choice(((1200, 280), (1200, 230), (1200, 180)))
        self.msPerFrame = 1000 / 6
        self.last_time = 0
        self.speed = -12

    def update(self, current_time):
        if current_time > self.last_time + self.msPerFrame:
            self.image_idx = (self.image_idx + 1) % len(self.images)
            self.last_time = current_time
        self.image = self.images[self.image_idx]
        self.mask = pygame.mask.from_surface(self.image).scale((92, 70))

        self.rect = self.rect.move([self.speed, 0])
        if self.rect.right < 0:
            self.kill()