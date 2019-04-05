import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 150, 0)
BLUE = (0, 0, 255)

window_size = 640, 480
window = pygame.display.set_mode(window_size)
window.fill(BLUE)

pygame.display.set_caption('Intro to Game Programming')

# From the previous example(07) we have x and y positions
x_position = 0
y_position = 0

# Now we will introduce a velocity vector representing movement in the two directions; x and y
# You will not be surprised by the fact these are the only dimensions we can use to move around in
# a 2D system and in such a system, movement can always be broken down into horizontal and vertical
# components, in this case x and y components of the velocity vector.
# We will start with this velocity: V = (3,1)
# this means that for every three units of length the x travels(to the right), y travels one(down).
# this will create a gentle slope down the screen to the right.It's worth noting that the unit of
# length here is a pixel.
x_velocity = 3
y_velocity = 1

# Lest control the frames per second in this program.
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill(BLUE)
    pygame.draw.rect(window, RED, pygame.Rect(x_position, y_position, 60, 60))

    # Now the position is calculated with respect to the velocity that is kept in the two
    # velocity variables(x_velocity and y_velocity).
    # What this means in terms of speed is that it is controlled by the values in these
    # velocity variables => the higher the value of each variable, the faster the speed
    # in that respective direction.
    x_position += x_velocity
    y_position += y_velocity

    pygame.display.update()
    clock.tick(60)
    window.fill(BLUE)

pygame.quit()