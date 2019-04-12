import sys
import pygame


def sprite_loader(sprite_width, sprite_height, sheet_file):
    sprite_frames = []

    image = pygame.image.load(sheet_file).convert_alpha()
    width, height = image.get_size()

    for r in range(int(height / sprite_height)):
        for c in range(int(width / sprite_width)):
            sprite_frames.append(image.subsurface((c * sprite_width, r * sprite_height, sprite_width, sprite_height)))

    return sprite_frames

pygame.init()

FRAMES_PER_SECOND = 60
WIZARD_SPEED = 10

screen = pygame.display.set_mode((640, 400))
pygame.display.set_caption('The Wizard is Waving')

frames = sprite_loader(50, 72, 'duke_spritesheet.png')
number_of_sprites = len(frames)
timer = pygame.time.Clock()

# We are now going to have a red rectangle move across the screen at a constant speed.
# By varying the frame rate it is possible to compare the Dukes movements with the speed
# of the rectangle.  The desired result should be that the waving should not change that
# much but the speed of the rect will.
rect_x_position = 0
frame_counter = 0
current_frame = 0

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False
            sys.exit()

    screen.fill((200, 200, 200))
    screen.blit(frames[int(current_frame)], (100, 100))

    # A little fix should the FPS go below 10.
    frame_control = FRAMES_PER_SECOND
    if frame_control < 10:
        frame_control = 10

    # The Duke now waves all the time
    frame_counter = (frame_counter + 1) % frame_control
    current_frame = frame_counter // (frame_control / WIZARD_SPEED)

    # the rect_x_position is increased by 2 every round.
    rect_x_position += 2

    # Since we are using this program to visually compare the movement of its
    # artifacats, we implement a "wrap-around" functionality for the rectangle.
    if rect_x_position >= 640:
        rect_x_position = -30
    # We draw the rectangle
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(rect_x_position, 300, 30, 30))

    pygame.display.update()
    timer.tick(FRAMES_PER_SECOND)
