from King_The_Fools_actual import *
import pygame

man_rect.x += change_x
keys = pygame.key.get_pressed()
def right():
    if keys[pygame.K_d]:
        change_x = speed
        man = man_stand
        if man_rect.x >= 1090:
            test -= 10
            
            if man_rect.x > 1090:
                man_rect.x = 1090
def left():        
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