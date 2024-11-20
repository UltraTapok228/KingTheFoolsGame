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

man_stand.set_colorkey([163,73,164])
man_left.set_colorkey([163,73,164])
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
alb1_rect.x = 300
alb1_rect.y = 150

alb2_img = pygame.image.load('alb2.png')
alb2_rect = alb2_img.get_rect()
alb2_rect.x = WIDTH-400
alb2_rect.y = 150

alb3_img = pygame.image.load('alb3.png')
alb3_rect = alb3_img.get_rect()
alb3_rect.x = 550
alb3_rect.y = 150

alb4_img = pygame.image.load('alb4.png')
alb4_rect = alb4_img.get_rect()
alb4_rect.x = 300
alb4_rect.y = 270

alb5_img = pygame.image.load('alb5.png')
alb5_rect = alb5_img.get_rect()
alb5_rect.x = 550
alb5_rect.y = 270

alb6_img = pygame.image.load('alb6.png')
alb6_rect = alb6_img.get_rect()
alb6_rect.x = WIDTH-400
alb6_rect.y = 270

alb7_img = pygame.image.load('alb7.png')
alb7_rect = alb7_img.get_rect()
alb7_rect.x = 300
alb7_rect.y = 390

alb8_img = pygame.image.load('alb8.png')
alb8_rect = alb8_img.get_rect()
alb8_rect.x = 550
alb8_rect.y = 390

alb9_img = pygame.image.load('alb9.png')
alb9_rect = alb9_img.get_rect()
alb9_rect.x = WIDTH-400
alb9_rect.y = 390

# Игрок находится на платформе
on_platform = False
on_dirt = False
on_zish = False
# экран загрузки
menu = pygame.image.load('menu.jpg')
menu = pygame.transform.scale(menu, [1200, 700])

choice = pygame.image.load('choice.png')
choice2 = pygame.image.load('choice2.png')

testy = 2
test = 2

# фон
background = pygame.image.load('background.png') # стардантный фон леса
background = pygame.transform.scale(background, [WIDTH, HEIGHT])

background1 = pygame.image.load('dark_forest.png') # фон внезапной головы(в начале)
background1 = pygame.transform.scale(background1, [WIDTH, HEIGHT])

background2 = pygame.image.load('pupet_wizard_background.png') # фон куклы кодуна
background2 = pygame.transform.scale(background2, [WIDTH, HEIGHT])

background3 = pygame.image.load('room_zish.png') # комната злодея(конец злодея и шапки)
background3 = pygame.transform.scale(background3, [WIDTH, HEIGHT])

background4 = pygame.image.load('market.png') # базар (злодей и шапка)
background4 = pygame.transform.scale(background4, [WIDTH, HEIGHT])

background5 = pygame.image.load('dark_forest.jpeg') # фон лесника и охотника
background5 = pygame.transform.scale(background5, [WIDTH, HEIGHT])

# фон на данный момент
fon_now = background

# Кнопка начала игры
start_btn = pygame.image.load('play_btn.png')
start_btn = pygame.transform.scale(start_btn, [278, 80])
start_rect = start_btn.get_rect()
start_rect.x = WIDTH // 2 - (278//2)
start_rect.y = HEIGHT // 2 + 50

#start_rect.x = WIDTH // 2 - 474
#start_rect.y = HEIGHT // 2 + 50

# Кнопка выхода из игры
exit_btn = pygame.image.load('exit.png')
exit_btn = pygame.transform.scale(exit_btn, [278, 80])
exit_rect = exit_btn.get_rect()
exit_rect.x = WIDTH // 2 - (278//2)
exit_rect.y = HEIGHT // 2 + 150

# песни альбома "Камнем по голове"
sudden_head_img = pygame.image.load('Камнем по голове/Внезапная голова.png')
sudden_head_img = pygame.transform.scale(sudden_head_img, [100, 100])
sudden_head_rect = sudden_head_img.get_rect()
sudden_head_rect.x = 300
sudden_head_rect.y = 150

fool_and_lightning = pygame.image.load('Камнем по голове/дурак и молния.png')
fool_and_lightning = pygame.transform.scale(fool_and_lightning, [100, 100])
fool_and_lightning_rect = fool_and_lightning.get_rect()
fool_and_lightning_rect.x = WIDTH-400
fool_and_lightning_rect.y = 150


villain_and_hat = pygame.image.load('Камнем по голове/Злодей и Шапка.png')
villain_and_hat = pygame.transform.scale(villain_and_hat, [100, 100])
villain_and_hat_rect = fool_and_lightning.get_rect()
villain_and_hat_rect.x = 550
villain_and_hat_rect.y = 150

