#jón ólafur
#æfingaverk lambda

"""
listi_minn=[1,12,23,34,4,5,56,7,8,89]
f= lambda x:x*x
listi=[f(x) for x in listi_minn]
print(listi)

#filter
#skilar sletttum tolum
my_list = [1,5,4,6,8,11,3,12]
new_list = list(filter(lambda x: (x%2==0), my_list))

print(new_list)

#map
#sinumar við tvö
my_list = [1,5,4,6,8,11,3,12]
new_list = list(map(lambda x: x*2, my_list))

print(new_list)

#reduce
from functools import reduce
product = reduce((lambda x, y: x *y), [1,2,3,4])
print(product # skilar 24
 prduct = 1
 list = [1,2,3,4]
 from num in list:
    product = product *num
#skilar 24
"""

#liður 1

print("listi 1")
list1 = ["ha"]
f = lambda x: "halllo"
listi =[f(x) for x in list1]

print(listi)

print("listi 1")
listi2=[1,12,23,34,4,5,56,7,8,89]
fa= lambda x: x*x*x
nyr_listi2 = [fa(x) for x in listi2]
print(nyr_listi2)

print("listi 3")
listi3 = [1,12,23,34,4,5,56,7,8,89]
f3= lambda x: x *4
nyr_listi3 = [f3(x) for x in listi3]
print(nyr_listi3)

#liður 2
print("listi sem 3 gengur upp í")
listi = [1,2,3,5,6,9,12,13,15,16,18]
nyr_listi = list(filter(lambda x: (x%3==0), listi))
print(nyr_listi)

#liður 3
print("listi sem sinumar með 4")
sinum_listi= list(map(lambda x: x*4, listi))
print(sinum_listi)

#pygame
#kassi sem hreyfist óstjónlega um skja
import pygame

pygame.init()

#litirnir
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 150, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

#stærðinn á skjánum
window_size = 600, 400#1200, 800
window=pygame.display.set_mode(window_size)
#liturinn á bakgruninum
window.fill(YELLOW)

pygame.display.set_caption('stjórnlaus kassi')

#staðsetninginn á kassanium
xr_position = 160
yr_position = 260
#staðsetinginn á hringinum
xc_position = 500
yc_position = 250

# hraði
xr_velocity = 8
yr_velocity = 4

xc_velocity = 5
yc_velocity = 3

clock = pygame.time.Clock()
clock_ticks = 100

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#er lika hægt að yta á exið í hroninu
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:#sitt a sem lykill tila hætta
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_b:
            print(xc_position,yc_position,xr_position,xc_position)

    window.fill(YELLOW)
    pygame.draw.rect(window, BLUE, pygame.Rect(xr_position, yr_position, 10, 10))
    pygame.draw.circle(window, RED, (xc_position, yc_position), 10)

    # position update(based on current velocity)
    #kassing
    xr_position += xr_velocity
    yr_position += yr_velocity
    #hringurinn
    xc_position += xc_velocity
    yc_position += yc_velocity

    # We need to check all sides of the window to see if the rect has touched them.
    # To have the rect turn around when it touches one of the windows sides we invert
    # it's direction by multiplying the components of the velocity vector by -1.
    # We also need to subtract the size of the rectangle so that we do not get some
    # surprises during the turnaround.
    #kassin
    if yr_position > 400 or yr_position < 0:  # top - bottom check
        yr_velocity *= -1

    if xr_position > 600 or xr_position < 0:  # left - right check
        xr_velocity *= -1
    #hringurinn
    if yc_position > 400 or yc_position < 10:  # top  bottom check
        yc_velocity *= -1
    if xc_position > 600 or xc_position < 10:  # left  right check
        xc_velocity *= -1

    #reinna að fá forritið til að hætta ef þeir rekast á hvort annað
    if xc_position == xr_position or xc_position == xr_position or yc_position == yr_position or yc_position == xr_position:
        xc_velocity = 0
        yc_velocity = 0
        xr_velocity =0
        yr_velocity =0
        print(xc_position,yc_position,xr_position,xc_position)




    pygame.display.update()

    clock.tick(100)
pygame.quit()
