import pygame

pygame.init()

DISPLAY_WIDTH = 600
DISPLAY_HEIGHT = 480

# Load the background image
racetrack = pygame.image.load('images/spaceship.png')
# Load the car images.
blue_car = pygame.image.load('images/bluecar.png')
red_car = pygame.image.load('images/redcar.png')

# image sizes
blue_car_width, blue_car_height = blue_car.get_rect().size
red_car_width, red_car_height = red_car.get_rect().size

# red car initial position
blue_car_x = (DISPLAY_WIDTH / 2) - (blue_car_width + 5)
blue_car_y = (DISPLAY_HEIGHT - 4) - blue_car_height
# blue car initial position
red_car_x = (DISPLAY_WIDTH / 2) + 5
red_car_y = (DISPLAY_HEIGHT - 4) - red_car_height

# the red cars initial velocity.
red_vel_x = 0
red_vel_y = 0
# the red cars initial velocity.
blue_vel_x = 0
blue_vel_y = 0

screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Racetrack')

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # we will be moving the red car up and down the "track" and therefore we need to
        # change the y position response to the player pressing the up or down arrows.
        # Since we are not moving the car to the right or left we do not alter the
        # vertical position (red_car_x).  That is why we only handle the up and down arrows.
        # We want the behavior to be that if the player presses an arrow the velocity changes
        # about 2 in the respective direction.  Once the plkayer releases the arrow key the
        # velocity is set to 0 and as a result the car stopps.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                red_vel_y = -2
            elif event.key == pygame.K_DOWN:
                red_vel_y = 2
            if event.key == pygame.K_w:
                blue_vel_y = -2
            elif event.key == pygame.K_s:
                blue_vel_y = 2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                red_vel_y = 0
            if  event.key == pygame.K_w or event.key == pygame.K_s:
                blue_vel_y = 0

    # car postitons updated
    red_car_y += red_vel_y
    blue_car_y += blue_vel_y

    screen.blit(racetrack, (0, 0))
    screen.blit(red_car, (red_car_x, red_car_y))
    screen.blit(blue_car, (blue_car_x, blue_car_y))

    # To fix the "glitch" from last demo we ajust the postition of the red car
    # to remain fixed if the car has collided with the top or bottom border.
    # We do not need to ajust the velocity as such in this case since the car is
    # only able to go in the opposite direction if the player presses the opposite arrow.
    if red_car_y > DISPLAY_HEIGHT - red_car_height:
        red_car_y = DISPLAY_HEIGHT - red_car_height
    elif red_car_y < 0:
        red_car_y = 0
    # To make things a bit different for the blue car we'll have him disappear only
    # to reemerge on the opposite site, continuing its original direction.
    if blue_car_y > DISPLAY_HEIGHT:
        blue_car_y = 0 - blue_car_height
    elif blue_car_y + blue_car_height < 0:
        blue_car_y = DISPLAY_HEIGHT

    pygame.display.update()

pygame.quit()
