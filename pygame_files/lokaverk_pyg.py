#jón ólafur
#lokavrkefni

import pygame

pygame.init()

"""
class Veggur(object):#geri veggina
    def __init__(self,pos):
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)
"""#ekki mikilvægt


class Geimskip(pygame.sprite.Sprite):# geri geimskip
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load("03_pygame/images/spaceship.png").convert()#sett inn mynd fyrir geimskipi
        self.rect = self.img.get_rect()
    def move(self):
        """
        self.speedx = 0
        if event.type == KEYDOWN and event.key == k_LEFT:
            self.speedx = -1
        elif event.type == KEYDOWN and event.key == K_RIGHT:
            self.speedx = 1
            """
    def skot(self):
        missile = Missile(self.rect.centerx,self.rect.top)
        allSprites.add(missile)
        Missile.add(missile)

class Geimverur:
    pass

class Missile(pygame.sprite.Sprite):
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)


pygame.display.set_caption("space invaders")
screen = pygame.display.set_mode((640, 480))

#veggir = list()#geri lista fyrir veggi
geimskip = Geimskip()#geri spilaran
geimverur = Geimverur()#geri óvinina

running = True

while running:

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        geimskip.move(-2, 0)
    if key[pygame.K_RIGHT]:
        geimskip.move(2, 0)
