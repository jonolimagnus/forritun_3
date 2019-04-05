import pygame

pygame.init()


# we now create a simple class that represents a single Box
# this class contains the info we need to blit the box to
# the screen. It also extracts the image name from the given
# path
class Box:
    def __init__(self, box_image, x_pos=0, y_pos=0):
        self.image = pygame.image.load(box_image).convert()
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
        self.name = str(box_image.rsplit('/', 1)[1])


screen_width = 550
screen_height = 480
screen = pygame.display.set_mode([screen_width, screen_height])

boxes = list()

boxes.append(Box('images/pink_box.png', 30, 30))
boxes.append(Box('images/green_box.png', 160, 30))
boxes.append(Box('images/orange_box.png', 290, 30))
boxes.append(Box('images/blue_box.png', 420, 30))

running = True

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
    if event.type == pygame.MOUSEBUTTONDOWN:
        for box in boxes:
            if box.rect.collidepoint(event.pos):
                print(box.name)

    for box in boxes:
        screen.blit(box.image, (box.rect.x, box.rect.y))

    pygame.display.flip()

pygame.quit()
