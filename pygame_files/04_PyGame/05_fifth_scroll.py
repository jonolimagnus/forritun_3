import pygame
import sys
from pygame.locals import *

# This demo is based on and inspired by Bytes for Lunch.
# Website: https://bytesforlunch.wordpress.com/2011/10/04/videogame-programming-a-simple-scrollable-background-with-python-and-pygame/
# Accessed: 15.10.2016

def calculate_pos(direction, x, width):
    if (x * direction) < 0:
        return(width * direction) + x
    elif x == width or x == 0:
        return(-width) * direction
    else:
        return (width - (x * direction)) * -direction

pygame.init()
clock = pygame.time.Clock()

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 200
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

back_1 = pygame.image.load('image_for_scroll.jpg').convert()
back_2 = pygame.image.load('image_for_scroll.jpg').convert()

x1 = 0
n = 0
x_pos = 0

# this version differs notably from the previous ones because
# the scrolling is controlled by user input and is not automated.
# The behaviour is that the background scrolls when the user presses
# the right or left arrow keys but stops if the user releases the keys.
# The code change is only in the input-handling part. Everything else
# is as it was in the last example.
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                n = 1
            if event.key == K_LEFT:
                n = -1
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                n = 0
            if event.key == K_LEFT:
                n = 0

    screen.blit(back_1, (x1, 0))
    screen.blit(back_2, (x_pos, 0))

    if n != 0:
        x_pos = calculate_pos(n, x1, SCREEN_WIDTH)

    x1 += n
    if x1 == SCREEN_WIDTH or x1 == -SCREEN_WIDTH:
        x1 = 0

    clock.tick(40)
    pygame.display.flip()