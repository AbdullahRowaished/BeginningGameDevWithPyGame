background_image_filename = '../sushiplate.jpg'
sprite_image_filename = '../fugu.png'

import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((1920, 1080),FULLSCREEN|HWSURFACE,32)

background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename)
Fullscreen = True

# Our clock object
clock1 = pygame.time.Clock()
clock2 = pygame.time.Clock()

# X coordinates of our sprite
x1 = 0.
x2 = 0.
# Speed in pixels per second
speed = 250.

frame_no = 0

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_f:
                Fullscreen = not Fullscreen
                if Fullscreen:
                    screen = pygame.display.set_mode((1920, 1080), FULLSCREEN, 32)
                else:
                    screen = pygame.display.set_mode((1280, 720), 0, 32)
            screen.blit(background, (0, 0))

    screen.blit(background, (0, 0))
    screen.blit(sprite, (x1, 50))
    screen.blit(sprite, (x2, 250))

    tp1 = clock1.tick(30)
    tp2 = clock2.tick(60)
    tps1 = tp1 / 1000.0
    tps2 = tp2 / 1000.0

    dm1 = tps1 * speed
    dm2 = tps2 * speed
    x1 += dm1
    x2 += dm2

    # If the image goes off the end of the screen, move it back
    if x1 > 640.:
        x1 -= 640
    if x2 > 640.:
        x2 -= 640

    pygame.display.update()
    frame_no += 1
