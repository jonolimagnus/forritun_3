import pygame

pygame.init()

WIDTH = 640
HEIGHT = 480

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('click on image')

pink_square = pygame.image.load("images/pink_box.png").convert()
red_square = pygame.image.load("images/orange_box.png").convert()

a = screen.blit(red_square, (30, 30))       # paint to screen
b = screen.blit(pink_square, (160, 30))     # paint to screen

# having clicked on a single image we now try it with two images
# in this demo we print the respective info depending on which box is clicked.

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if a.collidepoint(event.pos):
                print('clicked on orange square')
            if b.collidepoint(event.pos):
                print('clicked on pink square')

    pygame.display.flip()  # paint screen one time

pygame.quit()
