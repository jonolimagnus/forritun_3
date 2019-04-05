import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

window_size = window_width, window_height = 640, 480
window = pygame.display.set_mode(window_size)
window.fill(WHITE)

pygame.display.set_caption('Intro to Game Programming')

# lets put the x-position of the rectangle in a variable.
x_position = 0

# Sometimes programs run to fast for a graphical component to have any real meaning.
# In order to 'fix' this one method is to "slow down the clock".
# PyGame includes a Clock class in its time library and within that class is the method tick().
# By manipulating the frames that are displayed per second we can slow things down / speed them up
clock = pygame.time.Clock()
clock_ticks = 20

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    # Each time the game loop runs the value in the x_position variable is increased.
    # This "moves" the red rect to the right.
    x_position += 2

    pygame.draw.rect(window, RED, pygame.Rect(x_position, 30, 60, 60))
    pygame.display.update()

    # By constantly increasing the value of x_position variable and refilling the screen
    # we have created the illusion of a continuous movement!!
    window.fill(WHITE)

    # calling the clock.tick() method. The value we set in line 25 will be used but
    # try to vary the speed by changing the value of the clock_ticks variable.
    clock.tick(clock_ticks)

pygame.quit()