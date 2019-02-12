#jón ólafur
#skilaverkefni 2 test
import time
from skil_2_foll import *#importa follin af öðru skajlli
# #hér kemur valmynd

nafn = input("hvað er nafnið þitt")
on =1
while on ==1:
    print("liður 1")
    print("liður 2")
    print("liður 3")
    print("liður 4")
    print("liður 5")
    print("liður 6")
    print("hætta 7")
    val=int(input("veldur milli 1-6 7 til að hætta"))
#langhlid
    if val == 1:
        loop = True
        while loop ==True:#bý til loopu sem heldur áfram þar til það er skrifað mínus tölu
            a = float(input("veldu hlið 1: veldu mínus tölur til að hætta"))
            if a>0:
                b = float(input("veldu hlið 2"))
                print(langhlid(a,b))
            elif a<0:
                loop=False

#margfeldi af
    elif val ==2:
        end = True
        while end==True:#bý til loopu sem heldur áfram þar til það er skrifað 0
            tala1 = int(input("sláðu inn fyrstu tölu: veldu 0 til að hætta"))
            if tala1 !=0:
                tala2 = int(input("sláðu inn seinni tölu"))
                margfeldi_af(tala1,tala2)
                end=True
            if tala1 ==0:
                end=False


#fernginru úr stjörnu
    elif val == 3:
        kassi = int(input("veldur hliða stærð fernings"))
        ferningur_ur_stjornu(kassi)


# er slétt tala
    elif val ==4:
        loop =True
        while loop ==True:#bý til loopu sem heldur áfram þar til það er skrifað 0
            tala = int(input("sláðu inn tölu: veldu 0 til að hætta"))
            if tala !=0:
                er_slett_tala(tala)
            elif tala ==0:
                loop=False

#flatarmál hrings
    elif val ==5:
        loop=True
        while loop ==True:
            radius = float(input("sláðu inn radius hrings: veldu minus tölu til að hætta"))
            if radius >-1:
                print(flatarmal_hrings(radius))
            elif radius <-1:
                loop =False

#bank bank
    elif val ==6:
        tala = int(input("sláðu inn sekúndur"))
        bank_bank(tala)

    elif val ==7:
        on =0
        print("takk fyrir að taka þátt",nafn,time)
    else:
        print("þú átt að velja milli 1-6")
