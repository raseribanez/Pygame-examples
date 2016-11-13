#!/usr/bin/env python

import pygame
from pygame.locals import*
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800, 600),0,32)
color = (230,170,0)
radius = (60)

x = 0
y = 0

while True:
    for event in pygame.event.get():       
        if event.type == QUIT:
            pygame.quit()
            exit()

    x = x + 1
    y = y + 1

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen,color,(x, y),radius)

    pygame.display.flip()



