import pygame

pygame.init()

WIDTH = 640
HEIGHT = 480

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('click on image')

# an image when loaded does not know where it should be placed. It only know it's height and width.
# the rect of the image can be accessed using get_rect() but this returns a rect that has the left and top
# set to 0 as these are the internal coordinates of the image.
# in order to detect the mouse within the image correctly we need to supply the left and top with respect to the
# screen itself. We do this by creating a rect from the image and then add the missing left and top values.
# To detect if the mouse is within the image we use the function collidepoint() of the Rect class and pass it the
# mouse coordinates.
# in this demo we simply print the rect info if the mouse is within it.

the_image = pygame.image.load('images/blue_box.png').convert()
rect = the_image.get_rect()     # get the image rect
rect.left = 50                  # adding the x-position of the screen
rect.top = 90                   # adding the y-position of the screen

running = True

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
    if event.type == pygame.MOUSEBUTTONDOWN:
        if rect.collidepoint(event.pos):
                print(rect)

    screen.blit(the_image, (rect.left, rect.top))   # blit the image to the screen
    pygame.display.flip()                           # make it visible


pygame.quit()

