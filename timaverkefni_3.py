#jón ólafur
#tímaverkefni 3
#30/04/19
import random

#liður 1 heiltölur
def heiltala():#raða heiltölum öfugt og reiknar það saman
    for tala in listi:
        tala2 = tala +tala
        listi2.append(tala2)
    print(listi2)
listi = [32, 56]
listi2 = []
heiltala()
"""
tala1 = [65]
tala2 = [43]
listi1 = list.reverse(tala1)
listi2 = list.reverse(tala2)

"""
#liður 2
class Timaverk3:
    def __init__(self,aldur,kyn):
        self.aldur = aldur
        self.kyn = kyn
    def upplysingar(self):#geri if setningar til að vitta hvort þú ert karl eða kona og hvort þú ert fullorðinn eð aekki
        if self.aldur >=20 and self.kyn == "KK":
            print("þú ert fullorðinn karlmaður")
        elif self.aldur >=20 and self.kyn == "kvk":
            print("þú ert fullorðin kona")
        elif self.aldur >=20 and self.kyn != "KK" and self.kyn != "kvk":
            print("þú ert fullorðin en ert af óræðu kyni")
        elif self.aldur <=19 and self.aldur >= 13 and self.kyn == "KK":
            print("þú ert unglingur og karl")
        elif self.aldur <=19 and self.aldur >= 13 and self.kyn == "kvk":
            print("þú ert unglingur og kona")
        elif self.aldur <=19 and self.aldur >= 13 and self.kyn != "kvk" and self.kyn != "KK":
            print("þú ert unglingur en ert af óræðu kyni")
        elif self.aldur <=12 and self.kyn == "KK":
            print("þú er barn og strákur")
        elif self.aldur <=12 and self.kyn == "kvk":
            print("þú ert barn og stelpa")
        elif self.aldur <=12 and self.kyn != "KK" and self.kyn != "kvk":
            print("þú ert barn en óræður með kyn")
    def tolur_milli(self,a,b,c):#skilar lista milli a b og c
        if a ==b  ==c:
            print("tölurnar eru jafnar")
        else:
            for tala in range(a,b,c+1):
                print(tala,end=" ")
    def konni(self,listin):#nota lambda til af finna tölur stærri en 40
        nyr_listi =list(filter(lambda x: (x > 40), listin))
        print("þetta eru allar tölurnar sem eru hærri en 40 og enda á 1", nyr_listi)
#aðalforrit
timavek = Timaverk3(45,"kvk")
timavek.upplysingar()
timavek.tolur_milli(2,4,7)
print()
listin=[23,56,43,61,71]
timavek.konni(listin)
random_kyn =["KK","kvk","ekkert"]
folk = []
""" #ekki viss hvernig ég geri þetta
for x in range(20):
    kyn=random_kyn[x]
    aldur=random.randint(0-100)
    folk.append(Timaverk3)
print(folk)
"""


#liður3 erfðir
class Frum:#geri parent
    def __init__(self):
        self.nafn = "jón"
    def upplysingar(self):
        print("halló ég er klassin Frum ég heiti",self.nafn)
class Fyrst(Frum):#geri kid
    def __init__(self,setning,tala):#geri smið
        Frum.__init__(self)
        self.setning = setning
        self.tala =tala
    def upplysingar(self):#skrifa upplysingar
        print("halló ég er klassin Fyrst ég heiti",self.nafn)
    def fall(self,setning,tala):#geri fall sem reiknar töluna og geri setinguna það langa
        set_listi = setning
        end_listi = set_listi *tala
        print(end_listi,end=" ")
hlutur1 = Frum()
hlutur2= Fyrst("Hæ",3)
print(hlutur1.nafn)
hlutur1.upplysingar()
print(hlutur2.nafn)
hlutur2.upplysingar()
hlutur2.fall("Hæ ",3)
