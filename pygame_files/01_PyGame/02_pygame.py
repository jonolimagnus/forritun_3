import pygame
'''
    Does pretty much the same as the first program.
    It has however some added features and a lot less comments.
'''
pygame.init()

window_size = 640, 480
window = pygame.display.set_mode(window_size)

# when this line runs the window gets a caption
pygame.display.set_caption('Intro to Game Programming')

running = True

# In the game loop we now also listen if the user hits the Esc button.
# Should that be the case the program quits.
# If you need more info on events supported in PyGame be sure to read this:
# http://www.pygame.org/docs/ref/event.html
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # we need to check if a key has been pressed and if that key was the Esc key
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

pygame.quit()
