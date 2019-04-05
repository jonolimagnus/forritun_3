import pygame

pygame.init()

DISPLAY_WIDTH = 600
DISPLAY_HEIGHT = 480
WHITE = (255, 255, 255)

# Here we load the image and put it in a variable called the_car
the_car = pygame.image.load('images/bluecar.png')

# to be able to draw the image on the screen we need to supply the top left coorinates.
# in this case it's in the upper left corner of the screen.
x = 0
y = 0

screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Image')

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    # now we blit the car onto the background and then update the display to make it visible.
    screen.blit(the_car, (x, y))
    pygame.display.update()

pygame.quit()
