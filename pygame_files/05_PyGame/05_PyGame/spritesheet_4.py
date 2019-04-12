import sys
import pygame

# The Duke Java Mascot image is on a freee lisence from Oracle:
# Web: https://duke.kenai.com/wave/index.html
# Accessed: 16.10.2016
# Note: The sanity of using something from Java in a Python educational material can be questioned.
#       However the Duke is a well designed graphic that offers clarity through it's simple structure.

'''
    Up to now our code has depended on choosing a low frame rate so that our
    animation does not become unusable due to speed.  The thing to realize here
    is that the "playback" of the sprite frames(the images in the array) should
    be separated from the actual frame rate chosen. This is done in line 51 and 52.
'''

# Our sprite loading function.
def sprite_loader(sprite_width, sprite_height, sheet_file):
    sprite_frames = []

    image = pygame.image.load(sheet_file).convert_alpha()
    width, height = image.get_size()

    for r in range(int(height / sprite_height)):
        for c in range(int(width / sprite_width)):
            sprite_frames.append(image.subsurface((c * sprite_width, r * sprite_height, sprite_width, sprite_height)))

    return sprite_frames

pygame.init()

# A point about constants in python:
# Over the years the practice of haveng constat names written in upper case letters
# is globally accepted. Even if we use this notion here, Python has no way of knowing
# that we are defining a constant and considers it just like any another variable.
# Any experienced programmer will however realize that the intention is to create a constant
# and will most likely honor that and not change it's value even if (s)he can.
# Should we really need unmutable storage (constants) we can use tuples.
FRAMES_PER_SECOND = 10
WIZARD_SPEED = 10

screen = pygame.display.set_mode((640, 400))
pygame.display.set_caption('The Wizard is Waving')

frames = sprite_loader(50, 72, 'duke_spritesheet.png')
number_of_sprites = len(frames)
timer = pygame.time.Clock()

current_frame = 0
frame_counter = 0

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False
            sys.exit()

    screen.fill((200, 200, 200))
    screen.blit(frames[int(current_frame)], (100, 100))

    # This code ensures a relatively constant speed of the sprite animation
    # irrespective of the frames per second that have been chosen for the game.
    # it's role is to tie the animation to the frame rate at wich the game is running.
    # This is by no means perfect since it cannot(unchanged) handle FPS below 10.
    # you should test this "speed limits" by varying the value of the FRAMES_PER_SECOND constant.
    # Experimenting with this code section is not a bad idea at all.
    frame_counter = (frame_counter + 1) % FRAMES_PER_SECOND
    current_frame = frame_counter // (FRAMES_PER_SECOND / WIZARD_SPEED)


    pygame.display.update()
    timer.tick(FRAMES_PER_SECOND)
