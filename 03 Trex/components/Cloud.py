import pygame
from random import choice, randint

class Cloud(pygame.sprite.Sprite):
    def __init__(self, sprite, is_first=False, **config):
        super().__init__()

        self.images = []
        for col in range(1):
            self.images.append(sprite.subsurface(
                (174 + 92 * col, 4), (92, 28)))

        # 初始化图片
        self.image = choice(self.images)
        self.rect = self.image.get_rect()
        if is_first:
            self.rect.left = randint(0, 1200)
        else:
            self.rect.left = 1200
        self.rect.bottom = randint(88, 170)
        self.speed = -2

    def update(self):
        self.rect = self.rect.move(self.speed, 0)
        
        if self.rect.right < 0:
            self.kill()
            