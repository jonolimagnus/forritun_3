import pygame
# This demo is based on code from Lorenzo E. Danielsson
# Web page https://lorenzod8n.wordpress.com/2007/05/30/pygame-tutorial-3-mouse-events/
# Accessed: 10-02-2015

# lets declare the mouse buttons constants.
# The numbers for these are PyGame numbers.
# We turn these into readable constants names because we can :-)
LEFT_BUTTON = 1
MIDDLE_BUTTON = 2
RIGHT_BUTTON = 3
WHEEL_UP = 4
WHEEL_DOWN = 5

# We are not forgetting the background
BACKGROUND = (255, 255, 255)

running = True

window = pygame.display.set_mode((640, 480))
window.fill(BACKGROUND)

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT_BUTTON:
        print( "You pressed the left mouse button at (%d, %d)" % event.pos)
    elif event.type == pygame.MOUSEBUTTONUP and event.button == LEFT_BUTTON:
        print( "You released the left mouse button at (%d, %d)" % event.pos)
    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT_BUTTON:
        print("You pressed the right mouse button at (%d, %d)" % event.pos)
    elif event.type == pygame.MOUSEBUTTONUP and event.button == RIGHT_BUTTON:
        print("You released the right mouse button at (%d, %d)" % event.pos)

    window.fill(BACKGROUND)
    pygame.display.flip()
