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

# current position
x_position = 0
y_position = 0

# current velocity
x_velocity = 5
y_velocity = 2

clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    window.fill(BLUE)
    pygame.draw.rect(window, RED, pygame.Rect(x_position, y_position, 20, 20))

    # position update(based on current velocity)
    x_position += x_velocity
    y_position += y_velocity

    # We need to check all sides of the window to see if the rect has touched them.
    # To have the rect turn around when it touches one of the windows sides we invert
    # it's direction by multiplying the components of the velocity vector by -1.
    # We also need to subtract the size of the rectangle so that we do not get some
    # surprises during the turnaround.
    if y_position > 460 or y_position < 0:  # top - bottom check
        y_velocity *= -1
    if x_position > 620 or x_position < 0:  # left - right check
        x_velocity *= -    1

    pygame.display.update()

    clock.tick(60)
pygame.quit()