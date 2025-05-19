import pygame
from random import randint
import random
import time


pygame.init()

WIDTH = 1200
HEIGHT = 700
VIRTUAL_RES = (WIDTH, HEIGHT)
'''pygame.FULLSCREEN,'''

window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption('King The Fools')

FPS = 120
clock = pygame.time.Clock()

# иконка игры
icon_img = pygame.image.load('assets/images/icons/icon.png')
pygame.display.set_icon(icon_img)

# Персонажи игры
person_now = None
# Горшок
gorshok_stand = pygame.image.load('assets/images/персонажи/gorshok.png')
gorshok_left = pygame.transform.flip(gorshok_stand, True, False)

gorshok_stand.set_colorkey([163,73,164])
gorshok_left.set_colorkey([163,73,164])
man_now = gorshok_stand

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
grass_img = pygame.image.load('assets/images/компоненты локации/grass.png') # символ в массиве "g"

stone_bricks_img = pygame.image.load('assets/images/компоненты локации/stone_bricks.png') # символ в массиве "s"

dirt_img = pygame.image.load('assets/images/компоненты локации/dirt.png') # символ в массиве "з"

stone_img = pygame.image.load('assets/images/компоненты локации/stone.png') # символ в массиве "с" (кириллица)

board_img = pygame.image.load('assets/images/компоненты локации/boards.png') # символ в массиве "b"

board2_img = pygame.image.load('assets/images/компоненты локации/boards2.png') # символ в массиве "б"

tree_img = pygame.image.load('assets/images/компоненты локации/tree.png') # символ в массиве "t"
tree_left_img = pygame.transform.rotate(tree_img, 90)

door1_img = pygame.image.load('assets/images/компоненты локации/door1.png') # символ в массиве "1"
door2_img = pygame.image.load('assets/images/компоненты локации/door2.png') # символ в массиве "2"

plant1_img = pygame.image.load('assets/images/компоненты локации/plant1.png') # символ в массиве "$"
plant2_img = pygame.image.load('assets/images/компоненты локации/plant2.png') # символ в массиве "%"

tablet_img = pygame.image.load('assets/images/компоненты локации/tablet_villian_and_hat.png') # символ в массиве "y"(игрек)
tablet_img.set_colorkey([0,0,0])

market_tablet_img = pygame.image.load('assets/images/компоненты локации/market_tablet.png') # символ в массиве "Y"
market_tablet_img.set_colorkey([0,0,0])

barrel1_img = pygame.image.load('assets/images/компоненты локации/barrel1.png') # cимвол в массиве "#"
barrel1_img = pygame.transform.scale(barrel1_img, (70, 70))

barrel2_img = pygame.image.load('assets/images/компоненты локации/barrel2.png') # cимвол в массиве "№"
barrel2_img = pygame.transform.scale(barrel2_img, (70, 70))

barrel3_img = pygame.image.load('assets/images/компоненты локации/barrel3.png') # cимвол в массиве "?"
barrel3_img = pygame.transform.scale(barrel3_img, (70, 70))

barrel4_img = pygame.image.load('assets/images/компоненты локации/barrel4.png') # cимвол в массиве "&"
barrel4_img = pygame.transform.scale(barrel4_img, (70, 70))

chest_img = pygame.image.load('assets/images/компоненты локации/chest.png') # символ в массиве "h"
chest_img = pygame.transform.scale(chest_img, (70, 70))

wall_img = pygame.image.load('assets/images/компоненты локации/wall.png') # символ в массиве "w"
window_img = pygame.image.load('assets/images/компоненты локации/window.png') # символ в массиве "W"

lightning_bag = pygame.image.load('assets/images/компоненты локации/bag_for_lightnig.png') # символ в массиве "L"
lightning_bag = pygame.transform.scale(lightning_bag, (70, 70))

old_watch_img = pygame.image.load('assets/images/компоненты локации/old_watch.png') # символ в массиве "o" кириллица
old_watch_img = pygame.transform.scale(old_watch_img, (70, 70))

# шапки для злодей и шапка
hat_img = pygame.image.load('assets/images/компоненты локации/hat.png') # символ в массиве "п"
hat_img = pygame.transform.scale(hat_img, (70, 70))