# песни из Акустического альбома

puppet_of_wizard = pygame.image.load('Акустический альбом/кукла колдуна.png')
puppet_of_wizard = pygame.transform.scale(puppet_of_wizard, [100, 100])
puppet_of_wizard_rect = puppet_of_wizard.get_rect()
puppet_of_wizard_rect.x = 300
puppet_of_wizard_rect.y = 150

morning_dawn = pygame.image.load('Акустический альбом/утренний рассвет.png')
morning_dawn = pygame.transform.scale(morning_dawn, [100, 100])
morning_dawn_rect = morning_dawn.get_rect()
morning_dawn_rect.x = 550
morning_dawn_rect.y = 150

map = [
    '                            ',
    '                            ',  
    '                            ',
    '                            ',
    '                            ',
    '                            ',
    '                            ',
    '          -                 ',
    '****************************',
    '----------------------------',
    '----------------------------',
    '----------------------------',
    '                            ',
]

map2 = [
    '                            ',
    '                            ',  
    '                            ',
    '                            ',
    '                            ',
    '          -                 ',
    '          -                 ',
    '          -                 ',
    '****************************',
    '----------------------------',
    '----------------------------',
    '----------------------------',
    '                            ',
]

map3 = [
    '                            ',
    '                            ',  
    '                            ',
    '                            ',
    '                            ',
    '                            ',
    '          -                 ',
    '          -                 ',
    '****************************',
    '----------------------------',
    '----------------------------',
    '----------------------------',
    '                            ',
]

map4 = [
    '                            ',
    '                            ',  
    '                            ',
    '                            ',
    '                            ',
    '                            ',
    '                            ',
    '          -                 ',
    '****************************',
    '----------------------------',
    '----------------------------',
    '----------------------------',
    '                            ',
]

map5 = [
    '                            ',
    '                            ',  
    '                            ',
    '                            ',
    '                            ',
    '          -                 ',
    '          -                 ',
    '          -                 ',
    '****************************',
    '----------------------------',
    '----------------------------',
    '----------------------------',
    '                            ',
]

map6 = [
    '                            ',
    '                            ',  
    '                            ',
    '                            ',
    '                            ',
    '                            ',
    '          -                 ',
    '          -                 ',
    '****************************',
    '----------------------------',
    '----------------------------',
    '----------------------------',
    '                            ',
]

map7 = [
    '                            ',
    '                            ',  
    '                            ',
    '                            ',
    '                            ',
    '                            ',
    '                            ',
    '          -                 ',
    '****************************',
    '----------------------------',
    '----------------------------',
    '----------------------------',
    '                            ',
]

map8 = [
    '                            ',
    '                            ',  
    '                            ',
    '                            ',
    '                            ',
    '          -                 ',
    '          -                 ',
    '          -                 ',
    '****************************',
    '----------------------------',
    '----------------------------',
    '----------------------------',
    '                            ',
]

map9 = [
    '                            ',
    '                            ',  
    '                            ',
    '                            ',
    '                            ',
    '                            ',
    '          -                 ',
    '          -                 ',
    '****************************',
    '----------------------------',
    '----------------------------',
    '----------------------------',
    '                            ',
]

platforms = []
dirts = []
zishs = []
stones = []
vgs = []

