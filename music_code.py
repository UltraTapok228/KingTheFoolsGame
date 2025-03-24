import pygame

pygame.init()

def villian_and_hat_music():
    pygame.mixer.init()
    pygame.mixer.music.load("assets/sounds/Злодей и шапка.mp3")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)