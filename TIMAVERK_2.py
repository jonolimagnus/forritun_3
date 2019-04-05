#jón ólafur
#29/03/19
#timaverkefni 2

#liður 1
def meme():
    meme_tolur = [14,34,21,33,28,91,287,3,54]
    nyr_listi = list(filter(lambda x: (x%7==0), meme_tolur))
    print("þetta eru allar tölurnar sem ganga upp í 7",nyr_listi)
#aðalforrit
print(meme())

#liður 2
tolur = [14,34,21,33,28,91,287,3,54]
y_listi = list(map(lambda x: 2*x+3*(x+1), tolur))
print(y_listi)

#liður 3
class konni:
    def __init__(self,nafn,x,y):
        self.nafn= nafn
        self.x=x
        self.y=y
    def xogy(self,x,y):#skilar lista af tölum á milli x og y
        if self.x ==self.y:
            print("tölurnar eru jafnar")
        else:
            for tala in range(x,y+1):
                print(tala)
    def dict(self):#tekur inn lista og skilar dictionary
        listi2 = [12,18,23]
        dict = {"a","b","c"}
    def medal(self,listi):#skilar meðalatal talna
        medal = sum(listi)/len(listi)
        print(medal)
    def upplysingar(self):
        print("ég er hlutur af klassanum konni")
        print("nafnið mitt er", self.nafn)
        print("x gildi mitt er", self.x)
        print("y gildi mitt er", self.y)
#aðalforrit
konni =konni("jón",2,4)
print(konni.xogy(2,4))
listi = [12,34,56]
print(konni.medal(listi))
print(konni.upplysingar())
"""
listi2 = [12,18,23]
dict = {"a","b","c"}
for lykil, x in dict, listi:
    print(lykil,"=", x)

"""
#LIÐUR 4 erfðir
class Skoli:
    def __init__(self,nafn):
        self.nafn=nafn
    def HverErEg(self):
        return "ég er skólastofnun"
class Framhaldskoli(Skoli):
    def __init__(self,nafn,sernafn,fjoldiN,fjodliB):
        Skoli.__init__(self,nafn)
        self.sernafn=sernafn
        self.fN= fjoldiN
        self.fB= fjodliB
    def HverErEg(self):
        print(Skoli.HverErEg(self),self.nafn,self.sernafn,self.fN,self.fB)
class Grunnskoli(Skoli):
    def __init__(self,nafn,sernafn,fjoldiN,fjodlia):
        Skoli.__init__(self,nafn)
        self.sernafn=sernafn
        self.fN= fjoldiN
        self.fa= fjodlia
    def HverErEg(self):
        print(Skoli.HverErEg(self),self.nafn,self.sernafn,self.fN,self.fa)
#aðalforrit veit ekki hvernig ég losa mig við none
skoli= Skoli("skoli")
Hlutur1= Grunnskoli("nánar tiltekið","öldutæunsskóli",456,34)
Hlutur2= Framhaldskoli("nánar tiltekið","tækniskólinn",2100,300)
print(skoli.nafn)
print(skoli.HverErEg())
print(Hlutur1.sernafn)
print(Hlutur1.HverErEg())
print(Hlutur2.sernafn)
print(Hlutur2.HverErEg())
