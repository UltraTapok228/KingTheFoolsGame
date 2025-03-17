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
icon_img = pygame.image.load('assets/images/icons/icon.png')
pygame.display.set_icon(icon_img)

# Персонажи игры

# Горшок
gorshok_stand = pygame.image.load('assets/images/персонажи/gorshok.png')
gorshok_left = pygame.transform.flip(gorshok_stand, True, False)

gorshok_stand.set_colorkey([163,73,164])
gorshok_left.set_colorkey([163,73,164])
man_now = gorshok_stand
speed = 6
change_x = 0
gorshok = gorshok_stand
gorshok_rect = gorshok_stand.get_rect()
gorshok_rect.left = WIDTH // 2
gorshok_rect.bottom = HEIGHT // 2

gorshok_rect.x = randint(0, WIDTH)
gorshok_rect.y = 0

# Злодей и Шпака
villian = pygame.image.load('assets/images/персонажи/villian.png')
villian_left = pygame.transform.flip(villian, True, False)

villian_now = villian
villian_rect = villian.get_rect()
villian_rect.left = WIDTH // 2
villian_rect.bottom = HEIGHT // 2

villian_rect.x = 600
villian_rect.y = 0

# Торговец
trader = pygame.image.load('assets/images/персонажи/trader.png')
trader_left = pygame.transform.flip(trader, True, False)

trader_now = trader
trader_rect = trader.get_rect()
trader_rect.left = WIDTH // 2
trader_rect.bottom = HEIGHT // 2

'''
trader_rect.x = ...
trader_rect.y = ...
'''

jump = False
# Максимальная высота прыжка
jump_max = 50

# Изменение прыжка
jump_count = 0

# Находимся ли в главном меню
main_menu = True
# находимся ли мы в выборе уровня
choice_menu = False

choice_menu2 = False

# СОЗДАЁМ ТЕКСТУРЫ
on_grass_img = pygame.image.load('assets/images/компоненты локации/grass.png')
on_grass_img = pygame.transform.scale(on_grass_img, [70, 70])

stone_briks_img = pygame.image.load('assets/images/компоненты локации/stone_bricks.png') # символ в массиве "s"

dirt_img = pygame.image.load('assets/images/компоненты локации/dirt.png')
stone_img = pygame.image.load('assets/images/компоненты локации/stone.png')
stone_img = pygame.transform.scale(stone_img, [70, 70])

board = pygame.image.load('assets/images/компоненты локации/boards.png') # символ в массиве "b"

alb1_img = pygame.image.load('assets/images/обложки альбомов/alb1.png')
alb1_rect = alb1_img.get_rect()
alb1_rect.x = 300
alb1_rect.y = 150

alb2_img = pygame.image.load('assets/images/обложки альбомов/alb2.png')
alb2_rect = alb2_img.get_rect()
alb2_rect.x = 550
alb2_rect.y = 150

alb3_img = pygame.image.load('assets/images/обложки альбомов/alb3.png')
alb3_rect = alb3_img.get_rect()
alb3_rect.x = WIDTH-400
alb3_rect.y = 150

# экран загрузки
menu = pygame.image.load('assets/images/backgrounds/менюшки/menu.png')
menu = pygame.transform.scale(menu, [1200, 700])

choice = pygame.image.load('assets/images/backgrounds/менюшки/choice.png')
choice2 = pygame.image.load('assets/images/backgrounds/менюшки/choice2.png')

comming_soon_img = pygame.image.load('assets/images/backgrounds/менюшки/comming soon.png')

# Игрок находится на платформе
on_grass = False
on_board = False
on_dirt = False
on_brick = False

# фон
background = pygame.image.load('assets/images/backgrounds/bg/background.png') # стардантный фон леса
background = pygame.transform.scale(background, [WIDTH, HEIGHT])

background1 = pygame.image.load('assets/images/backgrounds/bg/dark_forest.png') # фон внезапной головы(в начале)
background1 = pygame.transform.scale(background1, [WIDTH, HEIGHT])

background5 = pygame.image.load('assets/images/backgrounds/bg/dark_forest.jpeg') # фон лесника и охотника
background5 = pygame.transform.scale(background5, [WIDTH, HEIGHT])

background2 = pygame.image.load('assets/images/backgrounds/bg/pupet_wizard_background.png') # фон куклы кодуна
background2 = pygame.transform.scale(background2, [WIDTH, HEIGHT])

background3 = pygame.image.load('assets/images/backgrounds/bg/room_zish.png') # комната злодея(начало и конец злодея и шапки)
#background3 = pygame.transform.scale(background3, [WIDTH, HEIGHT])

background4 = pygame.image.load('assets/images/backgrounds/bg/market.png') # базар (злодей и шапка)
background4 = pygame.transform.scale(background4, [WIDTH, HEIGHT])

# фон на данный момент
bg_now = background
bg_now_coords_x = 0