hat2_img = pygame.image.load('assets/images/компоненты локации/hat2.png') # символ в массиве "ш"
hat2_img = pygame.transform.scale(hat2_img, (70, 70))


# плэйт позволяющий сменить локацию
next_location = pygame.image.load('assets/images/компоненты локации/next_location.png') # символ в массиве "e" (латиница)

next_location_2 = pygame.image.load('assets/images/компоненты локации/next_location2.png') # символ в массиве "q"
next_location2_rect = next_location_2.get_rect()

# альбомы
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

background4 = pygame.image.load('assets/images/backgrounds/bg/market.png') # базар (злодей и шапка)
background4 = pygame.transform.scale(background4, [WIDTH, HEIGHT])

village_bg = pygame.image.load('assets/images/backgrounds/bg/village_bg.png') # деревня (злодей и шапка)
seller_of_nightmares_bg = pygame.image.load('assets/images/backgrounds/bg/seller_of_nightmares_house.png') # дом продавца кошмаров

seller_of_nightmares_inside_bg = pygame.image.load('assets/images/backgrounds/bg/seller_of_nightmares_house_inside.png')

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

# Кнопка входа в дом продавца кошмаров
entrance_to_house_btn = pygame.image.load('assets/images/кнопки/entrance_to_house_btn.jpg')
entrance_to_house_btn = pygame.transform.scale(entrance_to_house_btn, [278, 80])
entrance_to_house_rect = entrance_to_house_btn.get_rect()
entrance_to_house_rect.x = WIDTH // 2 - (entrance_to_house_rect.width//2)
entrance_to_house_rect.y = HEIGHT // 2 - (entrance_to_house_rect.height//2) 

# диалоговое окно
dialog_window_img = pygame.image.load('assets/images/interface/dialog_window.png') 
show_dialog = False

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

# шрифты
cyrillic_old_font = pygame.font.Font('fonts/CyrillicOld.otf', 20)

# тексты и реплики

text_villian_and_hat = "Шапка, да не просто шапка,"
text_surface_villian_and_hat = cyrillic_old_font.render(text_villian_and_hat, True, (255, 243, 0))  # Создаем поверхность с текстом
text_rect_villian_and_hat = text_surface_villian_and_hat.get_rect(center=(550, 400))  # Центрируем текст по X и Y

text_villian_and_hat_2 = "в свое время сам Великий Карл ее носил!"
text_surface_villian_and_hat_2 = cyrillic_old_font.render(text_villian_and_hat_2, True, (255, 243, 0))  # Создаем поверхность с текстом
text_rect_villian_and_hat_2 = text_surface_villian_and_hat_2.get_rect(center=(550, 400))  # Центрируем текст по X и Y

text_villian_and_hat_3 = "Обычный, черный и помятый цилиндр"
text_surface_villian_and_hat_3 = cyrillic_old_font.render(text_villian_and_hat_3, True, (255, 243, 0))  # Создаем поверхность с текстом
text_rect_villian_and_hat_3 = text_surface_villian_and_hat_3.get_rect(center=(550, 400))  # Центрируем текст по X и Y

text_villian_ant_hat_4 = "Волшебная сумка, способная поймать молнию"
text_surface_villian_and_hat_4 = cyrillic_old_font.render(text_villian_ant_hat_4, True, (255, 243, 0))  # Создаем поверхность с текстом
text_rect_villian_and_hat_4 = text_surface_villian_and_hat_4.get_rect(center=(550, 400))  # Центрируем текст по X и Y

text_villian_and_hat_5 = "    Таинственные часы, мистический "
text_surface_villian_and_hat_5 = cyrillic_old_font.render(text_villian_and_hat_5, True, (255, 243, 0))  # Создаем поверхность с текстом
text_rect_villian_and_hat_5 = text_surface_villian_and_hat_5.get_rect(center=(550, 400))  # Центрируем текст по X и Y

text_villian_and_hat_6 = "         проводник с прошлым..."
text_surface_villian_and_hat_6 = cyrillic_old_font.render(text_villian_and_hat_6, True, (255, 243, 0))  # Создаем поверхность с текстом
text_rect_villian_and_hat_6 = text_surface_villian_and_hat_6.get_rect(center=(550, 400))  # Центрируем текст по X и Y

