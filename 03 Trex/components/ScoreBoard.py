import pygame

class ScoreBoard(pygame.sprite.Sprite):
    def __init__(self, sprite, sound=None):
        super().__init__()
        self.images = []
        for col in range(12):
            self.images.append(sprite.subsurface(
                (1310 + 20 * col, 4), (20, 24)))
        
        self.image = pygame.Surface((22*14, 26))
        self.image.fill((255, 255, 255))
        self.rect       = self.image.get_rect()
        self.rect.topleft = 868, 20
        self.msPerFrame = 1000 / 4
        self.hi_score   = self.read()
        self.score      = 0
        self.sound      = sound
        self.last_time  = 0
        self.flash_score = 0
        self.flash_idx  = 0
        self.is_flashing = False
    
    def read(self):
        with open(r'score.data', 'r', encoding='utf-8') as f:
            score = f.read()
        return score

    def write(self):
        if int(self.score) < int(self.hi_score):
            return

        with open(r'score.data', 'w', encoding='utf-8') as f:
            f.write(str(self.score))

    def update(self, current_time):
        self.image.fill((255, 255, 255))

        self.image.blit(self.images[10], (2, 2))
        self.image.blit(self.images[11], (24, 2))

        for idx, digital in enumerate(str(self.hi_score).zfill(5)):
            self.image.blit(self.images[int(digital)], ((idx + 3) * 22 + 2, 2))
        
        self.score = current_time // 100

        if self.score % 100 == 0:
            self.sound.play()
            if not self.is_flashing:
                self.flash_score = self.score
                self.is_flashing = True

        if self.is_flashing:
            if self.flash_idx < 8:
                if current_time - self.last_time > self.msPerFrame:
                    self.flash_idx += 1
                    self.last_time = current_time
                if self.flash_idx % 2 == 1:
                    return
            else:
                self.flash_idx = 0
                self.is_flashing = False
        score = self.flash_score if self.is_flashing else self.score
                
        for idx, digital in enumerate(str(score).zfill(5)):
            self.image.blit(self.images[int(digital)], ((idx + 9) * 22 + 2, 2))

    def draw(self, surface):
        surface.blit(self.image, self.rect)
