background_image_filename = '../sushiplate.jpg'
sprite_image_filename = '../fugu.png'

import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((1280, 720),0 ,32)

background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename)
Fullscreen = True

# Our clock object
clock = pygame.time.Clock()

# X coordinates of our sprite
x, y = 100.,100.
# Speed in pixels per second
speed_x, speed_y = 384., 216.

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0, 0))
    screen.blit(sprite, (x, y))

    time_passed = clock.tick(30)
    time_passed_seconds = time_passed / 1000.0

    x += speed_x * time_passed_seconds
    y += speed_y * time_passed_seconds

    # If the image goes off the end of the screen, move it back
    if x > 1280 - sprite.get_width():
        speed_x = -speed_x
        x = 1280 - sprite.get_width()
    elif x < 0:
        speed_x = -speed_x
        x = 0
    if y > 720 - sprite.get_height():
        speed_y = -speed_y
        y = 720 - sprite.get_height()
    elif y < 0:
        speed_y = -speed_y
        y = 0

    pygame.display.update()