import pygame, sys
from random import *
from components.Cactus import *
from components.Cloud import *
from components.Horizon import *
from components.Pterodactyl import *
from components.ScoreBoard import *
from components.Trex import *

pygame.init()
size = width, height = 1200, 300
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Google Chrome T-rex')
fpsClock = pygame.time.Clock()

MAX_CACTUS_COUNT        = 3
MIN_CACTUS_GAP          = 480
MAX_PTERODACTYL_COUNT   = 1
MIN_PTERODACTYL_GAP     = 600
MAX_CLOUD_COUNT         = 5
MIN_CLOUD_GAP           = 200
MAX_CLOUD_GAP           = 800

# 导入雪碧图
image_sprite = pygame.image.load(r'assets/images/100-offline-sprite.png').convert_alpha()
image_sprite = pygame.transform.scale(image_sprite, (image_sprite.get_width() * 2, image_sprite.get_height() * 2))

# 导入声音文件
sounds = {
    'hit':              pygame.mixer.Sound(r'assets/audios/hit.mp3'),
    'button_press':     pygame.mixer.Sound(r'assets/audios/button-press.mp3'),
    'score_reached':    pygame.mixer.Sound(r'assets/audios/score-reached.mp3'),
}

# 实例化地平线
horizon         = Horizon(image_sprite)
scoreboard      = ScoreBoard(image_sprite, sounds['score_reached'])
clouds          = pygame.sprite.Group()
cactuses        = pygame.sprite.Group()
pterodactyls    = pygame.sprite.Group()
obstacles       = pygame.sprite.Group()
trex            = Trex(image_sprite)

# 变量初始化
last_obstacle_width = 0
obstacle_gap        = 0
cloud_gap           = 0
cloud_gap           = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 获取被按下的按键
    pressed_key = pygame.key.get_pressed()
    if pressed_key[pygame.K_UP] or pressed_key[pygame.K_SPACE]:
        trex.jump(sounds['button_press'])
    elif pressed_key[pygame.K_DOWN]:
        trex.duck()
    else:
        trex.run()

    if not trex.is_crashed:
        # 获取系统时钟
        ticks = pygame.time.get_ticks()

        if ticks % 100000 == 0:
            horizon.speed -= 1
            for item in clouds:
                item.speed -= ticks // 100000
            for item in cactuses:
                item.speed -= ticks // 100000
            for item in pterodactyls:
                item.speed -= ticks // 100000

        # 更新云组
        cloud_gap += 2
        # 云的间距大于 800 或大于 200，且数量小于 6，且概率等于 1/6
        if cloud_gap >= MAX_CLOUD_GAP or cloud_gap >= MIN_CLOUD_GAP and len(clouds) < MAX_CLOUD_COUNT and randint(1, 6) == 1:
            cloud = Cloud(image_sprite)
            clouds.add(cloud)
            cloud_gap = 0
    
        # 更新仙人掌
        obstacle_gap += 10
        if len(cactuses) < MAX_CACTUS_COUNT and randint(1, 20) == 1 and obstacle_gap >= MIN_CACTUS_GAP:
            cactus = Cactus(image_sprite)
            last_obstacle_width = cactus.image.get_width()
            cactuses.add(cactus)
            obstacle_gap = - last_obstacle_width
    
        # 更新翼龙
        if len(pterodactyls) < MAX_PTERODACTYL_COUNT and randint(1, 20) == 1 and obstacle_gap >= MIN_PTERODACTYL_GAP:
            pterodactyl = Pterodactyl(image_sprite)
            last_obstacle_width = pterodactyl.image.get_width()
            pterodactyls.add(pterodactyl)
            obstacle_gap = - last_obstacle_width

        # 更新游戏元素
        horizon.update()
        scoreboard.update(ticks)
        clouds.update()
        if ticks > 3000:
            cactuses.update()
            pterodactyls.update(ticks)
        
        # 检查碰撞
        for cactus in cactuses:
            if pygame.sprite.collide_mask(trex, cactus):
                # trex.crashed(sounds['hit'])
                scoreboard.write()

        for pterodactyl in pterodactyls:
            if pygame.sprite.collide_mask(trex, pterodactyl):
                # trex.crashed(sounds['hit'])
                scoreboard.write()

    trex.update(ticks)

    # 显示游戏元素
    screen.fill((255, 255, 255))
    horizon.draw(screen)
    scoreboard.draw(screen)
    clouds.draw(screen)
    cactuses.draw(screen)
    pterodactyls.draw(screen)
    trex.draw(screen)

    pygame.display.update()
    fpsClock.tick(60)
