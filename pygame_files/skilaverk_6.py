#jón ólafur
#skilaverk 6

import pygame
import time

pygame.init()

class Veggur(object):#geri veggina
    def __init__(self,pos):
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

class Sprengju_vorn(object):#gerri
    def __init__(self,pos):
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)


class Sprengjur(object):
    def __init__(self,pos):
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

class Spilari():
    def __init__(self):
        self.rect = pygame.Rect(32,32, 16, 16)
    def move(self, dx, dy):
        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

    def move_single_axis(self, dx, dy):
        # Move the rectangle
        self.rect.x += dx
        self.rect.y += dy
        # If you collide with a wall, move out based on velocity
        for kassi in veggir:
            if self.rect.colliderect(kassi.rect):
                if dx > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = kassi.rect.left
                if dx < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = kassi.rect.right
                if dy > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = kassi.rect.top
                if dy < 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = kassi.rect.bottom
        for skyldir in sprengju_vorn:#ef það er hitt á sprengju vörn þá er hún tekinn af kortinu
            if self.rect.colliderect(skyldir.rect):
                print("þú náðir í skjöld")
                print("sprengju vörninn kostar 5")
                stig = upphafsstig-skjoldur
                sprengju_vorn.remove(skyldir)


pygame.display.set_caption("komdu þér út")
screen = pygame.display.set_mode((640, 480))

clock = pygame.time.Clock()
veggir = list()#geri lista fyrir veggi
sprengju_vorn = list()#geri lista fyrir sprengju vörnin
spilari = Spilari()# geri spilaran
sprengjulisti=[]
#mazeið v = skyldir s = sprengjur w = veggir E = exit,
maze = [
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"W            V               WWWW   S W",
"W     W    WWWWWWWWWWWWW           WWWW",
"W   WWWWS       S        W            W",
"W   W        WWWWWWWWWWWW        WW VWW",
"WSWWW  WWWW     S                 WWWWW",
"W   W     W W                 WWWW    W",
"W   W    VW   WWW       WWWWWW       WW",
"W   WWW WWW   W W                     W",
"W        W   W   WWW                  W",
"WWW      W   WWWWW W                  W",
"W W      V  WW                     S  W",
"W W    WWWW W WWW                   WWW",
"W              S S                WWWWW",
"W      WWWW WWWWWWWWWWWW         WWWWWW",
"W             WW                      W",
"WWWWWWWWWWW    WW           WWWWW    W",
"W               WWW        W          W",
"W                 WWW    WW  WWWWWWWWWW",
"WWWWWWWWW              WW             W",
"W                     WWWW   V        W",
"W        WWWWWWWWWWW    S      WWWWWWWW",
"W                 WWWWWWW             W",
"WWWWW       WWW            V  WWWWWWWWW",
"W V      WWW       S            S    EW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
]
x = 0
y=0
for row in maze:
    for col in row:
        if col == "W":
            veggir.append(Veggur((x,y)))
        if col == "E":
            end_rect = pygame.Rect(x,y,16,16)
        if col == "S":
            sprengjur = Sprengjur((x,y))
            sprengjulisti.append(sprengjur)
        if col == "V":
            sprengju_vorn.append(Sprengju_vorn((x,y)))
        x+=16
    y+=16
    x=0

print("bláir eru skyldir og rauðir eru sprengjur")
running = True
stig = 0
skyldir = 1
upphafsstig = 30
skjoldur=5
sprenging = 10
print("þú ert með",upphafsstig)
while running:

    clock.tick(60)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False

    # Move the player if an arrow key is pressed
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        spilari.move(-2, 0)
    if key[pygame.K_RIGHT]:
        spilari.move(2, 0)
    if key[pygame.K_UP]:
        spilari.move(0, -2)
    if key[pygame.K_DOWN]:
        spilari.move(0, 2)

    if spilari.rect.colliderect(end_rect):
        print("þú vannst með", stig)
        raise SystemExit()

    """
    for sprengjur in sprengjulisti:
        if spilari.rect.colliderect(sprengjur.rect):
            if
"""
    for sprengja in sprengjulisti:

        if spilari.rect.colliderect(sprengja.rect):
            #skyldir =skyldir- skyldir
            if skyldir>=1:
                print("þú fékkst 10 stig")
                stig =upphafsstig +sprenging
                sprengjulisti.remove(sprengja)
            else:
                print("þú dóst")
                raise SystemExit()
        for skyldir in sprengju_vorn:
            if spilari.rect.colliderect(skyldir):
                skyldir+= 1

    screen.fill((255,255,255))
    for kassi in veggir:#litar veggina
        pygame.draw.rect(screen, (0,0,0), kassi.rect)

    for skyldir in sprengju_vorn:#lita sprengju vörnina
        pygame.draw.rect(screen, (0,0,255), skyldir.rect)

    for sprengja in sprengjulisti:#litur spregnju
        pygame.draw.rect(screen, (204,0,0),sprengja.rect)


    pygame.draw.rect(screen, (255,0,0),end_rect)

    pygame.draw.rect(screen, (200,200,0),spilari)

    pygame.display.flip()
