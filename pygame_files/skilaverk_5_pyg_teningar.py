#jón ólafur
#skilaverk 5

import pygame
import random

pygame.init()

Blue = (0, 0, 255)
RED = (255, 0, 0)


#classi fyrir teningana
class Teningur():
    def __init__(self,ten_img,x_pos,y_pos):
        self.image = pygame.image.load(ten_img).convert()
        self.ten = self.image.get_rect()
        self.ten.x = x_pos
        self.ten.y = y_pos
        self.name = str(ten_img.rsplit('/',1)[1])

my_font = pygame.font.SysFont("comic sans MS", 30)#letur stærð
#skjár
screen_width = 880
screen_height = 680

screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("tengingar")#nafn gluggans
teningalisti= list()#listi til að geima teninga
rect_list=list()
xid=30
listi=[]
listiten=[]
remove_listi=[]
teljari = 0
for x in range(6):#geri box fyrir collidepont
    rect_list.append(pygame.Rect(xid,30,100,100))
    xid+=130

#sett í listann
teningalisti.append(Teningur('ten/t1.jpg',30,30))
teningalisti.append(Teningur('ten/t2.jpg',160,30))
teningalisti.append(Teningur('ten/t3.jpg',290,30))
teningalisti.append(Teningur('ten/t4.jpg',420,30))
teningalisti.append(Teningur('ten/t5.jpg',550,30))
teningalisti.append(Teningur('ten/t6.jpg',680,30))
templisti = teningalisti.copy()
#takkinn ýttu á mig búinn til
takki = pygame.Rect(50, 200, 150, 80)#takki staða á skjá
pygame.draw.rect(screen, Blue, takki)#takkin búinn til og litaður
texti = my_font.render("ýttu á mig", True, RED)#stafirnir í takkanum settir inn og litaðir
screen.subsurface(takki)
screen.subsurface(takki).blit(texti, (3, 20))#staðseting textans sett inn á takkan
#takkin reyndu aftiur búinn til
reyna = pygame.Rect(50, 350, 200, 80)#takki staða á skjá
pygame.draw.rect(screen, Blue, reyna)#takkin búinn til og litaður
texti = my_font.render("reyndu aftur", True, RED)#stafirnir í takkanum settir inn og litaðir
screen.subsurface(reyna)
screen.subsurface(reyna).blit(texti, (3, 20))#staðseting textans sett inn á takkan
#takkin upplýsingar búinn til
info = pygame.Rect(300, 200, 400, 200)#takki staða á skjá
pygame.draw.rect(screen, Blue, info)#takkin búinn til og litaður
texti = my_font.render("stig", True, RED)#stafirnir í takkanum settir inn og litaðir
screen.subsurface(info)
screen.subsurface(info).blit(texti, (3, 20))#staðseting textans sett inn á takkan


def stig(listi):#geri stiginn
    stig = 0
    l=[]
    a=set(listi)#í a kermur hver ala bara einu sinni
    for tala in a:
        l.append(listi.count(tala))
    l.sort(reverse=True)
    print(l)
    for x in l:
        if len(l)==6:# í röð gefa 500
            stig=500
            break
        if l.count(x)==3 and x==2:
            stig=100
            break
        if x ==6:stig+=600
        if x ==5:stig+=350
        if x ==4:stig+=250
        if x ==3:stig+=80
        if x ==2:stig+=20
    return stig



running = True

flag=False
while running:
    if flag:
        teljari=0
        flag=False
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
    if event.type == pygame.MOUSEBUTTONDOWN:# and teljari <3:
        if reyna.collidepoint(event.pos):#reyndu aftur takkin
            listi.clear()
            teljari=0
            stig=0
            pygame.draw.rect(screen, Blue, info)
            strengur="stig"
            texti = my_font.render(strengur, True, RED)
            screen.subsurface(info)
            screen.subsurface(info).blit(texti, (3, 20))

            flag=True
        if  takki.collidepoint(event.pos) and teljari <3:#ýttu á mig takkin
            #rugla teningurm
            teljari +=1
            xhnit=30
            yhnit=30
            for x in range(6):
                if x not in listi:#ef búið er að frysta tening þá á ekki að setja nýja tölu í stað
                    ten=templisti[random.randint(0,len(templisti)-1)]
                    teningalisti[x]=ten
                #teningalisti.append(templisti[random.randint(0,6)])
            for ten in teningalisti:
                screen.blit(ten.image, (xhnit,yhnit))#í stað ten.rect.x og y
                xhnit+=130
            if teljari ==3:
                listiten.clear()
                for ten in teningalisti:
                    tala =int (ten.name[1])
                    listiten.append(tala)
                print(listiten)
                strengur=str(stig(listiten))
                texti = my_font.render(strengur, True, RED)
                screen.subsurface(info).blit(texti, (3,60))
                print(stig(listiten))

            for box in rect_list:
                if box.collidepoint(event.pos):
                    list.append(rect_list.index(box))

                """
        for box in teningalisti:
            if box.ten.collidepoint(event.pos):
                print(box.name)
"""
    pygame.display.flip()

pygame.quit()
