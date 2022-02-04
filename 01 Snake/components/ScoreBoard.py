import pygame


class ScoreBoard(pygame.sprite.Sprite):
    # 1、初始化方法
    # 主要用于定义一些类的属性
    def __init__(self):
        # 调用父级的初始化方法
        super().__init__()

        self.font = pygame.font.Font(r'assets/fonts/neuropol.ttf', 18)
        # 一个精灵类需要具备两个基本的属性，1、精灵的图形；2、精灵的图形的矩形框
        self.image = self.font.render(
            'Score: ' + str(0), True, (255, 255, 255))
            
        # 从图形获取图像的矩形框
        self.rect = self.image.get_rect()
        # 调整矩形框的位置
        self.rect.topleft = 10, 10

    # 2、更新方法
    # 主要用于更新类的图像或者图像的矩形框
    def update(self, score):
        self.image = self.font.render(
            'Score: ' + str(score), True, (255, 255, 255))
            