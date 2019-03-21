#jón ólafur
#skilaverkefni 4 erfir

import tkinter# næ í myndræna notendaskil
from tkinter import *
import random
import time

#liður 1
class Okutaki:#bý til parante classa
    def __init__(self,verd,litur):
        self.verd=verd
        self.litur=litur
    def upplysingar(self):
        print("Litur:",self.litur)
        print("Verð:",self.verd)

class Hjol(Okutaki):#bý til child classa
    def __init__(self,verd,litur,nafn,tegund,fjoldi,fjoldi_gira):
        Okutaki.__init__(self,verd,litur)#kemur með parent upplysingarnar með sér
        self.n=nafn
        self.t=tegund
        self.f=fjoldi
        self.fg=fjoldi_gira
    def upplysingar(self):
        print("hjól")
        print("Tegund:",self.t)
        print("Nafn:",self.n)
        print("Fjoldi:",self.f)
        print("Fjoldi gíra:",self.fg)

class Bill(Okutaki):#bý til child classa
    def __init__(self,verd,litur,hamarkshradi,fjoldi_hjola):
        Okutaki.__init__(self,verd,litur)#kemur með parent upplysingarnar með sér
        self.h=hamarkshradi
        self.fh=fjoldi_hjola
    def upplysingar(self):
        print("bíll")
        print("verð:",self.verd)
        print("litur:",self.litur)
        print("Hámarkshraði:",self.h)
        print("Fjöldi hjóla:",self.fh)

class Jardyta(Okutaki):#bý til child classa
    def __init__(self,verd,litur,skofla,hjlabunadur):
        Okutaki.__init__(self,verd,litur)#kemur með parent upplysingarnar með sér
        self.s=skofla
        self.h=hjlabunadur
    def upplysingar(self):
        print("jarðýta")
        print("verð",self.verd)
        print("litur",self.litur)
        print("Stærð skóflu",self.s)
        print("Hjólaumbúðir",self.h)

#aðalforrit
hjol=Hjol(12000,"silfur","dirt bike","Razer",6,12)
print(hjol.upplysingar())
bill=Bill(2500000,"svartu","50km/klst",4)
print(bill.upplysingar())
jardyta=Jardyta(1500000,"gulur","10 metrar lengd og 5 metrar hæð","gúmibelti")
print(jardyta.upplysingar())

#liður 2 myndrænt
#þrýhyrningur kassi og hringur
"""
WIDTH=550 #breidd gluggans
HEIGHT=500 # hæð gluggans
tk=tkinter.Tk()#búið til object úr Tk()klasanum GUI INTERFACE
canvas=tkinter.Canvas(width=WIDTH,height=HEIGHT)#Búinn til strigi sem hægt er að setja hluti á
tk.title("Kassar og önnur form")#nafn á glugga
canvas.pack()#gerðu gluggan fyrir mig
#mismunandi form búin til
canvas.create_line(0,0,500,400)#bý til línu frá punkti (0,0) að punkti (500,400)
canvas.create_rectangle(100,100,200,250,fill="yellow")#tbýr til bláan kassa frá hægra efri horn (100,100) neðra vinstra horn(200,250)
canvas.create_oval(10,10,300,50,fill="green")#býr til sporöskjulagaðan hring inn í kassa sem afmarkast af (10,10)og (300,50)
canvas.create_polygon(400,10,300,300,500,300,fill="purple")# þarf þrjá punkta til að mynda þríhyrning(400,10)(300,300)(500,300)
tk.mainloop()#slaufa sem keyrir forritið



#ranodm myndrænar línur
WIDTH=600 #breidd gluggans
HEIGHT=500 # hæð gluggans
tk=Tk()#búið til object úr Tk()klasanum
canvas=Canvas(width=WIDTH,height=HEIGHT)#Búinn til strigi sem hægt er að setja hluti á
tk.title("random kassar")#nafn á glugga
canvas.pack()#gerðu gluggan fyrir mig
for i in range(500):# býr til 500 kassa með random staðsetningu og stærð
    x1=random.randrange(500)
    y1=random.randrange(400)
    x2=random.randrange(400)
    y2=random.randrange(500)
    canvas.create_rectangle(x1,y1,x2,y2)
    tk.update()#teiknar upp á nýtt
    time.sleep(0.1)
tk.mainloop()


#bolti sem hreyfist
WIDTH=800#breidd
HEIGHT=600#hæð
tk=tkinter.Tk()#búið til object úr Tk(klasanum
canvas=tkinter.Canvas(width=WIDTH,height=HEIGHT)#Búinn til strigi sem hægt er að setja hluti á
tk.title("Skoppandi bolti")#nafn á glugga
canvas.pack()#gerðu gluggan fyrir mig
#búinn til hringur(bolti)sem inn ritast í kassa (efra horn(10,10)neðra horn(60,60)s.s þvermál 50
ball=canvas.create_oval(10,10,60,60,fill="orange")
x_speed=8#hraði í lárétta átt
y_speed=9# hraði í lóðrétta átt
while True:#heldur endalaust áfram
    canvas.move(ball,x_speed,y_speed)#hringur færður til
    pos=canvas.coords(ball)#fundin staðsetnig á hringnum
    #print(pos)#[14.0, 15.0, 64.0, 65.0]     (14,15)efrahorn vinstri (64,65)neðra horn hægri
    if pos[3]>=HEIGHT or pos[1]<=0:#ef hringurinn er kominn að útjaðri strigans(gluggans).upp og niður
        y_speed=-y_speed# þá breyta um stefnu
    if pos[2]>=WIDTH or pos[0]<=0:# til hliðana
        x_speed=-x_speed

    tk.update()#teiknar upp á nýtt
    time.sleep(0.03)#bíða í 0.03 sekúndur
tk.mainloop()


#100 boltar á ferð
WIDTH=800 #breidd gluggans
HEIGHT=600 # hæð gluggans
tk=tkinter.Tk()#búið til object úr Tk()klasanum
canvas=tkinter.Canvas(width=WIDTH,height=HEIGHT)#Búinn til strigi sem hægt er að setja hluti á
tk.title("100 boltar á ferðinni")#nafn á glugga
canvas.pack()#gerðu gluggan fyrir mig
class Ball:#klasinn Ball
    def __init__(self,color,size):#smiðurinn(construtor)fyrir klasann
        self.shape=canvas.create_oval(10,10,size,size,fill=color)#bolti búinn til
        self.xspeed=random.randrange(-10,10)#random láréttur hraði
        self.yspeed=random.randrange(-10,10)#random lóðréttur hraði
    def move(self):#fall sem hreyfir boltann og sér til þess að bolinn komist ekki út úr glugganum
        canvas.move(self.shape,self.xspeed,self.yspeed)
        pos=canvas.coords(self.shape)
        if pos[3]>=HEIGHT or pos[1]<=0:
            self.yspeed=-self.yspeed
        if pos[2]>=WIDTH or pos[0]<=0:
            self.xspeed=-self.xspeed
balls=[]#búinn til listi
colors=["red","green","blue","yellow","black"]#búinn til listi af litum
#hægt að bæta handvirkt bolta inn í listann
#newball=Ball("red",50)# liturinn rauður og stærðin 50(réttara sagt 40 pixlar)
#balls.append(newball)
#mun sniðugra að gera það gegnum for slaufu
for i in range(100):#keyrir 100 sinnum
    balls.append(Ball(random.choice(colors),random.randrange(50,100)))#setur 100 tilvik(object)í listann
#ball=canvas.create_oval(10,10,60,60,fill="orange")
x_speed=4
y_speed=5
while True:
    for ball in balls:
        ball.move()
    tk.update()#teiknar upp á nýtt
    time.sleep(0.03)
tk.mainloop()
"""

