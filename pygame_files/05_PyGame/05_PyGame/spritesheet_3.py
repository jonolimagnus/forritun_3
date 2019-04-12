import sys
import pygame

# Since the double loop can handle both single and two- dimensional
# sprite sheets we turn it into a simple sheet loading function.
# This function is by no means complete(e.x. no error handling,no starting point etc.)
# but loading "uniform" sprite sheets should work relatively well.
# the parameters to the function are the frame width, frame height and path to the file.
# The function returns an list of the images(frames) contained within the sprite sheet.

def sprite_loader(sp_width, sp_height, sheet_file):
    sprite_frames = []
    image = pygame.image.load(sheet_file).convert_alpha()
    width, height = image.get_size()

    for row in range(int(height / sp_height)):
        for col in range(int(width / sp_width)):
            sprite_frames.append(image.subsurface((col * sp_width, row * sp_height, sp_width, sp_height)))

    return sprite_frames


pygame.init()

screen = pygame.display.set_mode((640, 400))
pygame.display.set_caption('Private dancer')
# using the sprite_loader function
frames = sprite_loader(80, 80, 'dancer_spritesheet.png')
number_of_sprites = len(frames)
timer = pygame.time.Clock()

current_frame = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False
            sys.exit()

    screen.fill((200, 200, 200))
    screen.blit(frames[current_frame], (100, 100))

    current_frame += 1
    if current_frame == number_of_sprites:
        current_frame = 0

    pygame.display.update()
    timer.tick(10)