# Кнопка начала игры
start_btn = pygame.image.load('assets/images/кнопки/play_btn.png')
start_btn = pygame.transform.scale(start_btn, [278, 80])
start_rect = start_btn.get_rect()
start_rect.x = WIDTH // 2 - (278//2)
start_rect.y = HEIGHT // 2 + 65

# Кнопка просмотра управления
management_btn = pygame.image.load('assets/images/кнопки/management_btn.png')
management_btn = pygame.transform.scale(management_btn, [278, 80])
management_btn_rect = management_btn.get_rect()
management_btn_rect.x = WIDTH // 2 - (278//2)
management_btn_rect.y = HEIGHT // 2 + 160

# Кнопка выхода из игры
exit_btn = pygame.image.load('assets/images/кнопки/exit_btn.png')
exit_btn = pygame.transform.scale(exit_btn, [278, 80])
exit_rect = exit_btn.get_rect()
exit_rect.x = WIDTH // 2 - (278//2)
exit_rect.y = HEIGHT // 2 + 255

# Фон просмотра управления
management_bg = pygame.image.load('assets/images/backgrounds/менюшки/management_bg.png')

# песни альбома "Камнем по голове"
villain_and_hat = pygame.image.load('assets/images/Камнем по голове/Злодей и Шапка.png')
villain_and_hat = pygame.transform.scale(villain_and_hat, [100, 100])
villain_and_hat_rect = villain_and_hat.get_rect()
villain_and_hat_rect.x = 300
villain_and_hat_rect.y = 250 # 150

sudden_head_img = pygame.image.load('assets/images/Камнем по голове/Внезапная голова.png')
sudden_head_img = pygame.transform.scale(sudden_head_img, [100, 100])
sudden_head_rect = sudden_head_img.get_rect()
sudden_head_rect.x = 550
sudden_head_rect.y = 250 # 150

fool_and_lightning = pygame.image.load('assets/images/Камнем по голове/дурак и молния.png')
fool_and_lightning = pygame.transform.scale(fool_and_lightning, [100, 100])
fool_and_lightning_rect = fool_and_lightning.get_rect()
fool_and_lightning_rect.x = WIDTH-400
fool_and_lightning_rect.y = 250 # 150

# песни альбома "Будь как дома путник"
forester_img = pygame.image.load("assets/images/Будь как дома путник/Лесник.png")
forester_img = pygame.transform.scale(forester_img, [100, 100])
forester_img_rect = forester_img.get_rect()
forester_img_rect.x = 300
forester_img_rect.y = 150

# песни из Акустического альбома
puppet_of_wizard = pygame.image.load('assets/images/Акустический альбом/кукла колдуна.png')
puppet_of_wizard = pygame.transform.scale(puppet_of_wizard, [100, 100])
puppet_of_wizard_rect = puppet_of_wizard.get_rect()
puppet_of_wizard_rect.x = 300
puppet_of_wizard_rect.y = 150

villain_and_hat_map = [
    'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
    's               s                                        ',  
    's               s                                        ',
    's               s                                        ',
    's               s                                        ',
    's                                                        ',
    's                                                        ',
    's                                                        ',
    'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
    'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
    'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
    '---------------------------------------------------------',
    '---------------------------------------------------------',
]

grasses = []
dirts = []
stones = []
boards = []
stone_bricks = []

map_now = villain_and_hat_map
run = False
frame = 0

choice_lvl = False
choice_lvl2 = False

# сдвижение карты при движении игрока
testy = 2 # сдвижение по оси y
test = 2 # сдвижение по оси x

camera_x = 0

# Управление
def move(character_rect, speed):
    global jump, jump_count, on_grass, on_board, on_brick, testy, test, bg_now_coords_x

    keys = pygame.key.get_pressed()

    # Горизонтальное движение
    change_x = 0
    if keys[pygame.K_a]:  # Движение влево
        change_x = -speed
        test += 10
        bg_now_coords_x += 10

    if keys[pygame.K_d]:  # Движение вправо
        change_x = speed
        test -= 10
        

    # Прыжок
    if keys[pygame.K_SPACE] and on_grass:
        jump = True
        jump_count = jump_max
        on_grass = False
        on_board = False
        on_brick = False

    # Применение гравитации и прыжка
    if jump:
        character_rect.y -= jump_count
        jump_count -= 15  # Уменьшаем силу прыжка (эмуляция гравитации)
        if jump_count <= 0:
            jump = False
    else:
        character_rect.y += 15  # Гравитация, если не прыгаем

    # Остановка персонажа на земле
    if character_rect.y + character_rect.height >= HEIGHT:
        character_rect.y = HEIGHT - character_rect.height
        on_grass = True  # Персонаж стоит на земле
        on_board = True 
        on_brick = False
        jump = False  # Запрещаем дальнейшее падение
        jump_count = 0  # Сбрасываем счётчик прыжка

    # Ограничение персонажа по X, чтобы он не уходил за пределы экрана
    if character_rect.x + change_x < 0:  # Левый край экрана
        character_rect.x = 0
    elif character_rect.x + change_x > WIDTH - character_rect.width:  # Правый край экрана
        character_rect.x = WIDTH - character_rect.width
    else:
        character_rect.x += change_x  # Обновление позиции    

        # Обновление позиции
        character_rect.x += change_x

