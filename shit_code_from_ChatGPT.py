import pygame
import sys

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 1200, 700
FPS = 60

# Цвета
WHITE = (255, 255, 255)

# Загрузка изображений
icon = pygame.image.load("assets/images/icons/icon.png")
menu_bg = pygame.image.load("assets/images/backgrounds/менюшки/menu.png")
management_bg = pygame.image.load("assets/images/backgrounds/менюшки/management_bg.png")
choice2_bg = pygame.image.load("assets/images/backgrounds/менюшки/choice2.png")
choice_bg = pygame.image.load("assets/images/backgrounds/менюшки/choice.png")
coming_soon_bg = pygame.image.load("assets/images/backgrounds/менюшки/comming soon.png")

dirt = pygame.image.load("assets/images/компоненты локации/dirt.png")
grass = pygame.image.load("assets/images/компоненты локации/grass.png")
stone = pygame.image.load("assets/images/компоненты локации/stone.png")
stone_bricks = pygame.image.load("assets/images/компоненты локации/stone_bricks.png")
man = pygame.image.load("assets/images/персонажи/man.png")

# Загрузка кнопок
play_btn = pygame.image.load("assets/images/кнопки/play_btn.png")
management_btn = pygame.image.load("assets/images/кнопки/management_btn.png")
exit_btn = pygame.image.load("assets/images/кнопки/exit_btn.png")

album_buttons = [pygame.image.load(f"assets/images/обложки альбомов/alb{i}.png") for i in range(1, 10)]
levels_alb1 = [pygame.image.load("assets/images/Камнем по голове/Злодей и Шапка.png"), pygame.image.load("assets/images/Камнем по голове/Внезапная голова.png"), pygame.image.load("assets/images/Камнем по голове/дурак и молния.png")]
levels_alb2 = [pygame.image.load("assets/images/Акустический альбом/кукла колдуна.png"), pygame.image.load("assets/images/Акустический альбом/утренний рассвет.png")]

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Game")
pygame.display.set_icon(icon)

# Игровое состояние
state = "menu"
selected_album = None

def draw_menu():
    screen.blit(menu_bg, (0, 0))
    screen.blit(play_btn, (500, 250))
    screen.blit(management_btn, (500, 350))
    screen.blit(exit_btn, (500, 450))

def draw_management():
    screen.blit(management_bg, (0, 0))

def draw_album_selection():
    screen.blit(choice2_bg, (0, 0))
    for i, btn in enumerate(album_buttons):
        x = 400 + (i % 3) * 150
        y = 200 + (i // 3) * 150
        screen.blit(btn, (x, y))

def draw_level_selection():
    screen.blit(choice_bg, (0, 0))
    levels = levels_alb1 if selected_album == 1 else levels_alb2
    for i, level in enumerate(levels):
        screen.blit(level, (500, 250 + i * 100))

def game_loop():
    global state, selected_album
    clock = pygame.time.Clock()
    while True:
        screen.fill(WHITE)
        
        if state == "menu":
            draw_menu()
        elif state == "management":
            draw_management()
        elif state == "album_selection":
            draw_album_selection()
        elif state == "level_selection":
            draw_level_selection()
        elif state == "coming_soon":
            screen.blit(coming_soon_bg, (0, 0))
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                if state == "management" or state == "album_selection":
                    state = "menu"
                elif state == "level_selection":
                    state = "album_selection"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                
                if state == "menu":
                    if 500 <= x <= 700:
                        if 250 <= y <= 300:
                            state = "album_selection"
                        elif 350 <= y <= 400:
                            state = "management"
                        elif 450 <= y <= 500:
                            pygame.quit()
                            sys.exit()
                elif state == "album_selection":
                    for i in range(9):
                        bx = 400 + (i % 3) * 150
                        by = 200 + (i // 3) * 150
                        if bx <= x <= bx + 100 and by <= y <= by + 100:
                            if i == 0:
                                state = "level_selection"
                                selected_album = 1
                            elif i == 1:
                                state = "level_selection"
                                selected_album = 2
                            else:
                                state = "coming_soon"
        
        clock.tick(FPS)

if __name__ == "__main__":
    game_loop()