villain_and_hat_map = [
    'sbbbbbbbbbbbbbsbbbbbbbbbsbbbsss',
    's             s         s   sss',  
    's             s         s   sss',
    's             s         s   sss',
    's             s         s   sss',
    's                           sss',
    's                         1 sss',
    's                         2 sss',
    'sbbbbbbbbbbbbbbbbbbbbbbbbbebsss',
    'sbbbbbbbbbbbbbbbbbbbbbbbbbbbsss',
    'sbbbbbbbbbbbbbbbbbbbbbbbbbbbsss',
    '-------------------------------',
    '-------------------------------',
]

villain_and_hat_map_2 = [
    'wwwwwwwwwwwwwwwwwwwwwwwt                                   twwwwwww',
    'wwwwwwwwwwwwwwwwwwwwwWwt                                   twWwwwww',
    'wwwwwwwwwwwwwwwwwwwwwWwt                                   twWwwwww',
    'wwwwwwwwwwwwwwwwwwwwwwwt                                   twwwwwww',
    'TTTTTTTTTTTTTTTTTTTTTTTT                                   TTTTTTTT',
    'wwwwwwwwwwwwwwwwwwwwwws                                     swwwwww',
    'wwwwwwwwwwwwwwwwwwwWwws                                     swwwwww',
    'wwwwwwwwwwwwwwwwwwwWww1                                     swwwwww',
    'wwwwwwwwwwwwwwwwwwwwww2   y  $ % $% $   %%   %$$ $%         swwwwww',
    'sssssssssssssssssssssssgggggggggggggggggggggggggggggggggqgggsssssss',
    'ззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззз',
    'ззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззз',
    'ззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззз' 
]

villain_and_hat_map_3 = [
    '                                                                                                             ',
    '                                                                                                             ',
    '                                                                                                             ',
    '                                                                                                             ',
    '                                                                                                             ',
    '                                                                                                             ',
    '                                                                                                             ',
    '                                                                                                             ',
    '   %    $$     $%   %      $$ %     %    $     $ %    %%    $    %   $   $      $%      $         %%   $     ',
    'ggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg',
    'ззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззз',
    'ззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззз',
    'ззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззззз'
]

villain_and_hat_map_4 = [
    'sssssssssssssssssssssssssssssssssssssssssssssssssssst                                                                    tsssssssssssssss',
    'sssssssssssssssssssssssssssssssssssssssssssssssssssst                                                                    tsssssssssssssss',
    'sssssssssssssssssssssssssssssssssssssssssssssssssssst                                                                    tsssssssssssssss',
    'sssssssssssssssssssssssssssssssssssssssssssssssssssst                                                                    tsssssssssssssss',
    'sssssssssssssssssssssssssssssssssssssssssssssssssssst                                                                    tsssssssssssssss',
    'sssssssssssssssssssssssssssssssssssssssssssssssssssst                                                                    tsssssssssssssss',
    'sssssssssssssssssssssssssssssssssssssssssssssssssssst                                                                    tsssssssssssssss',
    'ssssssssssssssssssssssssssssssssssssssssssssssssssss1           h          п ш      о                                    tsssssssssssssss',
    'ssssssssssssssssssssssssssssssssssssssssssssssssssss2           hhL&       h h      h                                    tsssssssssssssss',
    'сссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссtsssssssssssssss',
    'сссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссtsssssssssssssss',
    'сссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссtsssssssssssssss',
    'сссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссtsssssssssssssss'
]

grasses = []
dirts = []
stones = []
boards = []
boards2 = []
stone_bricks = []
trees = []
doors1 = []
doors2 = []
plants1 = []
plants2 = []
tablets = []
market_tablets = []
next_lvl = []
next_lvl_2 = []
barrels_1 = []
barrels_2 = []
barrels_3 = []
barrels_4 = []
walls = []
windows = []
chests = []
bags = []
hats = []
watches = []
map_now = villain_and_hat_map
# run = False
# frame = 0

# сдвижение карты при движении игрока
testy = 2 # сдвижение по оси y
test = 2 # сдвижение по оси x

speed = 5
change_x = 0

location_switched = False

