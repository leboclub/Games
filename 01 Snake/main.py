import pygame, sys
from components.Apple import *
from components.Body import *
from components.Head import *
from components.ScoreBoard import *

pygame.init()
size = width, height = 960, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption('贪吃蛇 - 经典游戏复刻')
fpsClock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 4000)

# 载入资源
bg_image    = pygame.image.load(r'assets/images/bg.png')
score_sound = pygame.mixer.Sound(r'assets/audios/score-reached.mp3')

# 定义精灵组
apple_group = pygame.sprite.Group()
body_group  = pygame.sprite.Group()

# 实例化苹果
Apple(apple_group)
body_position_list = [
    (24 * 18, 24 * 12),
    (24 * 19, 24 * 12),
    (24 * 20, 24 * 12),
]
# 实例化蛇身
for position in body_position_list:
    Body(body_group)

head        = Head()
scoreboard  = ScoreBoard()
score       = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.USEREVENT and len(apple_group) < 3:
            Apple(apple_group)

    # 键盘事件控制蛇头的方向
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_RIGHT] and head.heading != 'LEFT':
        head.heading = 'RIGHT'
    elif pressed_keys[pygame.K_LEFT] and head.heading != 'RIGHT':
        head.heading = 'LEFT'
    elif pressed_keys[pygame.K_UP] and head.heading != 'DOWN':
        head.heading = 'UP'
    elif pressed_keys[pygame.K_DOWN] and head.heading != 'UP':
        head.heading = 'DOWN'

    # 4、游戏的逻辑部分
    body_position_list.append(head.rect.topleft)

    # 检测蛇头是否与苹果碰撞，如果碰撞则
    if pygame.sprite.spritecollide(head, apple_group, True):
        # 加分
        score += 10
        # 播放声音
        score_sound.play()
        # 增加蛇身
        Body(body_group)
        # 增加苹果
        Apple(apple_group)
    else:
        # 减少蛇身长度
        body_position_list.pop(0)

    # 更新蛇身位置
    for idx, body in enumerate(body_group):
        body.rect.topleft = body_position_list[idx]

    # 更新蛇头
    head.update()

    # 更新计分板
    scoreboard.update(score)

    # 检测蛇头是否与蛇身碰撞，如果碰撞则
    if pygame.sprite.spritecollide(head, body_group, False):
        # 游戏结束
        break

    # 检测蛇头是否超出边界，如果碰撞则
    if (head.rect.left < 0 or head.rect.right > width or 
        head.rect.top < 0 or head.rect.bottom > height):
        # 游戏结束
        break

    # 5、游戏的显示部分（注意图层顺序）
    screen.blit(bg_image, (0, 0))
    apple_group.draw(screen)
    body_group.draw(screen)
    screen.blit(head.image, head.rect)
    screen.blit(scoreboard.image, scoreboard.rect)

    pygame.display.update()
    fpsClock.tick(5)
