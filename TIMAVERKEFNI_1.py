#JON OLAFUR
#TIMAVERKEFNI 1
import random
import time

now =time.localtime()
def gisk_tala():
    for x in range(1):
        tala= random.randint(1,1000)
        print(tala)
def skoda_gisk(tala):
    if Gtala ==tala:
        print("vel gert þú fannst töluna")
        print("viltu spila aftur")
    elif Gtala != tala:
        print("rang tala")
        if Gtala < tala:
            print("of há")
            print("reyndu aftur")
        elif Gtala >tala:
            print("of lág")
            print("reyndu aftur")
def teninga_Kast(teljari_van,teljari_tap):
    end = True
    if kast_1>kast_2:
        print("þú tapaðir")
        end = True
    if kast_1<kast_2:
        print("þú vannst")
        end = False

on = 1
while on == 1:
    print("1 giska tölu")
    print("2 teningakast")
    print("3 takk")
    print("4 hætta")
    val = int(input("veldu milli 1-3 og 4 til að hætta"))

    if val == 1:#bý til tölu og fæ notandann til að giska töluna
        loop = True
        while loop == True:#bý til while loopu sem heldur áfram þangað til þú skrifar 0
            gisk_tala()
            Gtala = float(input("giskaðu tölu milli 1-1000: 0 til að hætta"))
            if Gtala !=0:
                skoda_gisk(Gtala)
            if Gtala ==0:
                loop = False
    elif val ==2:
        teljari_tap=0
        teljari_van=0
        svar = "j"
        while svar=="j":
            for x in range(1):
                kast_1 = random.randint(1,6)
                kast_2 = random.randint(1,6)
                print("talvan ksastar", kast_1)
                print("þú kastar",kast_2)
                if kast_1>kast_2:
                    teljari_tap = teljari_tap +1
                if kast_1<kast_2:
                    teljari_van=teljari_van+1
            teninga_Kast(teljari_tap,teljari_van)
            svar = input("viltu halda áframj/n")
            if svar != "j":
                print("talvan vann svona oft",teljari_tap)
                print("þú vannst svona oft", teljari_van)
    elif val ==3:
        tala = 10
        for x in range(tala):
            print("Takk")
            time.sleep(0.9)
        print("eigðu góðan dag vikudagur", now[6],"mánaðardagur", now[2])
    elif val ==4:
        on =0
    else:
        print("þú verður að velja milli 1-3")
