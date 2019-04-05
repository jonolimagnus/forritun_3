import pygame
'''
 The program prints out the mouse coordinates as it moves.
 The printed coordinates are printed on the "game screen" itself
 not on the Python console.
 The program makes use of the PyGame font.
 More info on that: http://www.pygame.org/docs/ref/font.html
'''
pygame.init()

GREY_COLOR = (70, 80, 90)
YELLOW_COLOR = (255, 255, 0)
DISPLAY_SIZE = (640, 400)

running = True
screen = pygame.display.set_mode(DISPLAY_SIZE)
screen.fill(GREY_COLOR)

# Since printing the mouse coordinates on the python console
# is a huge turnoff we print it on the screen itself. To do
# that the first thing is to set a font to work with.
my_font = pygame.font.SysFont("Comic Sans MS", 30)

while running:
    # As usual we check the events
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.MOUSEMOTION:
        # clear the screen between "runs"
        screen.fill((70, 80, 90))
        # Now we use the font we have already defined(my_font)
        label = my_font.render(str(event.pos), 1, YELLOW_COLOR)
         # put the info on the screen
        screen.blit(label, (230, 100))

    # draw the screen
    pygame.display.flip()
