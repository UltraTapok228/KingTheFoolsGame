import pygame
from random import randint

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 1200, 700
jump_max = 10

# Переменные состояния
main_menu = True
in_game = False
jump = False
jump_count = 0
on_platform = False
testy = 0
test = 0
map_now = []  # Карта уровня
platforms = []  # Платформы
dirts = []  # Земля

# Загрузка ресурсов
window = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.image.load("background.png")

menu = pygame.image.load('menu.jpg')
menu = pygame.transform.scale(menu, [1200, 700])

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

platform_img = pygame.image.load("grass.png")
dirt_img = pygame.image.load("dirt.png")
#background1 = pygame.image.load("pupet_wizard_background.png")

# экран загрузки
menu = pygame.image.load('menu.jpg')
menu = pygame.transform.scale(menu, [1200, 700])

choice = pygame.image.load('choice.png')
choice2 = pygame.image.load('choice2.png')

# Ресурсы уровней
alb1_img = pygame.image.load('alb1.png')
alb1_rect = alb1_img.get_rect()
alb1_rect.x = 300
alb1_rect.y = 150


# Позиция игрока
man_rect = pygame.Rect(400, 500, 50, 50)
change_x = 0

# Обработчик событий
def handle_events():
    global jump, jump_count, on_platform, main_menu, in_game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and on_platform:
                jump = True
                jump_count = jump_max
                on_platform = False

            if event.key == pygame.K_ESCAPE:
                main_menu = True
                man_rect.x = randint(0, WIDTH)
                man_rect.y = 776

# Отрисовка главного меню
def draw_main_menu():
    global main_menu, in_game
    window.blit(menu, (0, 0))
    window.blit(start_btn, start_rect)
    window.blit(exit_btn, exit_rect)

    pos = pygame.mouse.get_pos()

    # Начало игры при нажатии на кнопку "Старт"
    if start_rect.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
        main_menu = False
        in_game = False  # Переход в выбор уровня

    # Выход из игры при нажатии на кнопку "Выход"
    elif exit_rect.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
        pygame.quit()
        exit()

# Отрисовка выбора уровня
def draw_level_selection():
    global in_game, main_menu, map_now, platforms, dirts
    window.blit(choice2, (0, 0))
    window.blit(alb1_img, alb1_rect)
    pos = pygame.mouse.get_pos()

    # Если выбран первый уровень
    if alb1_rect.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
        in_game = True  # Игрок начал игру
        main_menu = False

        # Загрузка карты уровня
        map_now = map  # Предполагается, что где-то есть массив карты
        platforms.clear()
        dirts.clear()

        for i in range(len(map_now)):
            for j in range(len(map_now[i])):
                if map_now[i][j] == '*':
                    platform_rect = platform_img.get_rect()
                    platform_rect.x = platform_rect.width * j + test
                    platform_rect.y = platform_rect.height * i + testy
                    platforms.append(platform_rect)
                    window.blit(platform_img, platform_rect)

                elif map_now[i][j] == '-':
                    dirt_rect = dirt_img.get_rect()
                    dirt_rect.x = dirt_rect.width * j + test
                    dirt_rect.y = dirt_rect.height * i + testy
                    dirts.append(dirt_rect)
                    window.blit(dirt_img, dirt_rect)

# Обновление игровой логики (например, прыжок)
def update_game():
    global jump, jump_count
    man_rect.x += change_x

    if jump:
        if jump_count >= -jump_max:
            direction = 1 if jump_count > 0 else -1
            man_rect.y -= (jump_count ** 2) * 0.5 * direction
            jump_count -= 1
        else:
            jump = False

# Отрисовка игрового процесса
def draw_game():
    window.blit(menu, (0, 0))

    # Отрисовка платформ и земли
    for platform in platforms:
        window.blit(platform_img, platform)

    for dirt in dirts:
        window.blit(dirt_img, dirt)

    # Отрисовка игрока
    pygame.draw.rect(window, (255, 0, 0), man_rect)

# Основной цикл игры
def game_loop():
    global main_menu, in_game

    while True:
        handle_events()

        if main_menu:
            draw_main_menu()
        elif not main_menu and not in_game:
            draw_level_selection()
        elif in_game:
            update_game()
            draw_game()

        pygame.display.update()

# Запуск игры
game_loop()