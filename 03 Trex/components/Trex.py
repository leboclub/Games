import pygame
from random import choice

class Trex(pygame.sprite.Sprite):
    def __init__(self, sprite):
        pygame.sprite.Sprite.__init__(self)
        
        # 导入所有图片
        self.images = []
        for col in range(6):
            self.images.append(sprite.subsurface(
                (1696 + 88 * col, 4), (88, 94)))
        for col in range(2):
            self.images.append(sprite.subsurface(
                (2224 + 118 * col, 38), (118, 60)))

        self.image_idx = 0
        self.image = self.images[self.image_idx]
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.bottom = 50, 280
        # self.image.set_colorkey((255, 255, 255))
        self.mask = pygame.mask.from_surface(self.image)

        
        self.init_position = 50, 280
        self.fps = 6
        self.refresh_counter = 0
        self.speed = -18
        self.gravity = 0.88
        self.is_jumping = False
        self.is_ducking = False
        self.is_crashed = False
        self.movement = [0, 0]

    def jump(self, sound):
        if self.is_crashed or self.is_jumping:
            return
        sound.play()
        self.is_jumping = True
        self.movement[1] = self.speed

    def duck(self):
        if self.is_crashed or self.is_jumping:
            return
        self.is_ducking = True

    def run(self):
        self.is_ducking = False

    def crashed(self, sound):
        if self.is_crashed:
            return
        sound.play()
        self.is_crashed = True
    
    # 载入当前状态的图片
    def loadImage(self):
        self.image = self.images[self.image_idx]
        rect = self.image.get_rect()
        rect.left, rect.bottom = self.rect.left, self.rect.bottom
        self.rect = rect
        self.mask = pygame.mask.from_surface(self.image)

    # 更新小恐龙
    def update(self, current_time):
        if self.is_crashed:
            self.image_idx = 5
            self.loadImage()
            return

        if self.is_jumping:
            self.movement[1] += self.gravity
            self.image_idx = 0
            # self.loadImage()
            self.rect = self.rect.move(self.movement)
            if self.rect.bottom >= self.init_position[1]:
                self.rect.bottom = self.init_position[1]
                self.is_jumping = False

        elif self.is_ducking:
            if self.refresh_counter % 6 == 0:
                self.refresh_counter = 0
                self.image_idx = (self.image_idx + 1) % 2 + 6
                # self.loadImage()
                
        else:
            if self.refresh_counter % 5 == 0:
                self.refresh_counter = 0
                self.image_idx = (self.image_idx + 1) % 2 + 2
                # self.loadImage()
        self.refresh_counter += 1
        self.loadImage()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
