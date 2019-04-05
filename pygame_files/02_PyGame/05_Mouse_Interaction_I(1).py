import pygame

# constants
LEFT_BUTTON = 1
WINDOW_SIZE = (640, 480)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

running = True

window = pygame.display.set_mode(WINDOW_SIZE)
window.fill(BLACK)

# This time around we are going to check if the mouse is inside a rectangular
# that has been placed on the game window.  To do that we make use og a nice little
# function of the Rect class, called collidepoint().
# To make life easier for us we first create a Rect object and call it the_box.
# Notice that this box is placed not far from the origin(the upper left corner)
# To be exact; 30px right and 30px down. The box is 100px X 100px in size.
the_box = pygame.Rect(30, 30, 100, 100)

# now we need to paint the box on the screen and give it some (initial) color
# in the process(here: red)
pygame.draw.rect(window, RED, the_box)

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT_BUTTON:
        # When the user clicks on the left mouse button the the mouse coordinates
        # are sent to the collidepoint() function of the box(the_box) and the if
        # statement handles the result(True or False the mouse in either within the box or not)
        # if the mouse is within, the_box gets a paint job and turns blue.
        # At this moment everyone gets extremely happy :-)
        if the_box.collidepoint(event.pos):
            pygame.draw.rect(window, BLUE, the_box)

    pygame.display.flip()
