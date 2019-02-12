#jon ólafur
#undirbúninngur fyrir timavekr 1
import random


#listi og skráarvinsla
#liður 1
#listi
listiA = []
listiB = []
listiC = []
for x in range(100):
    talaA = random.randint(50,100)
    listiA.append(talaA)
print("listi A",listiA)
print()
for x in range(150):
    talaB = random.randint(75,200)
    listiB.append(talaB)
print("listi B",listiB)
print()
listiC = listiB+listiA
print("listi c",listiC)
print()


#skráarvinsla
listi = []
with open("tolur.txt","w",encoding="utf-8") as f:
    for tala in range(1,21):
        print(tala)
        listi.append(tala)
        f.write(str(listi))
with open("tolur.txt","r",encoding="utf-8") as f:
    texti = f.read()
    skra=texti.split()
    print(texti)

#strenigir/dictionary
#liður 2
#strengir finnar islenska og enska stafi
print()
strengur = "halló heimur"
for x in range(len(strengur)):#prenta út lengd strengs
    print(x)

#strenugr finna tvo stafi í roð
strengur2 = "halló heimur"
for stafur in strengur2:
    if stafur ==2:
        print(stafur)
print()
#dictionary
tafla = {"kústur":123,"skófla":23,"vettlingar":345,"fötur":23,"úlpur":12}
for k,v, in tafla.items():
    print(k,v)
print()
tafla["húfa"]=34
tafla["skór"]=45
for k,v, in tafla.items():
    print(k,v)
print()
listi1=list(tafla.values())#bý til lista úr töfluni svo ég get prentað út hieltöluna
print(listi1)
sum(listi1)
print("heiltala tölunar",sum(listi1))

for k in tafla.items():
    if max(listi1) ==k:
        print(max(listi1),k)
print("þass sem mest er til af",max(listi1))
print("það sem minst er til að",min(listi1))

#liður 3
#föll
#summu listans
def summa_lista():
    tolur1 = [12,34,55]
    tolur2 = [11,22,44]
    tolur3 = tolur1+tolur2
    return sum(tolur3)
#aðalforrit
print("þetta er summa listans",summa_lista())
#meðatal talna
listi = []
def medaltal():
    for tolur in range(10):
        tolur = random.randint(1,10)
        listi.append(tolur)
    medal = sum(listi)/len(listi)
    return medal
#aðalforrit
print("þetta er meðaltal listans",medaltal())
#eigið val
def flatarmal_kassa(hlid):
    flatarmal= hlid*2
    return flatarmal
#aðalforrit
hlid=int(input("slaðu inn hlið"))
print(flatarmal_kassa(hlid))
