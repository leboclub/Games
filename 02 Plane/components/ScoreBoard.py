import pygame


class ScoreBoard(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.font = pygame.font.Font(r'assets/fonts/Marker Felt.ttf', 30)
        self.image = self.font.render(str(0), True, (20, 20, 20))
        self.rect = self.image.get_rect()
        self.rect.topleft = 20, 20

    def update(self, score):
        self.image = self.font.render(str(score), True, (20, 20, 20))

    def draw(self, surface):
        surface.blit(self.image, self.rect)