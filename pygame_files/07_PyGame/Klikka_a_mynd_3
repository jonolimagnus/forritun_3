import pygame

pygame.init()

width = 640
height = 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('click on an image')

image_list = list()

# in this example we have 4 images that we want to click on. As it might become difficult
# to manage each image individually we make use of lists.
# we also make use of the fact that the blit() function returns rect and simply blit
# each image to the screen as we append it to the image-list.
# in the game loop we iterate through the list and check for each image if the mouse
# is within it.  If it is we print the rect-info
image_list.append(screen.blit(pygame.image.load("images/pink_box.png").convert(), (30, 30)))
image_list.append(screen.blit(pygame.image.load("images/orange_box.png").convert(), (160, 30)))
image_list.append(screen.blit(pygame.image.load("images/green_box.png").convert(), (290, 30)))
image_list.append(screen.blit(pygame.image.load("images/blue_box.png").convert(), (420, 30)))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for img in image_list:
                if img.collidepoint(event.pos):
                    print(img)

    pygame.display.flip()  # paint screen one time

pygame.quit()
