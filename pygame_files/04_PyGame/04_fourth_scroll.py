import pygame
import sys
from pygame.locals import *

# This demo is based on and inspired by Bytes for Lunch.
# Website: https://bytesforlunch.wordpress.com/2011/10/04/videogame-programming-a-simple-scrollable-background-with-python-and-pygame/
# Accessed: 15.10.2016

# this version of the scrolling program has consolidated the positional
# calculations into one function.  This secures more clarity of code
# which is always a good thing.
def calculate_pos(direction, x, width):
    if (x * direction) < 0:
        return(width * direction) + x
    elif x == width or x == 0:
        return(-width) * direction
    else:
        return (width - (x* direction))* -direction

		
pygame.init()
clock = pygame.time.Clock()

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 200
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

back_1 = pygame.image.load('image_for_scroll.jpg').convert()
back_2 = pygame.image.load('image_for_scroll.jpg').convert()

x1 = 0
n = 1

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                n *= -1

    # here the new function calculate_pos() is called and it returns the
    #position of the second image.
    x_pos = calculate_pos(n, x1, SCREEN_WIDTH)

    screen.blit(back_1, (x1, 0))
    screen.blit(back_2, (x_pos, 0))

    x1 += n
    if x1 == SCREEN_WIDTH or x1 == -SCREEN_WIDTH:
        x1 = 0

    clock.tick(40)
    pygame.display.flip()