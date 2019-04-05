import pygame
# This demo is based on code from Lorenzo E. Danielsson
# Web page https://lorenzod8n.wordpress.com/2007/05/30/pygame-tutorial-3-mouse-events/
# Accessed: 10-02-2015
pygame.init()

# define some colors
BACKGROUND = (0, 80, 0)
LINE_COLOR = (255, 0, 0)

window_size = window_width, window_height = 640, 480
window = pygame.display.set_mode(window_size)

# lets set the background color so that it does not default to black or something worse :-)
window.fill(BACKGROUND)
# and then set the initial values for the x and y coordinates.
x_coord = y_coord = 0

running = True  # same old same old

# In this example we are working with the mouse motion for our demonstrations.
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            # We put the mouse coordinates into the two variables
            x_coord, y_coord = event.pos

            # clear the background by drawing it over whatever it contains
            window.fill(BACKGROUND)

            # At last as the ultimate "show off" we draw crossing lines.
            # One is vertical and the other is horizontal.  They intersect at the mouse position
            pygame.draw.line(window, LINE_COLOR, (x_coord, 0), (x_coord, 479))
            pygame.draw.line(window, LINE_COLOR, (0, y_coord), (639, y_coord))

    pygame.display.flip()

pygame.quit()

