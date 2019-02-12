#jón ólafur
#æfingaverk 1A
import random
#strengjarallý
def fjoldi_orda(strengur):#bý til fall
    ord=0
    bil=0
    for stafur in strengur:
        if stafur==" ":#kemur bil
            bil+=1#telur bil
    ord=bil+1
    return"fjöldi orða í þessum texta er "+str(ord)

def fyrstu_5(strengur):
    return strengur[0:5]

def sidustu_4(strengur):
    return strengur[-4:]

def midju_staf(strengur):
    tel=len(strengur)
    if tel % 2==0:#ef það er einginn miðstafur
        return "hér er einginn miðstafur"
    else:
        mid=int(tel/2-0.5)#finn númerið mið staf
        return "miðstafurinn er númer "+str(mid+1)+" sem er stafurinn "+strengur[mid]

def finna_s(strengur):
    temp=""
    for stafur in strengur:
        if stafur =="s" or stafur =="S":
            temp+=stafur
        else:
            temp="$"
    return temp

#aðalforritið
texti=input("skrifaðu inn texta")#bý til strenginn
print(fjoldi_orda(texti))#kallar í fallið
print(fyrstu_5(texti))#sýnir fyrstu 5 stafina
print(sidustu_4(texti))#kallar í síðustu 4 staafina
print(midju_staf(texti))#kallar in miðstafin
print(finna_s(texti))#kalla í finna streng


#listarallý
randomlisti=[]#bý til random lista
for x in range(100):
    tala = random.randint(34,69)
    randomlisti.append(tala)
    if sum(randomlisti)==45000:
        print(sum(randomlisti))
    elif sum(randomlisti)>45000:
        pass
print(randomlisti)
summa = sum(randomlisti)
medaltal=summa/len(randomlisti)
print("meðaltal er",round(medaltal,3))
print(max(randomlisti))#fæ stærstu toluna
print(min(randomlisti))#fæ minstu töluna
print(sum(randomlisti))#fæ summu listans
