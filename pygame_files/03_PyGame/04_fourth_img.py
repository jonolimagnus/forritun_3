import pygame

pygame.init()

DISPLAY_WIDTH = 600
DISPLAY_HEIGHT = 480

# Load the background image
racetrack = pygame.image.load('images/spaceship.png')
# Load the car images.
blue_car = pygame.image.load('images/bluecar.png')
red_car = pygame.image.load('images/redcar.png')

# As before we need the size of the images.
blue_car_width, blue_car_height = blue_car.get_rect().size
red_car_width, red_car_height = red_car.get_rect().size

# In this demo we place both cars side by side at the bottom of the screen
# on each side of the "middle line". Lets have about 10 pixels of space between them
# and have each one 4 pixels above the bottom of the screen.
blue_car_x = (DISPLAY_WIDTH / 2) - (blue_car_width + 5)
blue_car_y = (DISPLAY_HEIGHT - 4) - blue_car_height

# because the left side of the car is on the right side of the "Middleline"
# we dont't need to add the width, only half of the suggested space between the cars
red_car_x = (DISPLAY_WIDTH / 2) + 5
# identicle to the second line of the blue car since this sets the distance of the cars
# to the bottom of the screen. The height of both cars needs to be taken into
# consideration so that the cars won't be "displayed" off the screen.
red_car_y = (DISPLAY_HEIGHT - 4) - red_car_height

screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Racetrack')

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Since the background image is the same size as the screen, no further calculations
    # are needen and the image is blittet at 0,0 on the screen before the two cars.
    screen.blit(racetrack, (0, 0))
    # now we blit the two cars to the screen
    screen.blit(red_car, (red_car_x, red_car_y))
    screen.blit(blue_car, (blue_car_x, blue_car_y))

    pygame.display.update()

pygame.quit()
