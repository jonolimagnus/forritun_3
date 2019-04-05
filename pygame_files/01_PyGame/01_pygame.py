import pygame
'''
    The program imports the PyGame library.
    The only other thing it does is to open a 640X480 window with a black background.
    It however demonstrates a program structure that is important in the development
    of games.
    Good stuff on PyGame basics:  http://www.nerdparadise.com/tech/python/pygame/basics/
'''
pygame.init()   # we always need this

# PyGame helps us define the size of the display(window).
window_size = 640, 480

# and then we create it
window = pygame.display.set_mode(window_size)

running = True  # loop control variable(for the game loop)

# What follows is the game loop.
# Within it the game is "played" by listening to the players input and react to it.
while running:
    # at minimum we need to be able to quit the program.
    # we therefore "listen" for the  "correct" event from the user.
    # in this case we quit the program when the user hits the X in
    # the top right corner of the screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# When the game loop is no longer running the following line causes the program to quit.
pygame.quit()
