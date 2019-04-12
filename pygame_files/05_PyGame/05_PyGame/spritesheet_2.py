import pygame

pygame.init()

FRAME_WIDTH = 80    # the known width of the frame
FRAME_HEIGHT = 80   # the known height of the frame

screen = pygame.display.set_mode((640, 400), 0, 32)
image = pygame.image.load('dancer_spritesheet.png')

sheet_frames = list()
timer = pygame.time.Clock()
# We still need the size of the sprite sheet
sheet_width, sheet_height = image.get_size()

# Now er are dealing with multiple rows of frames(images) so we need a
# double loop to traverse the sheet, all else is the same.
for row in range(int(sheet_height / FRAME_HEIGHT)):
        for col in range(int(sheet_width / FRAME_WIDTH)):
            sheet_frames.append(image.subsurface((col * FRAME_WIDTH, row * FRAME_HEIGHT, FRAME_WIDTH, FRAME_HEIGHT)))

# Get the size of the list(number of elements/frames)
number_of_sprites = len(sheet_frames)
current_frame = 0

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((200, 200, 200))
    screen.blit(sheet_frames[current_frame], (100, 100))

    current_frame += 1
    if current_frame == number_of_sprites:
        current_frame = 0

    pygame.display.update()
    timer.tick(10)

pygame.quit()