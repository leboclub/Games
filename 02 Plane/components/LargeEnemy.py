import pygame
from components.EnemyBullet import *


class LargeEnemy(pygame.sprite.Sprite):

    def __init__(self, bullet_group):
        super().__init__()

        # 加载声音
        self.down_sound = pygame.mixer.Sound(r'assets/audios/enemy2_down.mp3')
        self.down_sound.set_volume(0.5)

        self.images = []
        paths = [
            r'assets/images/enemy2.png',
            r'assets/images/enemy2_n2.png',
            r'assets/images/enemy2_hit.png',
            r'assets/images/enemy2_down1.png',
            r'assets/images/enemy2_down2.png',
            r'assets/images/enemy2_down3.png',
            r'assets/images/enemy2_down4.png',
            r'assets/images/enemy2_down5.png',
            r'assets/images/enemy2_down6.png',
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
        self.rect.centerx, self.rect.bottom = 240, 0

        # 初始化速度
        self.x_speed = 3
        self.y_speed = 1

        self.downing = False
        self.image_idx = 0
        self.last_time = 0
        self.frame_pre_ms = 1000 // 10
        self.status = 'NORMAL'

        self.blood = 500
        self.bullet_group = bullet_group
        self.cooldwon = 0
        self.directions = [-3, -2, -1, 0, 1, 2, 3]
        self.score = 500

    def down(self):
        self.down_sound.play()
        self.status = 'DOWN'

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
            self.cooldwon = 60 * 8

        if self.rect.top < 0:
            self.rect = self.rect.move(0, self.y_speed)
        else:
            self.rect = self.rect.move(self.x_speed, 0)

        if self.rect.left < 0 or self.rect.right > 480:
            self.x_speed = -self.x_speed

        if current_time - self.last_time > self.frame_pre_ms:
            self.image_idx += 1
            self.last_time = current_time

        if self.status == 'NORMAL':
            self.image_idx %= 2

        elif self.status == 'HIT':
            self.image_idx = 2
            self.status = 'NORMAL'

        elif self.status == 'DOWN':
            if not self.downing:
                self.downing = True
                self.image_idx = 3

        # 如果超过图片索引就自毁
        if self.rect.top >= 800 or self.image_idx == len(self.images):
            self.kill()
            return

        self.image = self.images[self.image_idx]

    def shot(self):
        for direction in self.directions:
            EnemyBullet(self.rect.center, direction).add(self.bullet_group)
