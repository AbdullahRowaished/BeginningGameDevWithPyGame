background_image_filename = '../sushiplate.jpg'

import pygame
from pygame.locals import *
from sys import exit

pygame.init()

pygame.event.set_blocked(KEYUP)
pygame.event.set_allowed(QUIT)
text = str(pygame.event.get_blocked(KEYUP))

SCREEN_SIZE = (800, 600)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
background = pygame.image.load(background_image_filename).convert()
screen.fill((0, 0, 0))
screen.blit(background, (0, 0))
font = pygame.font.SysFont("arial", 16)
screen.blit(font.render(text, True, (0, 0, 0)), (0, 400))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    pygame.display.update()