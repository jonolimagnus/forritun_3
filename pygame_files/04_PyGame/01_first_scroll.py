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

    # The thing here is to have the second version of the same image follow
    # the first one over the screen. The graphics need to be designed in such
    # a way that the starting y-pixels are (almost) identical to the end y-pixels.
    # otherwise the transition will not be smooth.
    # when the first image has "left" the screen it's starting position is reset.
    screen.blit(back_1, (x, 0))
    # the second image starts totally off the screen and since ew are going to the right
    # the image is put on the left side of the first one.
    screen.blit(back_2, (x - SCREEN_WIDTH, 0))

    # for each round of the loop the images are moved one pixel to the right creating the
    # illusion of a smooth movement of the mountain range in the background.
    # when the screen width is reached the x coordinate is set to the starting value of 0.
    x += 1
    if x == SCREEN_WIDTH:
        x = 0

    clock.tick(60)
    pygame.display.flip()
