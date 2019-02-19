#jón ólafur
#afingaverk klasar
import random
import math
import time

class Trapis():
    teljari = 0
    def __init__(self,a=0,b=0,c=0,d=0,h=0):
        if a <0 or b<0 or c <0 or d<0 or h<0:
            raise ValueError("lengdir verða að vera + tölur")
        else:
            self.a=a
            self.b=b
            self.c=c
            self.d=d
            self.haed=h
            Trapis.teljari+=1
    def ummal(self):
        return self.a+self.b+self.c+self.d
    def flatarmal_1(self):
        s = (self.a+self.b+self.c+self.d)/2
        return ((self.a+self.c)/(self.a-self.c))*math.sqrt((s-self.c)*(s-self.a)*(s-self.c-self.b)*(s-self.c-self.d))
    def flatarmal_2(self):
        return self.haed*((self.a+self.c)/2)
    def jafnarma(self):
        return self.d==self.b#skilar True/Flase
    def skilgreining_a_ser(self):
        print("Trapisa eða hálfsamsíðungur er ferhyrningur þar sem tvær mótlægar hliðar eru samsíða")

class Froskar():
    def eiginleikar(self):
        pass
class kerlufroskar():
    def eiginleikar(self):
        pass
class test():
    def fjoldi(self):
        pass
        #if magn =>10000:


class Bill:
    """Þessi klassi býr til bíl"""
    def __init__(self,t="",a=0,h=0,b=0,e=0):#er smiðurinn
        self.t=t#tegund
        self.a=a#árgerð
        self.h=h#hraði
        self.b=b#bensín
        self.e=e#eyðsla

    def stada(self,sek):
        kominn_metrar = self.h*sek
        return kominn_metrar#hvað er bíllin búinn að fara marga metra

    def eftir_bensin(self,sek):
        #finnur út hversu mikið bensín er eftir
        eftir_b = self.b-(self.e*self.h*sek//100)
        return eftir_b

    def eg(self):
        print("tegund",self.t,"árgerð",self.a,"hraði",self.h,"bensín",self.b,"eyðsla",self.e)

    def keppni(self):
        pass

h=random.randint(10,20)#random hraði metrar á sekúndu
b=random.randint(5000,10000)#RANDOM BENSÍN
e=random.randint(100,1000)#random eyðsla

bil_1=Bill("bens",2018,h,b,e)
bil_1.eg()

print()
h=random.randint(15,25)#random hraði metrar á sekúndu
b=random.randint(5000,10000)#RANDOM BENSÍN
e=random.randint(300,1000)#random eyðsla
bil2=Bill("ford mustang",1995,h,b,e)
bil2.eg()

print()
h=random.randint(10,20)#random hraði metrar á sekúndu
b=random.randint(5000,10000)#RANDOM BENSÍN
e=random.randint(100,1000)#random eyðsla
bil3=Bill("toyota",2010,h,b,e)
bil3.eg()

print()
#byrja að keppa
sek=1
#á meðan ekki eru kominr 1000metrar og enþá eftir bensín
while bil_1.stada(sek)<=1000and bil_1.eftir_bensin(sek)>0:
    print("eldsneyti staða",round(bil_1.eftir_bensin(sek),2))
    print("bíllin er kominn",bil_1.stada(sek),"metra")
    time.sleep(0.1)
    sek= sek+1#sjá hvernig þetta gengur
print(bil_1.t,"kláraði",bil_1.stada(sek),"metrar á",sek,"sekúndum")
print(round(bil_1.eftir_bensin(sek),2),"lítrar voru eftir af bensíni")
if bil_1.stada(sek)<=1000:#ef bílll náði að klára
    timi1=sek
else:
    timi1=-1#ef tímin er -1 þá kláraði bíllin ekki

#á meðan ekki eru kominr 1000metrar og enþá eftir bensín
while bil2.stada(sek)<=1000and bil2.eftir_bensin(sek)>0:
    print("eldsneyti staða",round(bil2.eftir_bensin(sek),2))
    print("bíllin er kominn",bil2.stada(sek),"metra")
    time.sleep(0.1)
    sek= sek+1#sjá hvernig þetta gengur
print(bil2.t,"kláraði",bil2.stada(sek),"metrar á",sek,"sekúndum")
print(round(bil2.eftir_bensin(sek),2),"lítrar voru eftir af bensíni")
if bil2.stada(sek)<=1000:#ef bílll náði að klára
    timi2=sek
else:
    timi2=-1#ef tímin er -1 þá kláraði bíllin ekki

#á meðan ekki eru kominr 1000metrar og enþá eftir bensín
while bil3.stada(sek)<=1000and bil3.eftir_bensin(sek)>0:
    print("eldsneyti staða",round(bil3.eftir_bensin(sek),2))
    print("bíllin er kominn",bil3.stada(sek),"metra")
    time.sleep(0.1)
    sek= sek+1#sjá hvernig þetta gengur
print(bil3.t,"kláraði",bil3.stada(sek),"metrar á",sek,"sekúndum")
print(round(bil3.eftir_bensin(sek),2),"lítrar voru eftir af bensíni")
if bil3.stada(sek)<=1000:#ef bílll náði að klára
    timi3=sek
else:
    timi3=-1#ef tímin er -1 þá kláraði bíllin ekki

class val():
    pass
#aðalforrit
#trapis
print("allar hliðar þurfa að vera í plús tölum")
a= int(input("sláðu inn hlið 1"))
b= int(input("sláðu inn hlið 2"))
c= int(input("sláðu inn hlið 3"))
d= int(input("sláðu inn hlið 4"))
haed = int(input("sláðu inn hæð"))
trapis =Trapis(a,b,c,d,haed)#bý til hlut úr klassanum Trapisa
print("þetta er ummál", trapis.ummal())
print("þetta er flatarmál", trapis.flatarmal_1())
print("þetta er annað flatarmál", trapis.flatarmal_2())
if trapis.jafnarma():#ef True
    print("trapisan er jafnarma")
else:
    print("trapisan er ekki jarnarma")
trapis.skilgreining_a_ser()
#froskar

#bílar

#fuck if i know
