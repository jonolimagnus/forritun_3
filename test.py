#jón ólafur
#skilaverkefni 3 klasar
#2019/02/19

import csv
from klasi import Verkalydsfelag

verkalydsfelag=[]
def opnaskra():
    #print("test")
    with open("verkalydsfelag.csv","r",newline="",encoding="utf-8") as file:
        reader=csv.reader(file,delimiter=";")
        for row in reader:
            #print(row)
            hlutur = Verkalydsfelag(row[0], row[1], row[2], row[3])
            verkalydsfelag.append(hlutur)

def skrifaISkra():#skrifa í skrá
    with open("verkalydsfelag.csv","w",newline="",encoding="utf-8") as file:
        writer=csv.writer(file,delimiter=";")
        for x in verkalydsfelag:
            writer.writerow([x.n,x.f,x.l,x.k])

def nyrMedlimur():#bý til nyjan meðlim
    nafn=input("hvað heitir meðlimurinn")
    felags=input("hvað er felgasnumerið")
    laun=input("hver eru launinn")
    kt=input("hver er kennitalan")
    hlutur= klasi.Verkalydsfelag(nafn, felags, laun, kt)
    verkalydsfelag.append(hlutur)

def eydaMedlimi():
    pass

def breytaMedlimi():
    pass

def prentaVerkalidsfelag():#prenti út upplýsingum um meðlimina
    for hlutur in verkalydsfelag:
        hlutur.upplysingar()

def nafnLaun():#prenti út nafn og laun
    for x in verkalydsfelag:
        print(x.n,x.l)

def utborgunLaun():
    pass


on = 1
while on ==1:
    print("1 opnaskrá")
    print("2 skrifa í skrá")
    print("3 nýr meðlimur")
    print("4 eyða meðlimi")
    print("5 breyta meðlimi")
    print("6 prenta verkaliðsfelag")
    print("7 nafn og laun")
    print("8 útborguð laun")
    print("9 work in progress")
    print("10 hætta")
    val = int(input("veldu milli 1-9 10 til að hætta"))

    if val ==1:
        opnaskra()

    elif val == 2:
        skrifaISkra()

    elif val == 3:
        nyrMedlimur()

    elif val == 4:
        eydaMedlimi()

    elif val == 5:
        breytaMedlimi()

    elif val == 6:
        prentaVerkalidsfelag()

    elif val == 7:
        nafnLaun()

    elif val == 8:
        utborgunLaun()

    elif val == 9:
        pass

    elif val == 10:
        on = 0
    else:
        print("verður að velja milli 1-9")
