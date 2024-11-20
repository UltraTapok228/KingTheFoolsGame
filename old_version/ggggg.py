show = True
choice_menu = False

# ... ваш остальной код

while True:
    # ... ваш остальной код 

    if main_menu == False and choice_menu == True:
        # ... ваш остальной код
        pos = pygame.mouse.get_pos()
        # альбом камнем по голове
        if alb1_rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == True:
            # Устанавливаем флаг, что уровень выбран
            level_selected = True
            choice_menu = False

        elif alb2_rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == True:
            # Устанавливаем флаг, что уровень выбран
            level_selected = True
            choice_menu = False

        # ... (аналогично для alb3_rect, alb4_rect, ..., alb9_rect)

    # ... ваш остальной код

    # Отрисовка уровня, если он выбран
    if level_selected == True:
        window.blit(background1, [0, 0])
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

    # ... ваш остальной код

    pygame.display.update()
    clock.tick(60)
