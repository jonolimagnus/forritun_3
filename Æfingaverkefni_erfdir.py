#Höfundur: Óskar Agnarsson
import math
class Rummal:
    def upplysingar(self):
        print("Ég er klasi sem reiknar út rúmmál hluta")

class Kula(Rummal):
    def __init__(self,radius):
        self.radius=radius
    def thvermal(self):
        return self.radius*2
    def rummal(self):
        return round((4*math.pi*math.pow(self.radius,3))/3,2)

class Kassi(Rummal):
    def __init__(self,l,b,h):
        self.l=l
        self.b=b
        self.h=h
    def rummal(self):
        return self.l*self.b*self.h
    def yFlatarmal(self):
        return (2*self.l*self.b)+(2*self.l*self.h)+(2*self.b*self.h)

class Pyramid(Rummal):
    def __init__(self,l,b,h):
        self.l=l
        self.b=b
        self.h=h
    def rummal(self):
        return round((self.l*self.b*self.h)/3,2)

class Itrottamadur:
    def __init__(self,nafn,aldur,kyn):
        self.nafn=nafn
        self.aldur=aldur
        self.kyn=kyn
    def kraftur(self):
        return 2
    def upplysingar(self):
        print("Nafn:",self.nafn)
        print("Aldur:",self.aldur)
        print("Kyn:",self.kyn)

class Hlaupari(Itrottamadur):
    def __init__(self,nafn,aldur,kyn,hradi):
        Itrottamadur.__init__(self,nafn,aldur,kyn)
        self.hradi=hradi
    def kraftur(self):
        return super().kraftur()*self.hradi
    def upplysingar(self):
        print("Nafn:",self.nafn)
        print("Aldur:",self.aldur)
        print("Kyn:",self.kyn)
        print("Hraði:",self.hradi)


class Kraftlyftingar(Itrottamadur):
    def __init__(self,nafn,aldur,kyn,styrkur):
        Itrottamadur.__init__(self,nafn,aldur,kyn)
        self.styrkur=styrkur
    def kraftur(self):
        return super().kraftur()*self.styrkur
    def upplysingar(self):
        print("Nafn:",self.nafn)
        print("Aldur:",self.aldur)
        print("Kyn:",self.kyn)
        print("Styrkur:",self.styrkur)

hlaupari1=Hlaupari("Óskar",17,"kk",15)
print(hlaupari1.upplysingar())
kraft1=Kraftlyftingar("Gestur",16,"kk",20)
print(kraft1.upplysingar())

kula1=Kula(5)

kassi1=Kassi(4,7,3)

pyramid1=Pyramid(5,6,8)

print("Rúmmál kúlunnar er:",kula1.rummal())

print("Rúmmál kassans er:",kassi1.rummal())

print("Rúmmál pýramídans er:",pyramid1.rummal())