#100 form á ferð
WIDTH=800 #breidd gluggans
HEIGHT=600 # hæð gluggans
tk=tkinter.Tk()#búið til object úr Tk()klasanum
canvas=tkinter.Canvas(width=WIDTH,height=HEIGHT)#Búinn til strigi sem hægt er að setja hluti á
tk.title("100 form á ferðinni")#nafn á glugga
canvas.pack()#gerðu gluggan fyrir mig
class Ball:
    def __init__(self,color,size):#smiðurinn(construtor)fyrir klasann
        self.shape=canvas.create_oval(10,10,size,size,fill=color)#bolti búinn til
        self.xspeed=random.randrange(-10,15)#random láréttur hraði
        self.yspeed=random.randrange(-10,15)#random lóðréttur hraði
    def move(self):
        canvas.move(self.shape,self.xspeed,self.yspeed)
        pos=canvas.coords(self.shape)
        if pos[3]>HEIGHT or pos[1]<=0:
            self.yspeed=-self.yspeed
        if pos[2]>=WIDTH or pos[0]<=0:
            self.xspeed=-self.xspeed
balls=[]
colors=["red","green","blue","yellow","black"]#búinn til listi af litum
for i in range(30):#keyrir 30 sinnum
    balls.append(Ball(random.choice(colors),random.randrange(50,100)))#

class Rectangel:
    def __init__(self,color,size):
        self.shape=canvas.create_rectangle(100,100,200,250,fill=color)#kassa búinn til
        self.xspeed=random.randrange(-10,10)#random láréttur hraði
        self.yspeed=random.randrange(-10,10)#random lóðréttur hraði
    def move(self):
        canvas.move(self.shape,self.xspeed,self.yspeed)
        pos=canvas.coords(self.shape)
        if pos[3]>HEIGHT or pos[1]<=0:
            self.yspeed=-self.yspeed
        if pos[2]>=WIDTH or pos[0]<=0:
            self.xspeed=-self.xspeed
rectangels=[]
for i in range(40):
    rectangels.append(Rectangel(random.choice(colors),random.randrange(50,100)))

class Oval:
    def __init__(self,color,size):
        self.shape=canvas.create_oval(10,10,300,50,fill=color)#hting búinn til
        self.xspeed=random.randrange(-10,10)#random láréttur hraði
        self.yspeed=random.randrange(-10,10)#random lóðréttur hraði
    def move(self):
        canvas.move(self.shape,self.xspeed,self.yspeed)
        pos=canvas.coords(self.shape)
        if pos[3]>HEIGHT or pos[1]<=0:
            self.yspeed=-self.yspeed
        if pos[2]>=WIDTH or pos[0]<=0:
            self.xspeed=-self.xspeed
ovals=[]
for i in range(30):
    ovals.append(Oval(random.choice(colors),random.randrange(25,50)))

x_speed=4
y_speed=5
while True:
    for ball in balls:
        ball.move()

    for rectangel in rectangels:
        rectangel.move()

    for oval in ovals:
        oval.move()
    tk.update() #teiknar upp á nýtt
    time.sleep(0.03)
tk.mainloop()

#mynd á hreyfingu
