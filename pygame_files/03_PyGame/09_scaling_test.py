import pygame

pygame.init()

# hlöðum inn mynd.
dice_image = pygame.image.load('images/sd0.png')
# keyrum transform.scale fallið
dice_image = pygame.transform.scale(dice_image, (50, 50))  # this code reduces the image size about half.

# náum í rect sem er stærð myndarinnar
image_rect = dice_image.get_rect()

SCREEN_COLOR = (0, 60, 0)
WINDOW_SIZE = (800, 480)

screen = pygame.display.set_mode(WINDOW_SIZE)
screen.fill(SCREEN_COLOR)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        screen.fill(SCREEN_COLOR)
        screen.blit(dice_image, image_rect)  # blittum myndinni
    pygame.display.update()

pygame.quit()
