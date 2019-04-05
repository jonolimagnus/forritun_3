import pygame
import random

pygame.init()


class Box:
    def __init__(self, box_id, box_image, x_pos=0, y_pos=0):
        self.id = box_id
        self.image = pygame.image.load(box_image).convert()
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
        self.name = str(box_image.rsplit('/', 1)[1])


screen_width = 680
screen_height = 480
screen = pygame.display.set_mode([screen_width, screen_height])

boxes = list()
messages = list()

# this example we have added a id attribute to the Box class.
# we also have a five element list with latin quotes.
# now when the user clicks on a box the id of that box is
# used to find a latin quote corresponding to that id
messages.append('Aut viam inveniam aut faciam - I will either find a way or make one')
messages.append('Abusus non tollit usum - Wrong use does not preclude proper use')
messages.append('Ad vitam paramus - We are preparing for life')
messages.append('Age quod agis - Do what you do well, pay attention to what you are doing')
messages.append('Audi et alteram partem - Hear the other side too')

boxes.append(Box(0, 'images/pink_box.png', 30, 30))
boxes.append(Box(1, 'images/green_box.png', 160, 30))
boxes.append(Box(22, 'images/orange_box.png', 290, 30))
boxes.append(Box(3, 'images/blue_box.png', 420, 30))
boxes.append(Box(4, 'images/lime_box.png', 550, 30))
running = True

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
    if event.type == pygame.MOUSEBUTTONDOWN:
        for box in boxes:
            if box.rect.collidepoint(event.pos):
                print(messages[box.id % 5]) # the modulus prevents the list from going out of range

    for box in boxes:
        screen.blit(box.image, (box.rect.x, box.rect.y))

    pygame.display.flip()

pygame.quit()
