import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

window_size = 640, 480
window = pygame.display.set_mode(window_size)
window.fill(WHITE)

pygame.display.set_caption('Intro to Game Programming')

x_position = 0

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    # Each time the game loop runs, the value in the x_position variable is increased.
    # This "moves" the red rect to the right.
    # The method shown here is simply to take "smaller steps" when updating the x_position variable.
    # Note:  This does NOT slow down the whole program only the "movement" of the red rectangle.
    x_position += 0.1

    pygame.draw.rect(window, RED, pygame.Rect(x_position, 30, 60, 60))
    pygame.display.update()

    window.fill(WHITE)

pygame.quit()