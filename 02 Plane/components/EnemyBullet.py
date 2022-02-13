import pygame


class EnemyBullet(pygame.sprite.Sprite):

    def __init__(self, pos, x_speed):
        super().__init__()

        self.sound = pygame.mixer.Sound(r'assets/audios/bullet.mp3')
        self.image = pygame.image.load(r'assets/images/bullet.png')
        self.sound.set_volume(0.1)
        self.sound.play()
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.x_speed = x_speed
        self.y_speed = 5

    def update(self):
        self.rect = self.rect.move(self.x_speed, self.y_speed)
        if self.rect.top >= 800 or self.rect.right <= 0 or self.rect.left >= 480:
            self.kill()
