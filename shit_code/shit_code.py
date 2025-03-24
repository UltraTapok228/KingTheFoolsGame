import pygame

pygame.init()

WIDTH, HEIGHT = 1200, 700
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('King The Fools')
pygame.display.set_icon(pygame.image.load('assets/images/icons/icon.png'))

FPS = 60
clock = pygame.time.Clock()

# Загрузка изображений
menu = pygame.image.load('assets/images/backgrounds/менюшки/menu.png')
menu = pygame.transform.scale(menu, [1200, 700])
man_bg = pygame.image.load('assets/images/backgrounds/менюшки/management_bg.png')
choice2 = pygame.image.load('assets/images/backgrounds/менюшки/choice2.png')
choice = pygame.image.load('assets/images/backgrounds/менюшки/choice.png')
comming_soon = pygame.image.load('assets/images/backgrounds/менюшки/comming soon.png')

# Кнопки главного меню
play_btn = pygame.image.load('assets/images/кнопки/play_btn.png')
play_btn = pygame.transform.scale(play_btn, [278, 80])
management_btn = pygame.image.load('assets/images/кнопки/management_btn.png')
management_btn = pygame.transform.scale(management_btn, [278, 80])
exit_btn = pygame.image.load('assets/images/кнопки/exit_btn.png')
exit_btn = pygame.transform.scale(exit_btn, [278, 80])

# Кнопки выбора альбомов
album_buttons = [pygame.image.load(f'assets/images/обложки альбомов/alb{i}.png') for i in range(1, 10)]
album_rects = [btn.get_rect(topleft=(300 + (i % 3) * 200, 200 + (i // 3) * 150)) for i, btn in enumerate(album_buttons)]

# Кнопки уровней альбома Камнем по Голове
level_buttons1 = [
    pygame.image.load('assets/images/Камнем по голове/Злодей и Шапка.png'),
    pygame.image.load('assets/images/Камнем по голове/Внезапная голова.png')
]

# Кнопки уровней Акустического альбома
level_buttons3 = [
    pygame.image.load('assets/images/Акустический альбом/кукла колдуна.png')
]

# Переменные состояния
state = 'menu'  # menu, management, album_select, level_select, game
selected_album = None
selected_level = None

running = True
while running:
    window.fill((0, 0, 0))
    pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if state in ['management', 'album_select', 'level_select', 'game']:
                    state = 'album_select'
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if state == 'menu':
                if play_btn.get_rect(center=(WIDTH//2, HEIGHT//2 - 50)).collidepoint(pos):
                    state = 'album_select'
                elif management_btn.get_rect(center=(WIDTH//2, HEIGHT//2 + 50)).collidepoint(pos):
                    state = 'management'
                elif exit_btn.get_rect(center=(WIDTH//2, HEIGHT//2 + 150)).collidepoint(pos):
                    running = False
            elif state == 'album_select':
                for i, rect in enumerate(album_rects):
                    if rect.collidepoint(pos):
                        if i == 0:
                            state = 'level_select1'
                        elif i == 2:
                            state = 'level_select3'
                        else:
                            state = 'coming_soon'
    
    if state == 'menu':
        window.blit(menu, (0, 0))
        window.blit(play_btn, play_btn.get_rect(center=(WIDTH//2, HEIGHT//2 - 50)))
        window.blit(management_btn, management_btn.get_rect(center=(WIDTH//2, HEIGHT//2 + 50)))
        window.blit(exit_btn, exit_btn.get_rect(center=(WIDTH//2, HEIGHT//2 + 150)))
    elif state == 'management':
        window.blit(man_bg, (0, 0))
    elif state == 'album_select':
        window.blit(choice2, (0, 0))
        for i, btn in enumerate(album_buttons):
            window.blit(btn, album_rects[i])
    elif state == 'level_select1':
        window.blit(choice, (0, 0))
        for i, btn in enumerate(level_buttons1):
            window.blit(btn, (300 + i * 200, 300))
    elif state == 'level_select3':
        window.blit(choice, (0, 0))
        for i, btn in enumerate(level_buttons3):
            window.blit(btn, (300, 300))
    elif state == 'coming_soon':
        window.blit(comming_soon, (0, 0))
    
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()