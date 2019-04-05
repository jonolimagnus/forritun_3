import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

window_size = 640, 480
window = pygame.display.set_mode(window_size)
window.fill(BLUE)

pygame.display.set_caption('Intro to Game Programming')

x_position = 0
# since we're going to move the red rectangle in two dimensions we a variable for the y coordinate
y_position = 0

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    # Each time the game loop runs the value in both position variables is increased.
    # This now  "moves" the red rect to the right and down at the same time.
    x_position += 0.1
    y_position += 0.1

    # now instead of previous hard coding use y_position for the y coordinate
    pygame.draw.rect(window, RED, pygame.Rect(x_position, y_position, 60, 60))
    pygame.display.update()

    window.fill(BLUE)

pygame.quit()