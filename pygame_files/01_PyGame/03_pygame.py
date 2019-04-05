import pygame

pygame.init()

# Create some color constants for later use. The colors are created by RGB mixture.
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 150, 0)
BLUE = (0, 0, 255)

window_size = 640, 480
window = pygame.display.set_mode(window_size)
window.fill(GREEN)  # This command sets the background color.

pygame.display.set_caption('Intro to Game Programming')

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    # since we are now setting the background color instead of using the default
    # black one we need to update the display to make our color(GREEN) visible to the player.

    # Try to comment out this line and run the program if you don't believe you need it :-)
    pygame.display.update()

pygame.quit()
