import pygame
from components.EnemyBullet import *
from components.Prop import *
from random import choice, randint


class MediumEnemy(pygame.sprite.Sprite):

    def __init__(self, buller_group, prop_group):
        super().__init__()

        self.down_sound = pygame.mixer.Sound(r'assets/audios/enemy1_down.mp3')
        self.down_sound.set_volume(0.5)

        self.images = []
        paths = [
            r'assets/images/enemy1.png',
            r'assets/images/enemy1_hit.png',
            r'assets/images/enemy1_down1.png',
            r'assets/images/enemy1_down2.png',
            r'assets/images/enemy1_down3.png',
            r'assets/images/enemy1_down4.png',
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
        self.x_speed = 0
        self.y_speed = randint(1, 2)

        self.downing = False
        self.image_idx = 0
        self.last_time = 0
        self.frame_pre_ms = 1000 // 10
        self.status = 'NORMAL'

        self.blood = 6
        self.buller_group = buller_group
        self.cooldwon = 0
        self.directions = [-3, -2, -1, 0, 1, 2, 3]
        self.prop_group = prop_group
        self.score = 50

    def down(self):
        self.down_sound.play()
        self.status = 'DOWN'
        if randint(1, 10) == 1:
            Prop(self.rect.center).add(self.prop_group)

    def hit(self):
        if self.downing or self.blood == 0:
            return 0

        self.blood -= 1
        if self.blood == 0:
            self.down()
            return self.score

        return 0

    def update(self, current_time):
        self.cooldwon -= 1
        if self.cooldwon <= 0:
            self.shot()
            self.cooldwon = 60 * 5

        self.rect = self.rect.move(self.x_speed, self.y_speed)

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
                self.downing = True
                self.image_idx = 2

        # 如果超过图片索引就自毁
        if self.rect.top >= 800 or self.image_idx == len(self.images):
            self.kill()
            return

        self.image = self.images[self.image_idx]

    def shot(self):
        direction = choice(self.directions)
        EnemyBullet(self.rect.center, direction).add(self.buller_group)
