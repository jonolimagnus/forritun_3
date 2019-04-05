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

back_1 = pygame.image.load('image_for_scroll.jpg').convert()
back_2 = pygame.image.load('image_for_scroll.jpg').convert()

x = 0
# what we are trying to do here is to implement a solution so that
# when the user hits tha space bar the direction is changes.
# the mountain range is still "auto-scrolling" over the screen.
# to do this we need a direction indicator which we store in the variable n
# there are two directions so we aim to use 1 and -1.  And we start with 1
n = 1

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:    # if spacebar is poresse we simply invert the direction.
                n *= -1

    # this section is a bit different from the previous example.
    # now we need to be aware of the face that when we "turn around" the images
    # can be anywhere within the given boundaries. This means that one does not simply
    # put them in their original position(that would create a "glitch"). Furthermor
    # the changes made are dependent upon the direction we are heading when we turn(hit the spacebar)
    if n == 1:
        # images are going from left to right
        if x < 0:
            x_pos = SCREEN_WIDTH + x
        elif x == SCREEN_WIDTH:
            x_pos = -SCREEN_WIDTH
        else:
            x_pos = -SCREEN_WIDTH + x
    else:
        # images are going from right to left
        if x > 0:
            x_pos = -SCREEN_WIDTH + x
        elif x == 0:
            x_pos = SCREEN_WIDTH
        else:
            x_pos = SCREEN_WIDTH + x

    screen.blit(back_1, (x, 0))
    # x_pos holds the current position of the second image in relation to the first one.
    screen.blit(back_2, (x_pos, 0))

    x += n
    # since we can now scroll in two directions we need to expand the if statement
    # to reset the value of x.
    if x == SCREEN_WIDTH or x == -SCREEN_WIDTH:
        x = 0

    clock.tick(40)
    pygame.display.flip()
