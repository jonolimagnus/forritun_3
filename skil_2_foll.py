#jón ólafur
#skilaverkefni 2 foll
#bý til defenitions sem eru notaðar á öðru skjali
import time
def langhlid(a,b):#nota pýðagóras til að finna flatarmál
    c2 = (a*a)+(b*b)#langhlið þrihynings
    c = c2%c2
    return c


def margfeldi_af(tala1,tala2):
    if tala1%tala2 ==0:
        print(tala2,"er margfeldi af ",tala1)
    elif tala1%tala2!=0:
        print(tala2,"er ekki marfeldi af",tala1)

def ferningur_ur_stjornu(kassi):
    for x in range(kassi):
        for i in range(kassi):#fjoldi stjarna
            print("*",end="")
        print()#ný lina

def er_slett_tala(tala):
    if tala %2 ==0:#slétt tala
        print(tala,"er slétt tala")
    elif tala %2!=0:#oddatala
        print(tala,"er oddatala")

def flatarmal_hrings(radius):
    summa = radius*radius
    return round(summa,2)#skilar tveim aukastöfumm

def bank_bank(tala):
    for x in range(tala):
        print("bank")
        time.sleep(0.2)
    print("hver er þar")

