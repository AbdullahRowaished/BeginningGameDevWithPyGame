import pygame
from math import fabs
from pygame.locals import *
from sys import exit

pygame.init()

SCREEN_SIZE = (640, 480)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

font = pygame.font.SysFont("arial", 16)
font_height = font.get_linesize()
event_text = []

joysticks = []
for joystick_no in range(pygame.joystick.get_count()):
    stick = pygame.joystick.Joystick(joystick_no)
    stick.init()
    joysticks.append(stick)

while True:

    event = pygame.event.wait()
    if event.type == QUIT:
        exit()
    if event.type in (JOYAXISMOTION,
                      JOYBALLMOTION,
                      JOYHATMOTION,
                      JOYBUTTONUP,
                      JOYBUTTONDOWN):
        event_text.append(str(event))

    event_text = event_text[-int(SCREEN_SIZE[1]/font_height):]

    screen.fill((255,255,255))

    y = SCREEN_SIZE[1] - font_height
    for text in reversed(event_text):
        if (fabs(stick.get_axis(0).real) >= 0.25
                or fabs(stick.get_axis(1).real) >= 0.25
                or fabs(stick.get_axis(2).real) >= 0.25
                or fabs(stick.get_axis(3).real) >= 0.25):
            screen.blit(font.render(text, True, (0,0,0)), (0,y))
        y-=font_height

    pygame.display.update()