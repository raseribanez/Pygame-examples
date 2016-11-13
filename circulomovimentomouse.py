# Another example of demonstrating circles
# This one was commented in Spanish so I have edited

import pygame
from pygame.locals import*
from sys import exit

pygame.init()

amarelo = (230, 170, 0)
preto = (0, 0, 0)

screen = pygame.display.set_mode((640, 360), 0, 32)
raio = 60
x = 0
y = 0

while True:
    for event in pygame.event.get():
       if event.type == QUIT:
            exit()
        if event.type == MOUSEMOTION:
            x, y = pygame.mouse.get_pos()


    posicao = (x, y)

    screen.fill(preto)
    pygame.draw.circle(screen, amarelo, posicao, raio)

    pygame.display.update()
