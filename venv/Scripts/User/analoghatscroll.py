picture_file = '../fugu.png'

import pygame
from math import fabs
from pygame.locals import *
from sys import exit
from vector2 import Vector2

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)

picture = pygame.image.load(picture_file).convert()
picture_pos = Vector2(0, 0)
scroll_speed = 1000.

clock = pygame.time.Clock()

joystick = None

if pygame.joystick.get_count() > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

if joystick is None:
    print("Sorry, you need a joystick for this!")
    exit()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    scroll_direction = Vector2(0, 0)
    if joystick.get_numhats() > 0:
        scroll_direction = Vector2(*joystick.get_hat(0))
        scroll_direction.normalize()

    analog_scroll = Vector2(0, 0)
    left_x = joystick.get_axis(0)
    left_y = joystick.get_axis(1)
    right_x = joystick.get_axis(2)
    right_y = joystick.get_axis(3)
    analog_scroll = Vector2(left_x, -left_y)
    analog_scroll_2 = Vector2(right_x, -right_y)

    screen.fill((255,255,255))
    screen.blit(picture, (picture_pos.x, -picture_pos.y))

    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.

    picture_pos +=  scroll_direction * scroll_speed * time_passed_seconds
    if fabs(analog_scroll.get_magnitude()) > 0.3:
        picture_pos += analog_scroll * scroll_speed * time_passed_seconds
    if fabs(analog_scroll_2.get_magnitude()) > 0.3:
        picture_pos += analog_scroll_2 * scroll_speed * time_passed_seconds

    pygame.display.update()