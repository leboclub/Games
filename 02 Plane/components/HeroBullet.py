import pygame

class HeroBullet(pygame.sprite.Sprite):
    def __init__(self, pos, type='normal'):
        super().__init__()

        self.sound = pygame.mixer.Sound(r'assets/audios/bullet.mp3')
        self.images = {
                    'normal': pygame.image.load(r'assets/images/bullet1.png'),
                    'laser': pygame.image.load(r'assets/images/bullet2.png'),
                }
        self.image = self.images[type]
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 2, self.image.get_height() // 2))
        self.sound.set_volume(0.1)
        self.sound.play()
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed = -10

    def update(self):
        self.rect = self.rect.move(0, self.speed)
        if self.rect.bottom <= 0:
            self.kill()