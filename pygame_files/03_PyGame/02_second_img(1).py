import pygame

pygame.init()

DISPLAY_WIDTH = 600
DISPLAY_HEIGHT = 480
WHITE = (255, 255, 255)

# Here we load the image and put it in a variable called the_car
the_car = pygame.image.load('images/bluecar.png')
# To be able to "realisticly" place an image on the screen we sometimes(almost always is a good idea)
# need to take into consideration that the image is embedded in a rectangle and the drawing
# mechanisms refer to the upper left corner of that rectangle as a handle to the whole image.
# To find for example the right side, the bottom or the center coordinates we need to know the
# height and the witdh in pixels of the image in question.
# In pygame we can find the image size by calling get_rect().size on that image and
# put this info into two variables. Now we can use these to place the image with
# more accuracy than just using the top left coordinates.
car_width, car_height = the_car.get_rect().size

# In case you need to refer to the image size and it's offsets while developing the game you can use
# the following print statements. Just be sure to remove them when you're done as not to unnecessary clutter the code :-)
print (car_height,car_width)  # --test line --
print (car_height / 2 )       # --test line --
print( car_width / 2 )        # --test line --

# let's put the middle of the car(the image) right in the middle of the screen in both planes(x and y)
# to do this we need to calculate the offset in both height and width from the top left corner, not only
# on the car image but on the screen as well!!
x = (DISPLAY_WIDTH / 2) - (car_width / 2)
y = (DISPLAY_HEIGHT / 2) - (car_height / 2)

screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Image')

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    # now we use the blit-function to draw the car onto the background and then update the display to make it visible.
    screen.blit(the_car, (x, y))
    pygame.display.update()

pygame.quit()
