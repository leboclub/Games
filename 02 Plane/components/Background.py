import pygame


class Background(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image_0 = pygame.image.load(r'assets/images/background.png')
        self.image_1 = pygame.image.load(r'assets/images/background.png')
        self.rect_0 = self.image_0.get_rect()
        self.rect_1 = self.image_1.get_rect()
        self.rect_1.bottom = self.rect_0.top
        self.speed = 1

    def update(self):
        self.rect_0 = self.rect_0.move(0, self.speed)
        self.rect_1 = self.rect_1.move(0, self.speed)

        if self.rect_0.top >= 800:
            self.rect_0.bottom = 0

        if self.rect_1.top >= 800:
            self.rect_1.bottom = 0

    def draw(self, surface):
        surface.blit(self.image_0, self.rect_0)
        surface.blit(self.image_1, self.rect_1)
