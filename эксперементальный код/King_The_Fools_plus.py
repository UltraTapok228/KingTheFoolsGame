import pygame
from random import randint
import time

pygame.init()

WIDTH = 1200
HEIGHT = 700

window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption('King The Fools')

FPS = 120
clock = pygame.time.Clock()

# Иконка игры
icon_img = pygame.image.load('icon.png')
pygame.display.set_icon(icon_img)

# СОЗДАЁМ ТЕКСТУРЫ
platform_img = pygame.image.load('компоненты локации/grass.png')
platform_img = pygame.transform.scale(platform_img, [70, 70])

stone_briks_img = pygame.image.load('компоненты локации/stone_bricks.png')

dirt_img = pygame.image.load('компоненты локации/dirt.png')
stone_img = pygame.image.load('компоненты локации/stone.png')
stone_img = pygame.transform.scale(stone_img, [70, 70])

# Картинки для альбомов
fool_and_lightning = pygame.image.load('Камнем по голове/дурак и молния.png')
fool_and_lightning = pygame.transform.scale(fool_and_lightning, [100, 100])
fool_and_lightning_rect = fool_and_lightning.get_rect()
fool_and_lightning_rect.x = 300
fool_and_lightning_rect.y = 150

# Главный цикл игры
main_menu = True
choice_menu = False
choice_menu2 = False
choice_lvl = False
choice_lvl2 = False
count_click = 0

# Кнопки
start_btn = pygame.image.load('кнопки/play_btn.png')
start_btn = pygame.transform.scale(start_btn, [278, 80])
start_rect = start_btn.get_rect()
start_rect.x = WIDTH // 2 - (278 // 2)
start_rect.y = HEIGHT // 2 + 65

exit_btn = pygame.image.load('кнопки/exit_btn.png')
exit_btn = pygame.transform.scale(exit_btn, [278, 80])
exit_rect = exit_btn.get_rect()
exit_rect.x = WIDTH // 2 - (278 // 2)
exit_rect.y = HEIGHT // 2 + 255

# Фон игры
menu = pygame.image.load('backgrounds/менюшки/menu.png')
menu = pygame.transform.scale(menu, [1200, 700])

# Игровой персонаж
man_stand = pygame.image.load('персонажи/man.png')
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
jump_max = 50
jump_count = 0

# Логика игры
def move():
    global change_x, man

    man_rect.x += change_x
    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
        change_x = speed
        man = man_stand
    elif keys[pygame.K_a]:
        change_x = -speed
        man = man_left
    else:
        change_x = 0

# Главный игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jump = True
                jump_count = jump_max
            if event.key == pygame.K_ESCAPE:
                main_menu = True
                choice_menu = False
                choice_menu2 = False
                man_rect.x = randint(0, WIDTH)
                man_rect.y = 776

    if main_menu:
        window.blit(menu, [0, 0])
        window.blit(start_btn, start_rect)
        window.blit(exit_btn, exit_rect)

        # Позиция указателя мыши
        pos = pygame.mouse.get_pos()

        # Обработка нажатий на кнопки
        if start_rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == 1:
            main_menu = False
            choice_menu = True
        elif exit_rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == 1:
            exit()

    elif choice_menu:
        window.fill((0, 0, 0))  # Заполнение фона черным
        window.blit(fool_and_lightning, fool_and_lightning_rect)

        pos = pygame.mouse.get_pos()

        # Проверка кликов на кнопку "дурак и молния"
        if fool_and_lightning_rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == 1:
            print("Вы выбрали 'Дурак и молния'")
            choice_menu = False
            choice_menu2 = True
            choice_lvl = True

    elif choice_menu2:
        window.fill((0, 0, 0))  # Очистка экрана
        window.blit(fool_and_lightning, fool_and_lightning_rect)

    move()  # Движение персонажа

    # Прыжок
    if jump:
        man_rect.y -= jump_count
        if man_rect.y <= jump_max:
            jump = False

    if man_rect.bottom > HEIGHT:
        man_rect.bottom = HEIGHT
        jump = False

    # Отрисовка персонажа
    window.blit(man, man_rect)

    pygame.display.update()
    clock.tick(FPS)
