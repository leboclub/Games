import pygame, sys
from components.Background import *
from components.Hero import *
from components.LargeEnemy import *
from components.MediumEnemy import *
from components.SmallEnemy import *
from components.ScoreBoard import *

pygame.init()
pygame.display.set_caption('飞机大战')
size = width, height = 480, 800
screen = pygame.display.set_mode(size)
fpsClock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 10000)

# 背景音乐
pygame.mixer.music.load(r'assets/audios/game_music.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

get_double_laser = pygame.mixer.Sound(r'assets/audios/get_double_laser.mp3')
get_double_laser.set_volume(0.5)
get_bomb = pygame.mixer.Sound(r'assets/audios/get_bomb.mp3')
get_bomb.set_volume(0.5)

background = Background()  # 实例化背景
score_board = ScoreBoard()  # 实例化计分板

hero_bullet_group = pygame.sprite.Group()  # 主角子弹组
hero = Hero(hero_bullet_group)  # 实例化主角

prop_group = pygame.sprite.Group()  # 补给包组
enemy_bullet_group = pygame.sprite.Group()  # 敌机子弹组
enemy_group = pygame.sprite.Group()  # 小型敌机组
small_enemy_group = pygame.sprite.Group()  # 小型敌机组
medium_enemy_group = pygame.sprite.Group()  # 中型敌机组
large_enemy_group = pygame.sprite.Group()  # boss 机组

score = 0  # 分数
playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.USEREVENT:
            pass

    pressed_key = pygame.key.get_pressed()
    if pressed_key[pygame.K_UP]:
        hero.move('UP')
    if pressed_key[pygame.K_DOWN]:
        hero.move('DOWN')
    if pressed_key[pygame.K_LEFT]:
        hero.move('LEFT')
    if pressed_key[pygame.K_RIGHT]:
        hero.move('RIGHT')

    # 增加敌机
    if randint(1, 30) == 1 and len(small_enemy_group) < 50:
        SmallEnemy().add(small_enemy_group)

    if randint(1, 100) == 1 and len(medium_enemy_group) < 20:
        MediumEnemy(enemy_bullet_group, prop_group).add(medium_enemy_group)

    if score > 0 and score % 2000 == 0 and len(large_enemy_group) < 1:
        LargeEnemy(enemy_bullet_group).add(large_enemy_group)

    # 检查敌机子弹与主角碰撞
    for bullet in enemy_bullet_group:
        if pygame.sprite.collide_mask(hero, bullet):
            playing = False

    for enemy in small_enemy_group:
        if pygame.sprite.collide_mask(hero, enemy):
            playing = False

    for enemy in medium_enemy_group:
        if pygame.sprite.collide_mask(hero, enemy):
            playing = False

    for enemy in large_enemy_group:
        if pygame.sprite.collide_mask(hero, enemy):
            playing = False

    # 检查子弹与敌机碰撞
    for bullet in hero_bullet_group:
        # boss 敌机
        sprite_list = pygame.sprite.spritecollide(bullet, small_enemy_group,
                                                  False)
        if sprite_list:
            bullet.kill()
            for enemy in sprite_list:
                score += enemy.hit()

        # boss 敌机
        sprite_list = pygame.sprite.spritecollide(bullet, medium_enemy_group,
                                                  False)
        if sprite_list:
            bullet.kill()
            for enemy in sprite_list:
                score += enemy.hit()

        # boss 敌机
        sprite_list = pygame.sprite.spritecollide(bullet, large_enemy_group,
                                                  False)
        if sprite_list:
            bullet.kill()
            for enemy in sprite_list:
                score += enemy.hit()

    # 检查主角与补给包碰撞
    prop_list = pygame.sprite.spritecollide(hero, prop_group, True)
    if prop_list:
        for prop in prop_list:
            if prop.type == 0:
                get_double_laser.play()
                hero.upgrade()
            else:
                get_bomb.play()
                for enemy in small_enemy_group:
                    enemy.down()
                for enemy in medium_enemy_group:
                    enemy.down()
                for enemy in large_enemy_group:
                    enemy.down()
                for bullet in enemy_bullet_group:
                    bullet.kill()

    tick = pygame.time.get_ticks()

    # 更新部分
    background.update()
    enemy_bullet_group.update()
    hero_bullet_group.update()
    small_enemy_group.update(tick)
    medium_enemy_group.update(tick)
    large_enemy_group.update(tick)
    prop_group.update(tick)
    hero.update(tick)
    score_board.update(score)

    # 绘制部分
    background.draw(screen)
    enemy_bullet_group.draw(screen)
    hero_bullet_group.draw(screen)
    large_enemy_group.draw(screen)
    medium_enemy_group.draw(screen)
    small_enemy_group.draw(screen)
    prop_group.draw(screen)
    hero.draw(screen)
    score_board.draw(screen)

    pygame.display.update()
    fpsClock.tick(60)
