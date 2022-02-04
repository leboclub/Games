from ast import Return
import pygame
from random import randint


class SmallEnemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.down_sound = pygame.mixer.Sound(r'assets/audios/enemy0_down.mp3')
        self.down_sound.set_volume(0.5)

        self.images = []
        paths = [
            r'assets/images/enemy0.png',
            r'assets/images/enemy0_down1.png',
            r'assets/images/enemy0_down2.png',
            r'assets/images/enemy0_down3.png',
            r'assets/images/enemy0_down4.png',
        ]
        for path in paths:
            # 加载图片
            image = pygame.image.load(path)
            # 将图片加入到列表中
            self.images.append(image)
        # 获取第一桢图片
        self.image = self.images[0]

        # 设置矩形框大小
        self.rect = self.image.get_rect()
        # 调整矩形框位置
        self.rect.bottomleft = randint(0, 480 - self.image.get_width()), 0

        # 初始化速度
        self.x_speed        = 0
        self.y_speed        = randint(1, 2)

        self.downing        = False
        self.image_idx      = 0
        self.last_time      = 0
        self.frame_pre_ms   = 1000 // 10
        self.status         = 'NORMAL'

        self.blood          = 1
        self.cooldwon       = 0
        self.score          = 10

    def down(self):
        self.down_sound.play()
        self.status = 'DOWN'

    def hit(self):
        if self.downing or self.blood == 0:
            return 0

        self.blood -= 1
        if self.blood == 0:
            self.down()
            return 10
        return 0

    def update(self, current_time):
        self.rect = self.rect.move(self.x_speed, self.y_speed)

        if self.rect.top >= 800:
            self.kill()

        if current_time - self.last_time > self.frame_pre_ms:
            self.image_idx += 1
            self.last_time = current_time

        if self.status == 'NORMAL':
            self.image_idx %= 1
        
        elif self.status == 'HIT':
            self.image_idx = 1
            self.status = 'NORMAL'

        elif self.status == 'DOWN':
            if not self.downing:
                self.image_idx = 1
                self.downing = True

        if self.image_idx == len(self.images):
            self.kill() 
            return

        self.image = self.images[self.image_idx]
