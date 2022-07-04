import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)

font = pygame.font.SysFont("arial", 32)
font_height = font.get_linesize()
pressed_keys = pygame.key.get_pressed()
for key_constant, pressed in enumerate(pressed_keys):
    print(pygame.key.name(key_constant),key_constant,pressed)

while True:

    pressed_key_text = []
    pressed_keys = pygame.key.get_pressed()
    screen.fill((255, 255, 255))
    y = font_height

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        #if event.type == KEYDOWN:
         #   screen.blit(font.render(pygame.key.name(event.key), True, (0,0,0)), (8,y))
          #  y += font_height
    for key_constant, pressed in enumerate(pressed_keys):
        if pressed:
            key_name = pygame.key.name(key_constant)
            text_surface = font.render(key_name+" pressed", True, (0,0,0))
            screen.blit(text_surface, (8,y))
            y += font_height

    pygame.display.update()