background_image_filename = '../sushiplate.jpg'

import pygame
from pygame.locals import *
from sys import exit

pygame.init()

CATONKEYBOARD = USEREVENT + 1
cat_event = pygame.event.Event(CATONKEYBOARD, event_msg="Bad cat!")
pygame.event.post(cat_event)

SCREEN_SIZE = (800, 600)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
background = pygame.image.load(background_image_filename).convert()
screen.fill((0, 0, 0))
screen.blit(background, (0, 0))
font = pygame.font.SysFont("arial", 16)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == CATONKEYBOARD:
            text = event.event_msg
            screen.blit(font.render(text, True, (0, 0, 0)), (0, 400))
    pygame.display.update()