# Управление
def move(character_rect, character_left_rect, character_right_rect, speed):
    global jump, jump_count, on_grass, on_board, on_brick, testy, test, bg_now_coords_x, person_now

    keys = pygame.key.get_pressed()

    # Горизонтальное и вертикальное движение
    change_x = 0
    change_y = 0

    if keys[pygame.K_a]:  # Движение влево
        person_now = character_left_rect  # Обновляем спрайт для движения влево
        change_x = -speed
        if character_rect.x <= 200:
            test += speed
            bg_now_coords_x += speed
    if keys[pygame.K_d]:  # Движение вправо
        person_now = character_right_rect  # Обновляем спрайт для движения вправо
        change_x = speed
        if character_rect.x >= (WIDTH - character_rect.width)-200:
            character_rect.x >= (WIDTH - character_rect.width)-200
            test -= speed
            bg_now_coords_x -= speed
    
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
    if character_rect.x + change_x < 200:  # Левый край экрана
        character_rect.x = 200
        test += 6
        bg_now_coords_x += 6
    elif character_rect.x + change_x > (WIDTH - character_rect.width)-200:  # Правый край экрана
        character_rect.x = (WIDTH - character_rect.width)-200
        test -= 6
        bg_now_coords_x -= 6
    else:
        character_rect.x += change_x  # Обновление позиции

# альбом камнем по голове
alb1_selected = False  # Отвечает за состояние выбора альбома
villian_and_hat_lvl = False  # Отвечает за выбор уровня Злодей и шапка

main_menu = True       # Начинаем с главного меню

