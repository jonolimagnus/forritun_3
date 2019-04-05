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

# the cars initial positions
blue_car_x = (DISPLAY_WIDTH / 2) - (blue_car_width + 5)
blue_car_y = (DISPLAY_HEIGHT - 4) - blue_car_height
red_car_x = (DISPLAY_WIDTH / 2) + 5
red_car_y = (DISPLAY_HEIGHT - 4) - red_car_height

# the red cars initial velocity.
# this would mean that the red car is not moving at all in the two directions.
red_vel_x = 0
red_vel_y = 0

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
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                red_vel_y = 0

    # Here is where the y position(vertical) if the red car is updated according to the velocity
    red_car_y += red_vel_y

    screen.blit(racetrack, (0, 0))
    screen.blit(red_car, (red_car_x, red_car_y))
    screen.blit(blue_car, (blue_car_x, blue_car_y))

    # As a last measure we add a boundary check to keep the red car on the screen
    # There's no need to check the left and right boundaries due to the fact
    # that the red car can only travel in one direction, up or down.
    if red_car_y > DISPLAY_HEIGHT - red_car_height or red_car_y < 0:
        red_vel_y = 0   # stops the car moving out of the screen. Or does it???

    pygame.display.update()

pygame.quit()
