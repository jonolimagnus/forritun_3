import pygame

pygame.init()

window_size = window_width, window_height = 640, 480
window = pygame.display.set_mode(window_size)

running = True  # loop control variable(for the game loop)

# In order for us to "catch a mouse" we need to set the "trap" in the event loop.
# A mouse has a few features we need to be aware of:
# MOUSEMOTION,
# MOUSEBUTTONUP,
# MOUSEBUTTONDOWN.

# Let's give this a try. to make sure it's working the code simply print something on the
# Python console in respnce to the respective mouse events.
# NOTE: It does not print anything on the game window.
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print ("I'm pressed.")     # We simply print something on the console
        elif event.type == pygame.MOUSEMOTION:
            print ("I'm being dragged.")
        elif event.type == pygame.MOUSEBUTTONUP:
            print ("I'm being released.")

pygame.quit()
