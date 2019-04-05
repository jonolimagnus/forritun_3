# coding=UTF-8
import pygame

pygame.init()

window_size = window_width, window_height = 640, 480
window = pygame.display.set_mode(window_size)

pygame.display.set_caption('Move the box in 2D')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# upphafsstaða rauða kassans er á miðjum skjánum
x_position = 310
y_position = 230

# upphafshraðinn er núll í báðar áttir(kassinn er kjurr)
x_velocity = 0
y_velocity = 0

window.fill(BLUE)

clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # ef einhver takki á lyklaborðinu fer niður þá þarf að tékka
        # á því hvaða takki það er. Í þessu demói erum við bara að
        # vinna með örvartakkana.
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # playerinn ýtti á vinstri örina og við setjum hraðann á 2 í mínus(til vinstri)
                x_velocity = -2
            elif event.key == pygame.K_RIGHT:
                x_velocity = 2
            elif event.key == pygame.K_UP:
                y_velocity = -2
            elif event.key == pygame.K_DOWN:
                y_velocity = 2
        # ef playerinn sleppir takkanum þá er hreyfingin stoppuð í x og y átt.
        # hér má bæta við ef einungis á að stoppa í þá átt sem sleppti takkinn
        # sýnir.
        # ALTSVO: ef ég er að fara upp til hægri og sleppi hægri örinni en held
        #         hinni niðri þá er einungis hraðinn til hægti settur á 0, ekki báðar áttir
        elif event.type == pygame.KEYUP:
            x_velocity = 0
            y_velocity = 0

    # staðan á rauða kassanum uppfærð miðað við hraðan(current speed)
    x_position += x_velocity
    y_position += y_velocity

    window.fill(BLUE)
    pygame.draw.rect(window, RED, pygame.Rect(x_position, y_position, 20, 20))

    # ef kasinn okkar er kominn að brúnum sjásins þá er hreyfing stöðvuð
    # i þá átt sem kassinn er að fara þegar hann rekst á skjábrúnina
    if y_position > 460 or y_position < 0:
        y_velocity = 0
    if x_position > 620 or x_position < 0:
        x_velocity = 0

    pygame.display.update()
    clock.tick(60)
pygame.quit()