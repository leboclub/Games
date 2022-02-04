import pygame
from random import choice

class Cactus(pygame.sprite.Sprite):
    def __init__(self, sprite):
        super().__init__()

        self.images = []
        self.images.append(sprite.subsurface((456, 4), (34, 70)))
        self.images.append(sprite.subsurface((490, 4), (68, 70)))
        self.images.append(sprite.subsurface((558, 4), (102, 70)))
        self.images.append(sprite.subsurface((664, 4), (50, 100)))
        self.images.append(sprite.subsurface((714, 4), (100, 100)))
        self.images.append(sprite.subsurface((814, 4), (150, 100)))

        self.image = choice(self.images)
        self.image.set_colorkey((255, 255, 255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.bottomleft = 1200, 280
        self.speed = -10

    def update(self):
        self.rect = self.rect.move(self.speed, 0)
        
        if self.rect.right < 0:
            self.kill()
            