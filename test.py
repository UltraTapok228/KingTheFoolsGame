import pygame
import sys

# Инициализация Pygame
pygame.init()

# Константы экрана
WIDTH, HEIGHT = 1200, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Игра")
pygame.display.set_icon(pygame.image.load("assets/images/icons/icon.png"))

# Загрузка изображений
menu_bg = pygame.image.load("assets/images/backgrounds/менюшки/menu.png")
management_bg = pygame.image.load("assets/images/backgrounds/менюшки/management_bg.png")
choice2_bg = pygame.image.load("assets/images/backgrounds/менюшки/choice2.png")
choice_bg = pygame.image.load("assets/images/backgrounds/менюшки/choice.png")
coming_soon = pygame.image.load("assets/images/backgrounds/менюшки/comming soon.png")

dirt = pygame.image.load("assets/images/компоненты локации/dirt.png")
grass = pygame.image.load("assets/images/компоненты локации/grass.png")
stone = pygame.image.load("assets/images/компоненты локации/stone.png")
stone_bricks = pygame.image.load("assets/images/компоненты локации/stone_bricks.png")
man = pygame.image.load("assets/images/персонажи/man.png")

# Кнопки главного меню
class Button:
    def __init__(self, x, y, image):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect(topleft=(x, y))
    
    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)
    
    def is_clicked(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)

# Функция отрисовки карты
textures = {"#": stone, ".": dirt, "G": grass, "B": stone_bricks}

def draw_map(map_data):
    for y, row in enumerate(map_data):
        for x, cell in enumerate(row):
            if cell in textures:
                screen.blit(textures[cell], (x * 64, y * 64))
    screen.blit(man, (100, 100))

# Определение уровней
maps = {
    "Злодей и Шапка": [
        "########",
        "#......#",
        "#.GGGG.#",
        "#.BBBB.#",
        "#......#",
        "########"
    ],
    "Внезапная голова": [
        "########",
        "#GGGGGG#",
        "#BBBBBB#",
        "#......#",
        "#......#",
        "########"
    ]
}

def game_loop(map_name):
    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_map(maps[map_name])
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return

# Главное меню
running = True
while running:
    screen.blit(menu_bg, (0, 0))
    play_btn = Button(500, 300, "play_btn.png")
    management_btn = Button(500, 400, "management_btn.png")
    exit_btn = Button(500, 500, "exit_btn.png")
    
    play_btn.draw(screen)
    management_btn.draw(screen)
    exit_btn.draw(screen)
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        if play_btn.is_clicked(event):
            # Логика выбора альбомов
            screen.blit(choice2_bg, (0, 0))
            pygame.display.flip()
            pygame.time.wait(500)  # Имитация задержки перед выбором альбома
            # Заглушка для выбора альбомов
            screen.blit(coming_soon, (0, 0))
            pygame.display.flip()
            pygame.time.wait(1000)
        if management_btn.is_clicked(event):
            screen.blit(management_bg, (0, 0))
            pygame.display.flip()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        break
        if exit_btn.is_clicked(event):
            running = False

pygame.quit()