map_now = map
run = False
frame = 0
show = True
while True:
    if show == True:
        window.blit(background, [0,0])
    
    man_old = man_rect.copy()    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            # прыжок
            if event.key == pygame.K_SPACE:
                show = False
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
        music1 = pygame.mixer.music.load("music_b.mp3")
        pygame.mixer.music.play(-1)
        window.blit(start_btn, start_rect)
        window.blit(exit_btn, exit_rect)

        # Позиция указателя мыши
        pos = pygame.mouse.get_pos()

        if start_rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == True:
            main_menu = False
            choice_menu = True
        elif exit_rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == True:
            exit()

    elif main_menu == False:
        window.blit(choice2, [0, 0])
        window.blit(alb1_img, alb1_rect)
        window.blit(alb2_img, alb2_rect)
        window.blit(alb3_img, alb3_rect)
        window.blit(alb4_img, alb4_rect)
        window.blit(alb5_img, alb5_rect)
        window.blit(alb6_img, alb6_rect)
        window.blit(alb7_img, alb7_rect)
        window.blit(alb8_img, alb8_rect)
        window.blit(alb9_img, alb9_rect)
        pos = pygame.mouse.get_pos()
        # альбом камнем по голове
        if alb1_rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == True:
            window.blit(choice, [0, 0])
            window.blit(sudden_head_img, sudden_head_rect)
            window.blit(villain_and_hat, villain_and_hat_rect)
            window.blit(fool_and_lightning, fool_and_lightning_rect) # во второй бетке)))
            """window.blit(background1, [0, 0])
            
            for i in range(len(map_now)):
                for j in range(len(map_now[i])):
                    
                    map_now = map
                    
                    if map_now[i][j] == '*':
                        platform_rect = platform_img.get_rect()
                        platform_rect.x = platform_rect.width * j + test
                        platform_rect.y = platform_rect.height * i + testy
                        platforms.append(platform_rect)
                        window.blit(platform_img, platform_rect)
                    if map_now[i][j] == '-': 
                        dirt_rect = dirt_img.get_rect()
                        dirt_rect.x = dirt_rect.width * j + test
                        dirt_rect.y = dirt_rect.height * i + testy
                        dirts.append(dirt_rect)
                        window.blit(dirt_img, dirt_rect)    
            man_rect.x += change_x"""
        # акустический альбом    
        elif alb2_rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == True:
            window.blit(choice, [0, 0])
            window.blit(puppet_of_wizard, puppet_of_wizard_rect)
            window.blit(morning_dawn, morning_dawn_rect)
            '''window.blit(background2, [0, 0])
            for i in range(len(map_now)):
                for j in range(len(map_now[i])):
                    map_now = map2
                    
                    if map_now[i][j] == '*':
                        platform_rect = platform_img.get_rect()
                        platform_rect.x = platform_rect.width * j + test
                        platform_rect.y = platform_rect.height * i + testy
                        platforms.append(platform_rect)
                        window.blit(platform_img, platform_rect)
                    if map_now[i][j] == '-': 
                        dirt_rect = dirt_img.get_rect()
                        dirt_rect.x = dirt_rect.width * j + test
                        dirt_rect.y = dirt_rect.height * i + testy
                        dirts.append(dirt_rect)
                        window.blit(dirt_img, dirt_rect)    
            man_rect.x += change_x'''
        # альбом будь как дома путник
        elif alb3_rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == True:
            window.blit(choice, [0, 0])
            '''window.blit(background5, [0, 0])
            for i in range(len(map_now)):
                for j in range(len(map_now[i])):
                    map_now = map3
                    
                    if map_now[i][j] == '*':
                        platform_rect = platform_img.get_rect()
                        platform_rect.x = platform_rect.width * j + test
                        platform_rect.y = platform_rect.height * i + testy
                        platforms.append(platform_rect)
                        window.blit(platform_img, platform_rect)
                    if map_now[i][j] == '-': 
                        dirt_rect = dirt_img.get_rect()
                        dirt_rect.x = dirt_rect.width * j + test
                        dirt_rect.y = dirt_rect.height * i + testy
                        dirts.append(dirt_rect)
                        window.blit(dirt_img, dirt_rect)    
            man_rect.x += change_x   '''     
        # как в старой сказке
        elif alb4_rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == True:
            window.blit(choice, [0, 0])
            '''window.blit(background, [0, 0])
            for i in range(len(map_now)):
                for j in range(len(map_now[i])):
                    map_now = map4
                    
                    if map_now[i][j] == '*':
                        platform_rect = platform_img.get_rect()
                        platform_rect.x = platform_rect.width * j + test
                        platform_rect.y = platform_rect.height * i + testy
                        platforms.append(platform_rect)
                        window.blit(platform_img, platform_rect)
                    if map_now[i][j] == '-': 
                        dirt_rect = dirt_img.get_rect()
                        dirt_rect.x = dirt_rect.width * j + test
                        dirt_rect.y = dirt_rect.height * i + testy
                        dirts.append(dirt_rect)
                        window.blit(dirt_img, dirt_rect)    
            man_rect.x += change_x   '''   
        # альбом жаль нет ружья  
        elif alb5_rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == True:
            window.blit(choice, [0, 0])
            '''window.blit(background, [0, 0])
            for i in range(len(map_now)):
                for j in range(len(map_now[i])):
                    map_now = map5
                    
                    if map_now[i][j] == '*':
                        platform_rect = platform_img.get_rect()
                        platform_rect.x = platform_rect.width * j + test
                        platform_rect.y = platform_rect.height * i + testy
                        platforms.append(platform_rect)
                        window.blit(platform_img, platform_rect)
                    if map_now[i][j] == '-': 
                        dirt_rect = dirt_img.get_rect()
                        dirt_rect.x = dirt_rect.width * j + test
                        dirt_rect.y = dirt_rect.height * i + testy
                        dirts.append(dirt_rect)
                        window.blit(dirt_img, dirt_rect)    
            man_rect.x += change_x     '''   
        # альбом бунт на корабле
        elif alb6_rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == True:
            window.blit(choice, [0, 0])
            '''window.blit(background, [0, 0])
            for i in range(len(map_now)):
                for j in range(len(map_now[i])):
                    map_now = map6
                    
                    if map_now[i][j] == '*':
                        platform_rect = platform_img.get_rect()
                        platform_rect.x = platform_rect.width * j + test
                        platform_rect.y = platform_rect.height * i + testy
                        platforms.append(platform_rect)
                        window.blit(platform_img, platform_rect)
                    if map_now[i][j] == '-': 
                        dirt_rect = dirt_img.get_rect()
                        dirt_rect.x = dirt_rect.width * j + test
                        dirt_rect.y = dirt_rect.height * i + testy
                        dirts.append(dirt_rect)
                        window.blit(dirt_img, dirt_rect)    
            man_rect.x += change_x    '''
        # альбом продавец кошмаров
        elif alb7_rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == True:
            window.blit(choice, [0, 0])
            '''window.blit(background, [0, 0])
            for i in range(len(map_now)):
                for j in range(len(map_now[i])):
                    map_now = map7
                    
                    if map_now[i][j] == '*':
                        platform_rect = platform_img.get_rect()
                        platform_rect.x = platform_rect.width * j + test
                        platform_rect.y = platform_rect.height * i + testy
                        platforms.append(platform_rect)
                        window.blit(platform_img, platform_rect)
                    if map_now[i][j] == '-': 
                        dirt_rect = dirt_img.get_rect()
                        dirt_rect.x = dirt_rect.width * j + test
                        dirt_rect.y = dirt_rect.height * i + testy
                        dirts.append(dirt_rect)
                        window.blit(dirt_img, dirt_rect)    
            man_rect.x += change_x    '''
        # альбом тень клоуна
        elif alb8_rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == True:
            window.blit(choice, [0, 0])
            '''window.blit(background, [0, 0])
            for i in range(len(map_now)):
                for j in range(len(map_now[i])):
                    map_now = map8
                    
                    if map_now[i][j] == '*':
                        platform_rect = platform_img.get_rect()
                        platform_rect.x = platform_rect.width * j + test
                        platform_rect.y = platform_rect.height * i + testy
                        platforms.append(platform_rect)
                        window.blit(platform_img, platform_rect)
                    if map_now[i][j] == '-': 
                        dirt_rect = dirt_img.get_rect()
                        dirt_rect.x = dirt_rect.width * j + test
                        dirt_rect.y = dirt_rect.height * i + testy
                        dirts.append(dirt_rect)
                        window.blit(dirt_img, dirt_rect)    
            man_rect.x += change_x '''       
        # альбом театръ демона
        elif alb9_rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == True:
            window.blit(choice, [0, 0])
            '''window.blit(background, [0, 0])
            for i in range(len(map_now)):
                for j in range(len(map_now[i])):
                    map_now = map9
                    
                    if map_now[i][j] == '*':
                        platform_rect = platform_img.get_rect()
                        platform_rect.x = platform_rect.width * j + test
                        platform_rect.y = platform_rect.height * i + testy
                        platforms.append(platform_rect)
                        window.blit(platform_img, platform_rect)
                    if map_now[i][j] == '-': 
                        dirt_rect = dirt_img.get_rect()
                        dirt_rect.x = dirt_rect.width * j + test
                        dirt_rect.y = dirt_rect.height * i + testy
                        dirts.append(dirt_rect)
                        window.blit(dirt_img, dirt_rect)    
            man_rect.x += change_x    '''


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
                 
        #print(pygame.mouse.get_pos())

        if jump == True:
            man_rect.y -= jump_count
            if man_rect.y >= jump_max:
                jump = False
            if man_rect.y >= 900:
                testy -= 20     

        #if jump_count > -jump_max or (man_rect.bottom < HEIGHT and on_platform == False):
            #jump_count -= 1
            
        else:
            jump = False
            on_platform = True
               
            man_rect.x += change_x
                
        
                #main_menu = True 

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