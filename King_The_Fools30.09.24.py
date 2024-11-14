import pygame
from random import randint
import random
import time

pygame.init()

WIDTH = 1200
HEIGHT = 700
'''pygame.FULLSCREEN,'''

window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption('King The Fools')

FPS = 120
clock = pygame.time.Clock()

# иконка игры
icon_img = pygame.image.load('icon.png')
pygame.display.set_icon(icon_img)

# персонаж
man_stand = pygame.image.load('man.png')
man_left = pygame.transform.flip(man_stand, True, False)

man_stand.set_colorkey([163, 73, 164])
man_left.set_colorkey([163, 73, 164])
man_now = man_stand
speed = 5
change_x = 0
man = man_stand
man_rect = man_stand.get_rect()
man_rect.left = WIDTH // 2
man_rect.bottom = HEIGHT // 2

man_rect.x = randint(0, WIDTH)
man_rect.y = 0

jump = False
# Максимальная высота прыжка
jump_max = 50

# Изменение прыжка
jump_count = 0
jump_count_npc = 0

# Находимся ли в главном меню
main_menu = True
# находимся ли мы в выборе уровня
choice_menu = False

# СОЗДАЁМ ТЕКСТУРЫ
platform_img = pygame.image.load('grass.png')
dirt_img = pygame.image.load('dirt.png')
stone_img = pygame.image.load('stone.png')

alb1_img = pygame.image.load('alb1.png')
alb1_rect = alb1_img.get_rect()
alb1_rect.x = WIDTH // 2 - 50
alb1_rect.y = 150

alb2_img = pygame.image.load('alb2.png')
alb2_rect = alb2_img.get_rect()
alb2_rect.x = alb1_rect.x - 170
alb2_rect.y = 150

alb3_img = pygame.image.load('alb3.png')
alb3_rect = alb3_img.get_rect()
alb3_rect.x = alb1_rect.x + 170
alb3_rect.y = 150

zish_img = pygame.image.load('zish.png')
zish_rect = zish_img.get_rect()
vg_img = pygame.image.load('vg.png')
vg_rect = vg_img.get_rect()
# Игрок находится на платформе
on_platform = False
on_dirt = False
on_zish = False
# экран загрузки
menu = pygame.image.load('menu.jpg')
menu = pygame.transform.scale(menu, [1200, 700])

choice = pygame.image.load('choice.png')

testy = 2
test = 2

# фон
background = pygame.image.load('background.png')
background = pygame.transform.scale(background, [WIDTH, HEIGHT])
fon_now = background

# Кнопка начала игры
start_btn = pygame.image.load('play_btn.png')
start_btn = pygame.transform.scale(start_btn, [278, 80])
start_rect = start_btn.get_rect()
start_rect.x = WIDTH // 2 - 474
start_rect.y = HEIGHT // 2 + 50

# Кнопка выхода из игры
exit_btn = pygame.image.load('exit.png')
exit_btn = pygame.transform.scale(exit_btn, [278, 80])
exit_rect = exit_btn.get_rect()
exit_rect.x = WIDTH // 2
exit_rect.y = HEIGHT // 2 + 50

map = [
    '                            ',
    '                            ',
    '                            ',
    '                            ',
    '                            ',
    '                            ',
    '                            ',
    '          s  s              ',
    '****************************',
    '----------------------------',
    '----------------------------',
    '----------------------------',
    '                            ',
]

map2 = [
    "",
    "",
    "",
    "",
    ""
]

platforms = []
dirts = []
zishs = []
stones = []
vgs = []