while True:
    #man_old = gorshok_rect.copy()
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            exit()

        # Обрабатываем нажатия клавиш
        if event.type == pygame.KEYDOWN:
            
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
                    pygame.mixer.music.load("assets/sounds/Злодей и шапка.mp3")
                    pygame.mixer.music.set_volume(0.05)
                    pygame.mixer.music.play(-1)
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

    villian_and_hat_music = False
    
    if villian_and_hat_lvl:  # Если уровень Злодей и Шапка выбран, рисуем его
        
        person_now = villian

        window.blit(bg_now, [bg_now_coords_x, 0])
        move(villian_rect, villian_left, villian, speed)
        change_x = 50
        for i in range(len(map_now)):
            for j in range(len(map_now[i])):
                if map_now[i][j] == 'b':
                    board_rect = board_img.get_rect()
                    board_rect.x = board_rect.width * j + test
                    board_rect.y = board_rect.height * i + testy
                    boards.append(board_rect)
                    window.blit(board_img, board_rect)   
                elif map_now[i][j] == 's':
                    stone_briks_rect = stone_bricks_img.get_rect()
                    stone_briks_rect.x = stone_briks_rect.width * j + test
                    stone_briks_rect.y = stone_briks_rect.height * i + testy
                    stone_bricks.append(stone_briks_rect)
                    window.blit(stone_bricks_img, stone_briks_rect)   
                elif map_now[i][j] == 'g':
                    grass_rect = grass_img.get_rect()
                    grass_rect.x = grass_rect.width * j + test
                    grass_rect.y = grass_rect.height * i + testy
                    grasses.append(grass_rect)
                    window.blit(grass_img, grass_rect)
                elif map_now[i][j] == 'з':
                    dirt_rect = grass_img.get_rect()
                    dirt_rect.x = grass_rect.width * j + test
                    dirt_rect.y = grass_rect.height * i + testy
                    dirts.append(dirt_rect)
                    window.blit(dirt_img, dirt_rect)
                elif map_now[i][j] == 't':
                    tree_rect = tree_img.get_rect()
                    tree_rect.x = tree_rect.width * j + test
                    tree_rect.y = tree_rect.height * i + testy
                    trees.append(tree_rect)
                    window.blit(tree_img, tree_rect)
                elif map_now[i][j] == 'б':
                    board2_rect = board2_img.get_rect()
                    board2_rect.x = board2_rect.width * j + test
                    board2_rect.y = board2_rect.height * i + testy
                    boards2.append(board2_rect)
                    window.blit(board2_img, board2_rect)
                elif map_now[i][j] == '1':
                    door1_rect = door1_img.get_rect()
                    door1_rect.x = door1_rect.width * j + test
                    door1_rect.y = door1_rect.height * i + testy
                    doors1.append(door1_rect)
                    window.blit(door1_img, door1_rect)
                elif map_now[i][j] == '2':
                    door2_rect = door1_img.get_rect()
                    door2_rect.x = door2_rect.width * j + test
                    door2_rect.y = door2_rect.height * i + testy
                    doors2.append(door2_rect)
                    window.blit(door2_img, door2_rect)
                elif map_now[i][j] == '$':
                    plant1_rect = plant1_img.get_rect()
                    plant1_rect.x = plant1_rect.width * j + test
                    plant1_rect.y = plant1_rect.height * i + testy
                    plants1.append(plant1_rect)
                    window.blit(plant1_img, plant1_rect)
                elif map_now[i][j] == '%':
                    plant2_rect = plant2_img.get_rect()
                    plant2_rect.x = plant2_rect.width * j + test
                    plant2_rect.y = plant2_rect.height * i + testy
                    plants2.append(plant2_rect)
                    window.blit(plant2_img, plant2_rect)
                elif map_now[i][j] == 'y':
                    tablet_rect = tablet_img.get_rect()
                    tablet_rect.x = tablet_rect.width * j + test
                    tablet_rect.y = tablet_rect.height * i + testy
                    tablets.append(tablet_rect)
                    window.blit(tablet_img, tablet_rect)
                elif map_now[i][j] == 'Y':
                    market_tablet_rect = market_tablet_img.get_rect()
                    market_tablet_rect.x = market_tablet_rect.width * j + test
                    market_tablet_rect.y = market_tablet_rect.height * i + testy
                    market_tablets.append(market_tablet_rect)
                    window.blit(market_tablet_img, market_tablet_rect)
                elif map_now[i][j] == 'e':
                    next_location_rect = next_location.get_rect()
                    next_location_rect.x = next_location_rect.width * j + test
                    next_location_rect.y = next_location_rect.height * i + testy
                    next_lvl.append(next_location_rect)
                    window.blit(next_location, next_location_rect)
                elif map_now[i][j] == 'q':
                    next_location2_rect = next_location_2.get_rect()
                    next_location2_rect.x = next_location2_rect.width * j + test
                    next_location2_rect.y = next_location2_rect.height * i + testy
                    next_lvl_2.append(next_location2_rect)
                    window.blit(next_location_2, next_location2_rect) 
                elif map_now[i][j] == '#':  
                    barrel1_rect = barrel1_img.get_rect()
                    barrel1_rect.x = barrel1_rect.width * j + test
                    barrel1_rect.y = barrel1_rect.height * i + testy
                    barrels_1.append(barrel1_rect)
                    window.blit(barrel1_img, barrel1_rect)
                elif map_now[i][j] == '№':
                    barrel2_rect = barrel2_img.get_rect()
                    barrel2_rect.x = barrel2_rect.width * j + test
                    barrel2_rect.y = barrel2_rect.height * i + testy
                    barrels_2.append(barrel2_rect)
                    window.blit(barrel2_img, barrel2_rect)    
                elif map_now[i][j] == '?':
                    barrel3_rect = barrel3_img.get_rect()
                    barrel3_rect.x = barrel3_rect.width * j + test
                    barrel3_rect.y = barrel3_rect.height * i + testy
                    barrels_3.append(barrel3_rect)
                    window.blit(barrel3_img, barrel3_rect)
                elif map_now[i][j] == '&':
                    barrel4_rect = barrel4_img.get_rect()
                    barrel4_rect.x = barrel4_rect.width * j + test
                    barrel4_rect.y = barrel4_rect.height * i + testy
                    barrels_4.append(barrel4_rect)
                    window.blit(barrel4_img, barrel4_rect)
                elif map_now[i][j] == 'w':
                    wall_rect = wall_img.get_rect()
                    wall_rect.x = wall_rect.width * j + test
                    wall_rect.y = wall_rect.height * i + testy
                    walls.append(wall_rect)
                    window.blit(wall_img, wall_rect)
                elif map_now[i][j] == 'W':
                    window_rect = window_img.get_rect()
                    window_rect.x = wall_rect.width * j + test
                    window_rect.y = wall_rect.height * i + testy
                    windows.append(window_rect)
                    window.blit(window_img, window_rect)
                elif map_now[i][j] == 'T':
                    tree_left_rect = tree_left_img.get_rect()
                    tree_left_rect.x = tree_left_rect.width * j + test
                    tree_left_rect.y = tree_left_rect.height * i + testy
                    trees.append(tree_left_rect)
                    window.blit(tree_left_img, tree_left_rect)
                elif map_now[i][j] == 'с':
                    stone_rect = stone_img.get_rect()
                    stone_rect.x = stone_rect.width * j + test
                    stone_rect.y = stone_rect.height * i + testy
                    stones.append(stone_rect)
                    window.blit(stone_img, stone_rect)
                elif map_now[i][j] == 'h':
                    chest_rect = chest_img.get_rect()
                    chest_rect.x = chest_rect.width * j + test
                    chest_rect.y = chest_rect.height * i + testy
                    chests.append(chest_rect)
                    window.blit(chest_img, chest_rect)
                elif map_now[i][j] == 'L':
                    bag_lightning_rect = lightning_bag.get_rect()
                    bag_lightning_rect.x = bag_lightning_rect.width * j + test
                    bag_lightning_rect.y = bag_lightning_rect.height * i + testy
                    bags.append(lightning_bag)
                    window.blit(lightning_bag, bag_lightning_rect)
                elif map_now[i][j] == 'п':
                    hat_rect = hat_img.get_rect()
                    hat_rect.x = hat_rect.width * j + test
                    hat_rect.y = hat_rect.height * i + testy
                    hats.append(hat_img)
                    window.blit(hat_img, hat_rect)
                elif map_now[i][j] == 'ш':
                    hat2_rect = hat2_img.get_rect()
                    hat2_rect.x = hat2_rect.width * j + test
                    hat2_rect.y = hat2_rect.height * i + testy
                    hats.append(hat2_img)
                    window.blit(hat2_img, hat2_rect)
                elif map_now[i][j] == 'о':
                    old_watch_rect = old_watch_img.get_rect()
                    old_watch_rect.x = old_watch_rect.width * j + test
                    old_watch_rect.y = old_watch_rect.height * i + testy
                    watches.append(old_watch_img)
                    window.blit(old_watch_img, old_watch_rect)
                    
    if villian_and_hat_lvl:
        # Перемещаем проверку столкновения внутрь блока villian_and_hat_lvl
        try:        
            # переход из дома злодея на улицу
            if next_location_rect.collidepoint(pos):
                location_switched = True
                bg_now = village_bg
                bg_now_coords_x = 0
                map_now = villain_and_hat_map_2
                change_x = 50
                
        
        except NameError:
            pass # Игнорируем ошибку, если next_location_rect ещё не определён

        mouse_pos = pygame.mouse.get_pos()

        try:
            # переход с улицы к дому продавца кошмаров
            if next_location2_rect.collidepoint(pos):
                location_switched = True
                bg_now = seller_of_nightmares_bg
                bg_now_coords_x = 0
                map_now = villain_and_hat_map_3
                change_x = 50
                window.blit(entrance_to_house_btn, entrance_to_house_rect)
            # переход в дом продавца кошмаров
            if entrance_to_house_rect.collidepoint(pos):
                location_switched = True
                bg_now = seller_of_nightmares_inside_bg
                map_now = villain_and_hat_map_4
                bg_now_coords_x = 0
                change_x = 50

            if hat2_rect.collidepoint(mouse_pos):
                window.blit(dialog_window_img, [400, 300])
                window.blit(text_surface_villian_and_hat, [420, 320])
                window.blit(text_surface_villian_and_hat_2, [420, 340])

            if hat_rect.collidepoint(mouse_pos):
                window.blit(dialog_window_img, [400, 300])
                window.blit(text_surface_villian_and_hat_3, [420, 320])

            if bag_lightning_rect.collidepoint(mouse_pos):
                window.blit(dialog_window_img, [400, 300])
                window.blit(text_surface_villian_and_hat_4, [410, 320])
            
            if old_watch_rect.collidepoint(mouse_pos):
                window.blit(dialog_window_img, [400, 300])
                window.blit(text_surface_villian_and_hat_5, [410, 320])
                window.blit(text_surface_villian_and_hat_6, [410, 340])

        except NameError:
            pass # Игнорируем ошибку, если next_location_rect2 ещё не определён

        window.blit(person_now, villian_rect)
        pygame.display.update()

    pygame.display.update()
    clock.tick(FPS)