import pygame
'''
    We define a Sprite Sheet to be an image containing more than one image.
    The usual method of animating is to load images into a list or added to a sprite collection.
    From there it is run through some sort of a loop structure to create the desired animation.
    With a sprite sheet there is an extra work needed of getting the images(sometimes
    called frames) from the sheet and into an designated array.  To do this we need
    to know a few things about the size if the individual image(frame) that we want to get.
    Having that information we can get going.
'''
pygame.init()

# the dimensions of each frame in the sprite sheet are know beforehand.
FRAME_WIDTH = 32    # the width of the frame
FRAME_HEIGHT = 64   # the height of the frame

screen = pygame.display.set_mode((640, 400), 0, 32)

sheet_frames = list()   # sheet_frames is the list that will hold the frames(images)
timer = pygame.time.Clock()
image = pygame.image.load('bomb_spritesheet.png')
# We need the size of the sprite sheet to be able to move around in it
# and "pick" out the appropriate frames(images)
sheet_width, sheet_height = image.get_size()

# We know the sprite sheet only has one row of frames(images) so we use a
# single loop to traverse the sheet rows and retrieve the correct portions
# that are then put into the sheet_frames array. To do this we use the
# subsurface() function.

for col in range(int(sheet_width / FRAME_WIDTH)):
    sheet_frames.append(image.subsurface((col * FRAME_WIDTH, 0, FRAME_WIDTH, FRAME_HEIGHT)))

# Get the size of the array(number of elements/frames)
number_of_sprites = len(sheet_frames)
current_frame = 0

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((120, 120, 120))
    screen.blit(sheet_frames[current_frame], (100, 100))

    # This code serves the purpose of repeating the animation but also
    # prevents the sheet_frames list to exceed it's size
    current_frame += 1
    if current_frame == number_of_sprites:
        current_frame = 0

    pygame.display.update()
    timer.tick(10)

pygame.quit()
