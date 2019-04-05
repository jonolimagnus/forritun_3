import pygame
import sys
from pygame.locals import *

# This demo is based on and inspired by Bytes for Lunch.
# Website: https://bytesforlunch.wordpress.com/2011/10/04/videogame-programming-a-simple-scrollable-background-with-python-and-pygame/
# Accessed: 15.10.2016

pygame.init()
clock = pygame.time.Clock()

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 200
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

# Get the background and put it in two separate variables!!!
back_1 = pygame.image.load('image_for_scroll.jpg').convert()
back_2 = pygame.image.load('image_for_scroll.jpg').convert()

# this means the left side of the screen. We're not using the y part
# since the background is only moving horizontally.
# It should be noted that the screen width matches the width of the image.
x = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # we will be going in the other direction from the previous example
    # but we do not change this line of code since it puts the first image
    # on the screen(in the correct starting place)
    screen.blit(back_1, (x, 0))
    # here is were ew change the code slightly(we now add the screen width to x)
    screen.blit(back_2, (x + SCREEN_WIDTH, 0))

    # the value oof x is decreased on each round of the loop and when it has
    # reached the minus screen_width value x is rests to 0
    x -= 1
    if x == -SCREEN_WIDTH:
        x = 0

    clock.tick(60)
    pygame.display.flip()
