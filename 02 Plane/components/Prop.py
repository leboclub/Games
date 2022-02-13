import pygame
from random import randint


class Prop(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()

        paths = [
            r'assets/images/prop_type_0.png',
            r'assets/images/prop_type_1.png',
        ]
        self.type = randint(0, 1)
        self.image = pygame.image.load(paths[self.type])
        self.image = pygame.transform.scale(
            self.image,
            (self.image.get_width() // 2, self.image.get_height() // 2))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = pos
        self.speed = 1

    def update(self, current):
        self.rect = self.rect.move(0, self.speed)

        if self.rect.top > 800:
            self.kill()
