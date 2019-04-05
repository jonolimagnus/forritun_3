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

# current position(must be bigger than the radius of the ball(circle)
x_position = 50
y_position = 50

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

    # let's try drawing a circle instead of a rectangle!
    pygame.draw.circle(window, RED, (x_position, y_position), 10)
    #pygame.draw.rect(window, RED, pygame.Rect(x_position+10, y_position+10, 20, 20))
    # position update(based on current velocity)
    x_position += x_velocity
    y_position += y_velocity

    # As before we need to check all sides of the window to see if the circle has touched them.
    # however we need to be aware of the radius and do our calculations accordingly.
    # otherwise the circle might disappear before it changes direction or it might not touch
    # the boundaries at all.
    if y_position > 470 or y_position < 10:  # top  bottom check
        y_velocity *= -1
    if x_position > 630 or x_position < 10:  # left  right check
        x_velocity *= -1

    pygame.display.update()
    clock.tick(60)
    window.fill(BLUE)

pygame.quit()
