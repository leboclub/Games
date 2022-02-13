import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, location=None):
        super().__init__()
        self.image = pygame.image.load(r'assets/images/button_nor.png')
        self.rect = self.image.get_rect()
        # self.image = pygame.Surface(image.get_size())
        # self.image.blit(image, (0, 0))
        # self.font = pygame.font.Font(r'assets/fonts/Marker Felt.ttf', 30)
        # text_render = self.font.render('Start', True, (20, 20, 20))
        # self.rect.center = location

    def draw(self, surface):
        surface.blit(self.image, self.rect)
