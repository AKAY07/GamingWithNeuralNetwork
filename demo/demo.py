"""
author:-adarsh kandwal
date:-
"""
import pygame
import random

pygame.init()

SCREEN = pygame.display.set_mode((800, 600))
ICON = pygame.image.load('C:/Users/Dell/Desktop/pygame/demo/ufo.png')
pygame.display.set_icon(ICON)
pygame.display.set_caption("SPACE LEGACY")

#background
BACKGROUND = pygame.image.load('C:/Users/Dell/Desktop/pygame/demo/back.j')

#our space ship
PLAYERIMG = pygame.image.load('C:/Users/Dell/Desktop/pygame/demo/space-invaders.png')
PLAYERX = 370
PLAYERY = 480
PLAYERX_CHANGE = 0

#enemy's ship 
ENEMYIMG = pygame.image.load('C:/Users/Dell/Desktop/pygame/demo/monster.png')
ENEMYX = random.randint(0, 800)
ENEMYY = random.randint(50, 150)
ENEMYX_CHANGE = 0.3
ENEMYY_CHANGE = 40



def player(x,y):
    SCREEN.blit(PLAYERIMG, (x,y))


def enemy(x,y):
    SCREEN.blit(ENEMYIMG, (x,y))

RUNNING = True

while RUNNING:
    
    SCREEN.fill((0, 0, 0))
    SCREEN.blit(BACKGROUND,(0,0))
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            RUNNING = False
        #if key is pressed arrow
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                PLAYERX_CHANGE = -0.3
            if event.key == pygame.K_RIGHT:
                PLAYERX_CHANGE = 0.3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                PLAYERX_CHANGE = 0
    
    #enemy movement
    ENEMYX += ENEMYX_CHANGE
    
    if ENEMYX <= 0:
        ENEMYX_CHANGE = 0.3
        ENEMYY += ENEMYY_CHANGE
    if ENEMYX >= 736:
        ENEMYX_CHANGE = -0.3
        ENEMYY += ENEMYY_CHANGE
    #player movement
    PLAYERX += PLAYERX_CHANGE
    if PLAYERX <= 0:
        PLAYERX = 0
    if PLAYERX >= 736:
        PLAYERX = 736 

    player(PLAYERX, PLAYERY)
    enemy(ENEMYX, ENEMYY)
    pygame.display.update()