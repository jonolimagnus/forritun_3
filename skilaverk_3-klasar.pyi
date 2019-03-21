#jón ólafur
#skilaverkefni 3 klasar
#2019/02/19

import csv
import klasi

verkalydsfelag=[]
def opnaskra():
    with open("verkalydsfelga.csv","r",newline="",encoding="utf-8") as file:
        reader=csv.reader(file,delimiter=";")
        for row in reader:
            print(row)
            hlutur = klasi.Verkalydsfelag(row[0], row[1], row[2], row[3])
            verkalydsfelag.append(hlutur)

def skrifaUt():
    with open("verkalydsfelga.csv","w",newline="",encoding="utf-8") as file:
        writer=csv.writer(file,delimiter=",")
        for x in verkalydsfelag:
            writer.writerow([x.n,x.f,x.l,x.k])
def nyrMedlimur():
    pass
def eydaMedlimi():
    pass
def breytaMedlimi():
    pass
def prentaVerkalidsfelag():
    pass
def nafnLaun():
    return
def utborgunLaun():
    pass


on = 1
while on ==1:
    print("1 opnaskrá")
    print("2 skrifa út")
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
        pass
    elif val == 3:
        pass
    elif val == 4:
        pass
    elif val == 5:
        pass
    elif val == 6:
        pass
    elif val == 7:
        pass
    elif val == 8:
        pass
    elif val == 9:
        pass
    elif val == 10:
        on = 0
    else:
        print("verður að velja milli 1-9")
