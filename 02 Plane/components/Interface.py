import sys
import pygame


def Button(screen, position, text, cfg):
    btn = pygame.image.load(r'assets/images/button_nor.png')
    btn_p = pygame.image.load(r'assets/images/button_p.png')
    btn_text = pygame.image.load(r'assets/images/button_p.png')
    image = pygame.Surface(132, 48)
    image.blit(btn, (0, 0))
    return screen.blit(image, (left + 50, top + 10))


'''开始界面'''


def StartInterface(screen, cfg):
    clock = pygame.time.Clock()
    while True:
        button_1 = Button(screen, (330, 190), '单人模式', cfg)
        button_2 = Button(screen, (330, 305), '双人模式', cfg)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_1.collidepoint(pygame.mouse.get_pos()):
                    return 1
                elif button_2.collidepoint(pygame.mouse.get_pos()):
                    return 2
        clock.tick(60)
        pygame.display.update()


'''结束界面'''


def EndInterface(screen, cfg):
    clock = pygame.time.Clock()
    while True:
        button_1 = Button(screen, (330, 190), '重新开始', cfg)
        button_2 = Button(screen, (330, 305), '退出游戏', cfg)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_1.collidepoint(pygame.mouse.get_pos()):
                    return
                elif button_2.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()
        clock.tick(60)
        pygame.display.update()
