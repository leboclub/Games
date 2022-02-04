import pygame
from components.HeroBullet import *

class Hero(pygame.sprite.Sprite):
    def __init__(self, bullet_group):
        super().__init__()

        self.images = []
        paths = [
            r'assets/images/hero1.png',
            r'assets/images/hero2.png',
            r'assets/images/hero_blowup_n1.png',
            r'assets/images/hero_blowup_n2.png',
            r'assets/images/hero_blowup_n3.png',
            r'assets/images/hero_blowup_n4.png',
        ]
        for path in paths:
            image = pygame.image.load(path)
            image = pygame.transform.scale(image, (image.get_width() // 2, image.get_height() // 2))
            self.images.append(image)

        self.image_idx = 0
        self.image = self.images[self.image_idx]

        self.rect = self.image.get_rect()
        self.rect.center = 480 // 2 , 700
        
        self.last_time = 0
        self.frame_pre_ms = 1000 / 15

        self.cooldown = 0

        self.speed = 5
        self.status = 'NORMAL'
        self.downing = False

        self.firepower = 0
        self.bullet_group = bullet_group

    # 坠落
    def down(self):
        self.status = 'DWON'

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def move(self, dirction):
        if dirction == 'UP' and self.rect.top > 0:
            self.rect = self.rect.move(0, -self.speed)
        elif dirction == 'RIGHT' and self.rect.right < 480:
            self.rect = self.rect.move(self.speed, 0)
        elif dirction == 'DOWN' and self.rect.bottom < 800:
            self.rect = self.rect.move(0, self.speed)
        elif dirction == 'LEFT' and self.rect.left > 0:
            self.rect = self.rect.move(-self.speed, 0)

    def update(self, current_time):
        self.shot()

        if current_time - self.last_time > self.frame_pre_ms:
            self.image_idx += 1
            self.last_time = current_time

        if self.status == 'NORMAL':
            self.image_idx %= 2

        elif self.status == 'DOWN':
            if not self.downing:
                self.downing = True
                self.image_idx = 2
        
        if self.image_idx == len(self.images):
            return

        self.image = self.images[self.image_idx]

    # 升级
    def upgrade(self):
        self.firepower += 100

    def shot(self):
        self.cooldown -= 1
        if self.cooldown <= 0:
            self.cooldown = 10
            if self.firepower > 0:
                self.firepower -= 2
                for i in range(2):
                    HeroBullet((self.rect.centerx - 16 + i * 32,
                               self.rect.centery), 'laser').add(self.bullet_group)
            else:
                HeroBullet(self.rect.center).add(self.bullet_group)
