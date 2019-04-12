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
pygame.display.set_caption('The Wizard Waves When We Want')

frames = sprite_loader(50, 72, 'duke_spritesheet.png')
number_of_sprites = len(frames)
timer = pygame.time.Clock()

current_frame = 0
frame_counter = 0
# lets introduce a status variable for the wave behaviour.
# when the "game" starts the Duke can not wave.
the_duke_can_wave = False

running = True

while running:
    # Now we are going to get some control over the Duke.
    # He is not going to wave unless we "tell" him to
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False
            sys.exit()
        # When a mouse is pressed down, the Duke is allowed to wave
        if event.type == pygame.MOUSEBUTTONDOWN:
            the_duke_can_wave = True
        # If we release the mouse button the Duke stops waving
        if event.type == pygame.MOUSEBUTTONUP:
            the_duke_can_wave = False

    screen.fill((200, 200, 200))
    screen.blit(frames[int(current_frame)], (100, 100))

    # A little fix should the FPS go below 10.
    frame_control = FRAMES_PER_SECOND
    if frame_control < 10:
        frame_control = 10

    # if the duke is allowed to wave, this code runs:
    if the_duke_can_wave > 0:
        frame_counter = (frame_counter + 1) % frame_control
        current_frame = frame_counter // (frame_control / WIZARD_SPEED)

    pygame.display.update()
    timer.tick(FRAMES_PER_SECOND)