map_now = map
run = False
frame = 0
while True:
    #window.blit(background, [0, 0])
    #music2 = pygame.mixer.music.load("music_m.mp3")
    #pygame.mixer.music.play(-1)
    man_old = man_rect.copy()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            # прыжок
            if event.key == pygame.K_SPACE:
                jump = True
                jump_count = jump_max
                on_platform = False
                # сдвижение камеры при возвышении
                if man_rect.y <= 460:
                    testy += 20

            # кнопка ESCAPE
            if event.key == pygame.K_ESCAPE:
                main_menu = True
                man_rect.x = randint(0, WIDTH)
                man_rect.y = 776

    if main_menu == True:
        window.blit(menu, [0, 0])
        window.blit(start_btn, start_rect)
        window.blit(exit_btn, exit_rect)

        # Позиция указателя мыши
        pos = pygame.mouse.get_pos()

        if start_rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == True:
            main_menu = False
            choice_menu = True
        elif exit_rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == True:
            exit()

    elif main_menu == False and choice_menu == True:
        window.blit(choice, [0, 0])
        window.blit(alb1_img, alb1_rect)
        window.blit(alb2_img, alb2_rect)
        window.blit(alb3_img, alb3_rect)
        
    pos = pygame.mouse.get_pos()

    if alb1_rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == True:
        window.blit(background, [0,0])
        for i in range(len(map_now)):
            for j in range(len(map_now[i])):
                # создаём траву
                if map_now[i][j] == '*':
                    platform_rect = platform_img.get_rect()
                    platform_rect.x = platform_rect.width * j + test
                    platform_rect.y = platform_rect.height * i + testy
                    platforms.append(platform_rect)
                    window.blit(platform_img, platform_rect)          
        pygame.display.update()
            
            
                  

        '''elif alb2_rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == True:
            exit()

        elif alb3_rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == True:
            exit()        
           '''

    else:
        for i in range(len(map_now)):
            for j in range(len(map_now[i])):
                # создаём траву
                if map_now[i][j] == '*':
                    platform_rect = platform_img.get_rect()
                    platform_rect.x = platform_rect.width * j + test
                    platform_rect.y = platform_rect.height * i + testy
                    platforms.append(platform_rect)
                    window.blit(platform_img, platform_rect)
                #  создаем землю
                elif map_now[i][j] == '-':
                    dirt_rect = dirt_img.get_rect()
                    dirt_rect.x = dirt_rect.width * j + test
                    dirt_rect.y = dirt_rect.height * i + testy
                    dirts.append(dirt_rect)
                    window.blit(dirt_img, dirt_rect)
                # создаем камень
                elif map_now[i][j] == 's':
                    stone_rect = stone_img.get_rect()
                    stone_rect.x = stone_rect.width * j + test
                    stone_rect.y = stone_rect.height * i + testy
                    stones.append(stone_rect)
                    window.blit(stone_img, stone_rect)

        man_rect.x += change_x
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:

            change_x = speed
            man = man_stand
            if man_rect.x >= 1090:
                test -= 10

                if man_rect.x > 1090:
                    man_rect.x = 1090

        # if keys[pygame.K_LEFT]:
        #     change_x = -speed
        #     man = man_left

        if keys[pygame.K_a]:
            change_x = -speed
            man = man_left
            if man_rect.x <= 0:
                test += 10

                if man_rect.x < 0:
                    man_rect.x = 0

        if not keys[pygame.K_d] and not keys[pygame.K_a]:
            change_x = 0

        # print(pygame.mouse.get_pos())

        if jump == True:
            man_rect.y -= jump_count
            if man_rect.y >= jump_max:
                jump = False
            if man_rect.y >= 900:
                testy -= 20

                # if jump_count > -jump_max or (man_rect.bottom < HEIGHT and on_platform == False):
            # jump_count -= 1

        else:
            jump = False
            on_platform = True

            man_rect.x += change_x

            # main_menu = True

        # Твёрдая трава
        if man_rect.bottom > HEIGHT:
            man_rect.bottom = HEIGHT
            jump = False
            on_platform = True

        man_rect.x += change_x

        for platform in platforms:
            if man_rect.colliderect(platform):
                if man_rect.left < man_old.left:
                    man_rect.x -= change_x

                if man_rect.right > man_old.right:
                    man_rect.x -= change_x

            if man_rect.colliderect(platform):
                if man_rect.bottom > man_old.bottom:
                    jump = False
                    on_platform = True
                    man_rect.bottom = platform.top

            if man_rect.colliderect(platform) and man_rect.y < platform.height:
                jump = False
                on_platform = True
                man_rect.top = man_old.top

        if on_platform == True:
            manrect_next = man_rect.copy()
            manrect_next.y += 1

            if manrect_next.collidelist(platforms) == -1:
                jump = True
                on_platform = False
                jump_count = -20

        window.blit(man, man_rect)

    pygame.display.update()
    clock.tick(FPS)