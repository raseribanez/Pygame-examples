# Ben Woodfield
# Small program to detect keyboard activity
# press keys to see a message - not all keys have been added yet


import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 600), 0, 32)
branco = (255, 255, 255)
preto = (0, 0, 0)

message = ""

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == KEYDOWN:
            # Here we can add the keys to display when pressed  
            # if 113 == 113
            if event.key == K_q:
                message = "q was pressed"
            # elif 119 == 119
            elif event.key == K_w:
                message = "w was pressed"
            elif event.key == K_a:
                message = "a was pressed"
            elif event.key == K_b:
                message = "b was pressed"
            elif event.key == K_c:
                message = "c was pressed"

    screen.fill(preto)
    screen.blit(pygame.font.SysFont("arial", 72).render(message, True, branco), (80, 200))
    pygame.display.update()
