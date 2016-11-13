# Ben Woodfield - Play video using Pygame
# To make this work you have to do 2 things
#
#1: Make sure your mpg or compatible video is saved in the SAME
# directory as this program
#
#2: Either rename your video 'video.mpg' or rename the coded name below

import pygame
from pygame.locals import *
from sys import exit

pygame.init()

video = pygame.movie.Movie('video.mpg') # Rename to your video name

screen = pygame.display.set_mode(video.get_size(), 0, 32)

video.set_display(pygame.display.get_surface())

video.play()

while video.get_busy():
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
