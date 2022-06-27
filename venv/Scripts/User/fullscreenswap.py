background_image_filename='sushiplate.jpg'

import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.setmode((1280, 720), 0, 32)
background = pygame.image.load(background_image_filename).convert()

Fullscreen = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.keyh == K_f:
                Fullscreen = not Fullscreen
                if Fullscreen:
                    screen = pygame.display.set_mode((1280, 720), FULLSCREEN, 32)
                else:
                    screen = pygame.display.set_mode((1280, 720), 0, 32)
            screen.blit(backgroun, (0, 0))
            pygame.display.update()