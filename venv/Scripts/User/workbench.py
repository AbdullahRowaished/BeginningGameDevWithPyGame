background_image_filename = '..\sushiplate.jpg'

import pygame
from pygame.locals import *
from sys import exit

SCREEN_SIZE = (1280, 720)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)

background = pygame.image.load(background_image_filename).convert()

while True:

    event = pygame.event.wait()
    if event.type == QUIT:
        exit()
    if event.type == VIDEORESIZE:
        SCREEN_SIZE = event.size
        screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
        pygame.display.set_caption("Window resized to "+str(event.size))

    screen_width, screen_height = SCREEN_SIZE
    Rect.inflate(background.convert(),screen_width,screen_height)
    screen.blit(background, (0,0))

    pygame.display.update()