# альбом камнем по голове
alb1_selected = False  # Отвечает за состояние выбора альбома
villian_and_hat_lvl = False  # Отвечает за выбор уровня Злодей и шапка

main_menu = True       # Начинаем с главного меню

while True:
    man_old = gorshok_rect.copy()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        # Обрабатываем нажатия клавиш
        if event.type == pygame.KEYDOWN:
            '''if event.key == pygame.K_SPACE:
                show = False
                jump = True
                jump_count = jump_max
                on_grass = False
                if gorshok_rect.y <= 460:
                    testy += 20'''
            
            if event.key == pygame.K_ESCAPE:
                main_menu = True
                choice_menu = False
                choice_menu2 = False
                alb1_selected = False  # Сброс состояния альбома
                villian_and_hat_lvl = False  # Сброс уровня
                # ................................... НЕ ЗАБУДЬ ПРО ОСТАЛЬНЫЕ УРОВНИ
                gorshok_rect.x = randint(0, WIDTH)
                gorshok_rect.y = 776
        
        # Обрабатываем клики мыши
        if event.type == pygame.MOUSEBUTTONUP:
            pos = event.pos

            if main_menu:
                if start_rect.collidepoint(pos):
                    main_menu = False
                    choice_menu = True
                    choice_menu2 = False
                elif exit_rect.collidepoint(pos):
                    exit()
                elif management_btn_rect.collidepoint(pos):
                    window.blit(management_bg, [0, 0])

            # альбом камнем по голове
            elif choice_menu and not alb1_selected:
                if alb1_rect.collidepoint(pos):
                    choice_menu = False
                    choice_menu2 = True
                    alb1_selected = True  # Фиксируем выбор альбома
            
            elif alb1_selected:
                if villain_and_hat_rect.collidepoint(pos):
                    print("Выбран уровень: Злодей и шапка")
                    map_now = villain_and_hat_map
                    bg_now = background3
                    villian_and_hat_lvl = True
                    sudden_head_lvl = False  # Отключаем другой уровень
                    print(f"villinan_and_hat_lvl: {villian_and_hat_lvl}, sudden_head_lvl: {sudden_head_lvl}")

               
    # Тута рисуем главное меню
    if main_menu:
        window.blit(menu, [0, 0])
        pygame.mixer.music.load("assets/sounds/KingAndFool.mp3")
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)
        window.blit(start_btn, start_rect)
        window.blit(exit_btn, exit_rect)
        window.blit(management_btn, management_btn_rect)
    
    # здеся рисуем все альбомы
    elif choice_menu and not alb1_selected:
        window.blit(choice2, [0, 0])
        window.blit(alb1_img, alb1_rect)

    # здеся рисуем песни альбома Камнем по голове
    elif alb1_selected and not villian_and_hat_lvl:  
        window.blit(choice, [0, 0])
        window.blit(villain_and_hat, villain_and_hat_rect)
        window.blit(sudden_head_img, sudden_head_rect)
        window.blit(fool_and_lightning, fool_and_lightning_rect)

    elif villian_and_hat_lvl:  # Если уровень Злодей и Шапка выбран, рисуем его
        pygame.mixer.music.pause()
        window.blit(bg_now, [bg_now_coords_x, 0])
        move(villian_rect, speed)
        for i in range(len(map_now)):
            for j in range(len(map_now[i])):
                if map_now[i][j] == 'b':
                    board_rect = board.get_rect()
                    board_rect.x = board_rect.width * j + test
                    board_rect.y = board_rect.height * i + testy
                    boards.append(board_rect)
                    window.blit(board, board_rect)   
                elif map_now[i][j] == 's':
                    stone_briks_rect = stone_briks_img.get_rect()
                    stone_briks_rect.x = stone_briks_rect.width * j + test
                    stone_briks_rect.y = stone_briks_rect.height *i + testy
                    stone_bricks.append(stone_briks_rect)
                    window.blit(stone_briks_img, stone_briks_rect)
        window.blit(villian_now, villian_rect)
        pygame.display.update()
                    
    else:       

        #print(pygame.mouse.get_pos())

        if jump == True:
            gorshok_rect.y -= jump_count
            if gorshok_rect.y >= jump_max:
                jump = False
            if gorshok_rect.y >= 900:
                testy -= 20     

        #if jump_count > -jump_max or (man_rect.bottom < HEIGHT and on_grass == False):
            #jump_count -= 1
            
        else:
            jump = False
            on_grass = True
               
            # gorshok_rect.x += change_x
        
    pygame.display.update()
    clock.tick(FPS)